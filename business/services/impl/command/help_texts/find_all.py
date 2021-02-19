from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.help_texts.help_texts_comand import HelpTextsCommand
from model.help_text import HelpText


class FindAll(HelpTextsCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            for help_text in json_obj['_embedded']['elements']:
                yield HelpText(help_text)
        except RequestError as re:
            raise BusinessError(f"Error finding all grids") from re