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

from randori_api_sdk.models.preference_out_collection import PreferenceOutCollection

class TestPreferenceOutCollection(unittest.TestCase):
    """PreferenceOutCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PreferenceOutCollection:
        """Test PreferenceOutCollection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PreferenceOutCollection`
        """
        model = PreferenceOutCollection()
        if include_optional:
            return PreferenceOutCollection(
                preferences = [
                    randori_api_sdk.models.preference_out.preference_out(
                        can_override = True, 
                        preference = null, 
                        preference_source = null, 
                        value = null, )
                    ]
            )
        else:
            return PreferenceOutCollection(
        )
        """

    def testPreferenceOutCollection(self):
        """Test PreferenceOutCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()