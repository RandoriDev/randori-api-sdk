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

from randori_api_sdk.models.saved_views_model_custom_in import SavedViewsModelCustomIn

class TestSavedViewsModelCustomIn(unittest.TestCase):
    """SavedViewsModelCustomIn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SavedViewsModelCustomIn:
        """Test SavedViewsModelCustomIn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SavedViewsModelCustomIn`
        """
        model = SavedViewsModelCustomIn()
        if include_optional:
            return SavedViewsModelCustomIn(
                description = '',
                entity_type = 'target',
                filter_data = randori_api_sdk.models.filter_data.filter_data(),
                is_favorite = True,
                is_global = True,
                name = '',
                sort_data = randori_api_sdk.models.sort_data.sort_data()
            )
        else:
            return SavedViewsModelCustomIn(
                entity_type = 'target',
                filter_data = randori_api_sdk.models.filter_data.filter_data(),
                sort_data = randori_api_sdk.models.sort_data.sort_data(),
        )
        """

    def testSavedViewsModelCustomIn(self):
        """Test SavedViewsModelCustomIn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
