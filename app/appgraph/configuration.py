import graphene
from flask import current_app
from gql import gql

from app.appgraph.util import get_request_role_userid, ValidationInterface, ValidationResponse
from app import validators, const
from app.hasura_client import hasura_client


class ConfigurationParameterInterface(graphene.InputObjectType):
    value = graphene.String()
    parameter_id = graphene.UUID(name='parameter_id')


class ConfigurationInterface(graphene.Interface):
    id = graphene.UUID()


class ConfigurationType(graphene.ObjectType):
    class Meta:
        interfaces = (ConfigurationInterface,)


class Validate(graphene.Mutation):
    """Validates configuration for a testrun. Ensures repository is accessible and test parameters are sane."""

    class Arguments:
        name = graphene.String(
            required=True,
            description='Name, not unique.')
        code_source = graphene.String(
            required=True,
            description=f'Test code source: "{const.CONF_SOURCE_JSON}" or "{const.CONF_SOURCE_REPO}"')
        repository_id = graphene.String(
            required=True,
            name='repository_id',
            description='Repository to fetch test definition from.')
        project_id = graphene.UUID(
            required=True,
            name='project_id',
            description='Project to create test in, user must have access to it.')
        configuration_parameters = graphene.List(
            ConfigurationParameterInterface,
            description='Default parameter types overrides.')

    Output = ValidationInterface

    @staticmethod
    def validate(info, name, code_source, repository_id, project_id, configuration_parameters):
        repository_id = str(repository_id)
        project_id = str(project_id)

        assert code_source in const.CONF_SOURCE_CHOICE, f'invalid choice of code_source ({code_source})'

        role, user_id = get_request_role_userid(info)
        assert user_id, f'unauthenticated request'

        gclient = hasura_client(current_app.config)

        repo = gclient.execute(gql('''query ($confName:String!, $repoId:uuid!, $projId:uuid!, $userId:uuid!) {
            repository_by_pk(id:$repoId) {
                url
                configurationType { slug_name }
                project {
                    is_deleted
                    userProjects { user_id }
                }
            }
            
            parameter {
                id
                default_value
                param_name
                name
            }
            
            user_project (where:{ user_id:{_eq:$userId}, project_id:{_eq:$projId} }) {
                id
            }
            
            project_by_pk(id:$projId) {
                id
            }
            configuration (where:{name:{_eq:$confName}, project:{userProjects:{user_id:{_eq:$userId}}}}) {
                id
            }
            
        }'''), {
            'confName': name,
            'repoId': repository_id,
            'projId': project_id,
            'userId': user_id,
        })

        if role != const.ROLE_ADMIN:
            assert repo.get('user_project', None), \
                f'non-admin ({role}) user {user_id} does not have access to project {project_id}'

        validators.validate_text(name)

        assert repo.get('project_by_pk', None), f'project "{project_id}" does not exist'

        assert len(repo.get('configuration', [])) == 0, f'configuration named "{name}" already exists'

        if repository_id and code_source == const.CONF_SOURCE_REPO:
            assert repo.get('repository_by_pk', None), f'repository does not exist'
            validators.validate_repository(user_id=user_id, repo_config=repo['repository_by_pk'])
            validators.validate_accessibility(current_app.config, repo['repository_by_pk']['url'])

        return validators.validate_test_params(configuration_parameters, defaults=repo['parameter'])

    def mutate(self, info, name, code_source, repository_id, project_id, configuration_parameters):
        Validate.validate(info, name, repository_id, project_id, configuration_parameters)
        return ValidationResponse(ok=True)


class Create(Validate):
    """Validates and saves configuration for a testrun."""

    Output = ConfigurationInterface

    def mutate(self, info, name, code_source, repository_id, project_id, configuration_parameters):
        role, user_id = get_request_role_userid(info)
        gclient = hasura_client(current_app.config)

        patched_params = Validate.validate(info, name, code_source, repository_id, project_id, configuration_parameters)

        query_params = {
            'name': name,
            'repository_id': str(repository_id),
            'project_id': str(project_id),
            'configurationParameters': {'data': []},
        }

        if user_id:
            query_params['created_by_id'] = user_id

        for param_id, param_value in patched_params.items():
            query_params['configurationParameters']['data'].append({
                'parameter_id': param_id,
                'value': param_value,
            })

        query = gql('''mutation ($data:[configuration_insert_input!]!) {
            insert_configuration(
                objects: $data
            ) {
                returning { id } 
            }
        }''')

        conf_response = gclient.execute(query, variable_values={'data': query_params})
        assert conf_response['insert_configuration'], f'cannot save configuration ({str(conf_response)})'

        return ConfigurationType(id=conf_response['insert_configuration']['returning'][0]['id'])
