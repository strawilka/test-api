import requests
import unittest
from base_test import BaseAPITest

class TestDelete(BaseAPITest):

    def setUp(self):
        super(TestDelete, self).setUp()
        self.url = self.base_url + '/issue/'

    def test_delete(self):
        issue_id = self.create_issue()

        r = requests.delete(self.url + issue_id, cookies=self.cookies)

        self.assertEquals(r.status_code, 200)


        r = requests.get(self.url + issue_id, cookies=self.cookies)

        self.assertEquals(r.status_code, 404)

    def test_delete_invalid(self):

        issue_id = 'blabla'

        r = requests.delete(self.url + issue_id, cookies=self.cookies)

        self.assertEquals(r.status_code, 404)