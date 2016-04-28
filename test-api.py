import unittest
import requests
import xmltodict
from base_test import BaseAPITest


class TestGetIssue(unittest.TestCase):

    #get an issue
    def setUp(self):
        self.base_url = 'https://codespace-api.myjetbrains.com/youtrack/rest'
        self.creds = ('root', 'c11desp@ce')


    def test_get_issue(self):
        url = self.base_url + '/issue/' + 'API-1'
        response = requests.get(url, auth=self.creds)
        r_dict = xmltodict.parse(response.text) #json, html

        self.assertEqual(response.status_code, 200)
        self.assertEqual(r_dict['issue']['@id'], 'API-1')


    def test_get_invalid_issue(self):
        url = self.base_url + '/issue/' + 'ZZZZ'

        r = requests.get(url, auth=self.creds)
        self.assertEqual(r.status_code, 404)

if __name__ == '__main__':
    unittest.main()

