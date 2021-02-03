import json
import os

from model.status import Status
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class StatusServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/status.json')
        self.statusSer = self.factory.get_status_service()
        with open(DATA) as f:
            self.status = Status(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.statusSer.find(self.status))

    def test_find_all(self):
        statuses = self.statusSer.find_all()
        self.assertEqual(14, len(statuses))

    def test_find_by_context(self, context):
        self.assertIsNotNone(self.statusSer.find_by_context(context))
