from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.relation.relation_command import RelationCommand
from model.schema import Schema


class FindSchemaByType(RelationCommand):

    def __init__(self, connection, type):
        super().__init__(connection)
        self.type = type

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/schema/{self.type}").execute()
            return Schema(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding schema ") from re