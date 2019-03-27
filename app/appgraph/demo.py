import uuid
from datetime import datetime

import graphene
from flask import current_app
from gql import gql

from app.appgraph.util import get_request_role_userid
from app import const
from app.hasura_client import hasura_client


example_request_result = [{"Min response time":"146","Average Content Size":"12","# failures":"0","Median response time":"150","Name":"/api/","Method":"GET","Max response time":"363","Average response time":"176","Requests/s":"1.13","# requests":"11"},{"Min response time":"0","Average Content Size":"0","# failures":"7","Median response time":"0","Name":"/api/echo/hello","Method":"GET","Max response time":"0","Average response time":"0","Requests/s":"0.00","# requests":"0"},{"Min response time":"0","Average Content Size":"0","# failures":"2","Median response time":"0","Name":"/api/error/400or500","Method":"GET","Max response time":"0","Average response time":"0","Requests/s":"0.00","# requests":"0"},{"Min response time":"0","Average Content Size":"0","# failures":"6","Median response time":"0","Name":"/api/error/401","Method":"GET","Max response time":"0","Average response time":"0","Requests/s":"0.00","# requests":"0"},{"Min response time":"0","Average Content Size":"0","# failures":"8","Median response time":"0","Name":"/api/error/404","Method":"GET","Max response time":"0","Average response time":"0","Requests/s":"0.00","# requests":"0"},{"Min response time":"0","Average Content Size":"0","# failures":"4","Median response time":"0","Name":"/api/random","Method":"GET","Max response time":"0","Average response time":"0","Requests/s":"0.00","# requests":"0"},{"Min response time":"0","Average Content Size":"0","# failures":"4","Median response time":"0","Name":"/api/send","Method":"POST","Max response time":"0","Average response time":"0","Requests/s":"0.00","# requests":"0"},{"Min response time":"146","Average Content Size":"12","# failures":"31","Median response time":"150","Name":"Total","Method":"None","Max response time":"363","Average response time":"176","Requests/s":"1.13","# requests":"11"}]
example_distribution_result = [{"90%":"210","100%":"360","80%":"170","99%":"360","50%":"150","95%":"360","98%":"360","Name":"GET /api/","75%":"170","66%":"170","# requests":"11"},{"90%":"N/A","100%":"N/A","80%":"N/A","99%":"N/A","50%":"N/A","95%":"N/A","98%":"N/A","Name":"/api/echo/hello","75%":"N/A","66%":"N/A","# requests":"0"},{"90%":"N/A","100%":"N/A","80%":"N/A","99%":"N/A","50%":"N/A","95%":"N/A","98%":"N/A","Name":"/api/error/400or500","75%":"N/A","66%":"N/A","# requests":"0"},{"90%":"N/A","100%":"N/A","80%":"N/A","99%":"N/A","50%":"N/A","95%":"N/A","98%":"N/A","Name":"/api/error/401","75%":"N/A","66%":"N/A","# requests":"0"},{"90%":"N/A","100%":"N/A","80%":"N/A","99%":"N/A","50%":"N/A","95%":"N/A","98%":"N/A","Name":"/api/error/404","75%":"N/A","66%":"N/A","# requests":"0"},{"90%":"N/A","100%":"N/A","80%":"N/A","99%":"N/A","50%":"N/A","95%":"N/A","98%":"N/A","Name":"/api/random","75%":"N/A","66%":"N/A","# requests":"0"},{"90%":"N/A","100%":"N/A","80%":"N/A","99%":"N/A","50%":"N/A","95%":"N/A","98%":"N/A","Name":"/api/send","75%":"N/A","66%":"N/A","# requests":"0"},{"90%":"210","100%":"360","80%":"170","99%":"360","50%":"150","95%":"360","98%":"360","Name":"Total","75%":"170","66%":"170","# requests":"11"}]


class PurgeProject(graphene.Mutation):
    """DO NOT USE. Purges project and all related objects from database."""

    class Arguments:
        project_id = graphene.UUID(required=False)
        project_name = graphene.String(required=False, description='Accepts an sql-style wildcard')

    deleted_projects = graphene.List(graphene.UUID)

    def mutate(self, info, project_id=None, project_name=None):
        assert not all((project_id, project_name)), f'use either id or name, not both'

        role, user_id = get_request_role_userid(info)
        assert user_id, f'unauthenticated request'
        assert role == const.ROLE_ADMIN, f'{role} user cannot create projects'

        gclient = hasura_client(current_app.config)

        if project_name:
            projects = gclient.execute(
                gql('''query ($name:String!) { project(where:{name:{_ilike:$name}}) { id } }'''),
                variable_values={'name': project_name}
            )
            project_ids_list = [str(x['id']) for x in projects['project']]
        else:
            project_ids_list = [str(project_id)]

        output = gclient.execute(gql('''mutation ($projIds:[uuid!]!) {
            delete_test_source(where:{project_id:{_in:$projIds}}) { affected_rows }
            delete_test_creator_configuration_m2m (where:{project_id:{_in:$projIds}}) {affected_rows}
            delete_test_creator (where:{test_creator_configuration_m2m:{project_id:{_in:$projIds}}}) {affected_rows}
            delete_configuration_parameter (where:{configuration:{project_id:{_in:$projIds}}}) {affected_rows}
            delete_result_error (where:{execution:{configuration:{project_id:{_in:$projIds}}}}) {affected_rows}
            delete_result_distribution (where:{execution:{configuration:{project_id:{_in:$projIds}}}}) {affected_rows}
            delete_result_aggregate (where:{execution:{configuration:{project_id:{_in:$projIds}}}}) {affected_rows}
            delete_execution (where:{configuration:{project_id:{_in:$projIds}}}) {affected_rows}
            delete_configuration (where:{project_id:{_in:$projIds}}) {affected_rows}
            delete_repository (where:{project_id:{_in:$projIds}}) {affected_rows}
            delete_user_project (where:{project_id:{_in:$projIds}}) {affected_rows}
            delete_project(where:{id:{_in:$projIds}}) {affected_rows}
        }'''), variable_values={'projIds': project_ids_list})

        return PurgeProject(deleted_projects=project_ids_list)


