import model.relation as rel
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from util.Filters import Filters
from util.URL import URL
from util.URLParameter import URLParameter


class FindRelationCandidates(WorkPackageCommand):
    def __init__(self, connection, work_package, filters, query, type, pageSize):
        super().__init__(connection)
        self.work_package = work_package
        self.filters = filters
        self.query = query
        self.type = type
        self.pageSize = pageSize

    def execute(self):
        try:
            json_obj = GetRequest(connection=self.connection,
                                  context=str(URL(f"{self.CONTEXT}"
                                                  f"{self.work_package.id}/available_relation_candidates",
                                                  [
                                                      Filters("filters", self.filters),
                                                      URLParameter("query", self.query),
                                                      URLParameter("type", self.type),
                                                      URLParameter("pageSize", self.pageSize)
                                                  ]))).execute()

            for relation in json_obj["_embedded"]["elements"]:
                yield rel.Relation(relation)
        except RequestError as re:
            raise BusinessError(f"Error finding relation candidates for work package {self.work_package.id}") from re