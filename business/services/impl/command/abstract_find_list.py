from abc import ABCMeta, abstractmethod

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.command import Command


class AbstractFindList(Command):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        """ Abtract class instance action handling """
        super().__init__(connection)
        if self.__class__ is AbstractFindList:
            raise TypeError('Abstract class cannot be instantiated')

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, self.request_url()).execute()
            for endpoint in json_obj["_embedded"]["elements"]:
                yield self.cast(endpoint)
        except RequestError as re:
            raise BusinessError("Error finding all the concerned endpoints") from re

    @abstractmethod
    def cast(self, endpoint):
        raise NotImplementedError

    @abstractmethod
    def request_url(self):
        raise NotImplementedError