import requests
import unittest
from yaml import load


class BaseAPITest(unittest.TestCase):

    def setUp(self):
        self.settings = load(open('settings.yaml').read())
        self.base_url = 'https://codespace-api.myjetbrains.com/youtrack/rest'

        params = {
            'login': self.settings['credentials']['login'],
            'password': self.settings['credentials']['psswd']
        }

        url = self.base_url + '/user/login'
        r = requests.post(url, data=params)
        self.cookies = r.cookies

    def create_issue(self):
        url = self.base_url + '/issue/'

        params = {
            'project': 'API',
            'summary': 'Test summary from robots',
            'description': 'Hail the robots'
        }

        r = requests.put(url, data=params, cookies=self.cookies)
        issue_id = r.headers['location'].split('/')[-1]
        return issue_id