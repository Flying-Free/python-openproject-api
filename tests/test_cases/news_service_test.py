import json

from model.new import New
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class NewsServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.newsSer = self.factory.get_news_service()
        with open('../data/new.json') as f:
            self.new = New(json.load(f))

    def test_find(self):
        new = self.newsSer.find(self.new)
        self.assertEqual(new.__dict__, self.new.__dict__)

    def test_find_all(self):
        news_list = self.newsSer.find_all(offset=None, page_size=None, filters=None, sort_by=None)
        # 2 news: One for each project
        self.assertEqual(2, len(news_list))
