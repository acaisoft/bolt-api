import graphene
import json

from flask import current_app
from services import gql_util
from services.hasura import hce


class ExecutionLogInterface(graphene.Interface):
    data = graphene.JSONString()
    argo_id = graphene.String()


class CreateExecutionLog(graphene.Mutation):

    class Arguments:
        data = graphene.JSONString()
        argo_id = graphene.String()

    Output = gql_util.OutputInterfaceFactory(ExecutionLogInterface, 'Create')

    @staticmethod
    def validate(info, data, argo_id):
        assert type(argo_id) is str, f'argo_id must be string'

    def mutate(self, info, data, argo_id):
        CreateExecutionLog.validate(info, data, argo_id)
        query = '''
            mutation ($data: json, $argo_id: String) {
                insert_argo_execution_log (objects: [{data: $data, argo_id: $argo_id}]){
                    affected_rows
                }
            }
        '''
        if type(data) is str:
            data = json.loads(data)
        elif type(data) is dict:
            pass
        query_params = {'data': data, 'argo_id': argo_id}
        resp = hce(current_app.config, query, variable_values=query_params)
        return gql_util.OutputValueFromFactory(CreateExecutionLog, {'returning': [{}]})