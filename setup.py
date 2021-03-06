# coding: utf-8

"""
    Wealthport API

    Wealthport provides a simple, lightweight and open Web API based on the Open API 2.0 standard (<a href=\"https://www.openapis.org\" target=\"_blank\">https://www.openapis.org</a>). Our APIs offer a variety of operations related to managing Sources, Folders, Orders and Recipes. There are operations to submit and track Jobs, upload and download data files and many more.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Wealthport API",
    author_email="",
    url="",
    keywords=["Swagger", "Wealthport API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Wealthport provides a simple, lightweight and open Web API based on the Open API 2.0 standard (&lt;a href&#x3D;\&quot;https://www.openapis.org\&quot; target&#x3D;\&quot;_blank\&quot;&gt;https://www.openapis.org&lt;/a&gt;). Our APIs offer a variety of operations related to managing Sources, Folders, Orders and Recipes. There are operations to submit and track Jobs, upload and download data files and many more.
    """
)
