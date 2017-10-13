# coding: utf-8

"""
    Wealthport API

    Wealthport provides a simple, lightweight and open Web API based on the Open API 2.0 standard (<a href=\"https://www.openapis.org\" target=\"_blank\">https://www.openapis.org</a>). Our APIs offer a variety of operations related to managing Sources, Folders, Orders and Recipes. There are operations to submit and track Jobs, upload and download data files and many more.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.source_request import SourceRequest


class TestSourceRequest(unittest.TestCase):
    """ SourceRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSourceRequest(self):
        """
        Test SourceRequest
        """
        model = swagger_client.models.source_request.SourceRequest()


if __name__ == '__main__':
    unittest.main()
