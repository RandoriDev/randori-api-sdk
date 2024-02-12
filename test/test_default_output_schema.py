# coding: utf-8

"""
    Randori API

    Endpoints accessible using API tokens

    The version of the OpenAPI document: 1.0
    Contact: support@randori.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from randori_api_sdk.models.default_output_schema import DefaultOutputSchema

class TestDefaultOutputSchema(unittest.TestCase):
    """DefaultOutputSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DefaultOutputSchema:
        """Test DefaultOutputSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DefaultOutputSchema`
        """
        model = DefaultOutputSchema()
        if include_optional:
            return DefaultOutputSchema(
                authorization = ''
            )
        else:
            return DefaultOutputSchema(
        )
        """

    def testDefaultOutputSchema(self):
        """Test DefaultOutputSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
