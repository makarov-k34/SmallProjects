import unittest

from pyramid.config import Configurator
from webtest import TestApp
from pyramid import testing


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("cornice")
    config.scan("CornTeachers.views")
    return config.make_wsgi_app()

class Views(unittest.TestCase):

    def setUp(self):
        app = main({})
        self.m_testApp = TestApp(app)
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def get_response(self, uri: str):
        self.response = self.m_testApp.get(uri, headers={"usr-timezone": '3'})

    def post_response(self, uri: str, body: object):
        self.response = self.m_testApp.post_json(uri, body, content_type="application/json")
        self.check_http_code(201)

    def put_response(self, uri: str, body: object):
        self.response = self.m_testApp.put_json(uri, body, content_type="application/json")
        self.check_http_code(201)

    def check_http_code(self, http_code: int):
        self.assertEqual(self.response.status_code, http_code)

    def test_all_views(self):
        """Check root"""
        self.get_response('/')  # Check root

        self.get_response("/teaсhers/Ivanov")
        self.get_response("/teaсhers/Ivanov")

        put_json = {
            "name": "newClass",
            "idclass": 1,

        }

        self.put_response('/class/', put_json)