class DemoProject(graphene.Mutation):
    """DO NOT USE. Debug use only. Creates a project with minimal data in database."""

    class Arguments:
        name = graphene.String()
        req_user_id = graphene.UUID(required=False)

    project_id = graphene.UUID()

    def mutate(self, info, name, req_user_id=None):
        # TODO: add some test_creator inputs when ready, maybe some

        UUID = str(uuid.uuid4())
        if not req_user_id:
            req_user_id = UUID
        role, user_id = get_request_role_userid(info)
        assert user_id, f'unauthenticated request'
        assert role == const.ROLE_ADMIN, f'{role} user cannot create projects'

        gclient = hasura_client(current_app.config)

        gclient.execute(gql('''mutation ($id:uuid!, $id2:uuid!, $userId:uuid!, $name:String!, $request_result:json!, $distribution_result:json!, $timestamp:timestamptz!) {
            insert_project (objects:[{id:$id, name:$name}]) {affected_rows}
            insert_user_project (objects:[{id:$id,, project_id:$id, user_id:$userId}]) {affected_rows}
            insert_good_repository: insert_repository (objects:[{id:$id, name:$name, project_id:$id, url:"git@bitbucket.org:acaisoft/load-events.git", type_slug:"load_tests"}]) {affected_rows}
            insert_bad_repository: insert_repository (objects:[{id:$id2, name:"some repo", project_id:$id, url:"git@bitbucket.org:acaisoft/invalid-url.git", type_slug:"load_tests"}]) {affected_rows}
            insert_good_conf_repository: insert_configuration (objects:[{id:$id, name:$name, project_id:$id, repository_id:$id, code_source:"repository", type_slug:"load_tests"}]) {affected_rows}
            insert_bad_conf_repository: insert_configuration (objects:[{name:"conf with some repo", project_id:$id, repository_id:$id2, code_source:"repository", type_slug:"load_tests"}]) {affected_rows}
            insert_execution (objects:[{id:$id, configuration_id:$id, status:"INIT"}]) {affected_rows}
            insert_result_aggregate (objects:[{execution_id:$id, average_response_time:10, number_of_successes:100, number_of_errors:20, number_of_fails:30, average_response_size:1234}]) {affected_rows}
            insert_result_distribution (objects:[{execution_id:$id, request_result:$request_result, distribution_result:$distribution_result, start:$timestamp, end:$timestamp}]) {affected_rows}
            insert_result_error (objects:[{execution_id:$id, error_type:"AssertionError", name:$name, exception_data:"tralala", number_of_occurrences:120}]) {affected_rows}
            insert_host: insert_configuration_parameter (objects:[{configuration_id:$id, parameter_slug:"load_tests_host", value:"https://att-lwd-go-dev.acaisoft.net/api"}]) {affected_rows}
            insert_duration: insert_configuration_parameter (objects:[{configuration_id:$id, parameter_slug:"load_tests_duration", value:"15"}]) {affected_rows}
            insert_conf_creator: insert_configuration (objects:[{id:$id2, name:$name, project_id:$id, code_source:"creator", type_slug:"load_tests"}]) {affected_rows}
            insert_test_creator(objects:[{ id:$id, max_wait:200, min_wait:100, data:{} }]) { affected_rows }
            insert_test_creator_configuration_m2m(objects:[{id:$id, configuration_id:$id2, name:$name, type_slug:"load_tests", project_id:$id }]) { affected_rows }

            source_1: insert_test_source(objects:[{ project_id:$id, source_type:"creator", test_creator_id:$id }]) { affected_rows }
            source_2: insert_test_source(objects:[{ project_id:$id, source_type:"repository", repository_id:$id }]) { affected_rows }
            source_3: insert_test_source(objects:[{ project_id:$id, source_type:"repository", repository_id:$id2 }]) { affected_rows }

        }'''), variable_values={
            'id': UUID, 'id2': str(uuid.uuid4()), 'name': name, 'userId': str(req_user_id),
            'timestamp': datetime.now().astimezone().isoformat(), 'request_result': example_request_result,
            'distribution_result': example_distribution_result,
        })

        return DemoProject(project_id=UUID)