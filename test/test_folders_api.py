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
from swagger_client.apis.folders_api import FoldersApi


class TestFoldersApi(unittest.TestCase):
    """ FoldersApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.folders_api.FoldersApi()

    def tearDown(self):
        pass

    def test_create_folder(self):
        """
        Test case for create_folder

        Create Folder
        """
        pass

    def test_delete_folder(self):
        """
        Test case for delete_folder

        Delete Folder
        """
        pass

    def test_delete_folder_sources(self):
        """
        Test case for delete_folder_sources

        Delete Sources
        """
        pass

    def test_retrieve_folder(self):
        """
        Test case for retrieve_folder

        Retrieve Folder
        """
        pass

    def test_retrieve_folder_sources(self):
        """
        Test case for retrieve_folder_sources

        Retrieve Sources
        """
        pass

    def test_retrieve_folders(self):
        """
        Test case for retrieve_folders

        Retrieve Folders
        """
        pass

    def test_update_folder(self):
        """
        Test case for update_folder

        Update Folder
        """
        pass


if __name__ == '__main__':
    unittest.main()
