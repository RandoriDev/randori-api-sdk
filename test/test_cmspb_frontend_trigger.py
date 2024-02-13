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

from randori_api_sdk.models.cmspb_frontend_trigger import CmspbFrontendTrigger

class TestCmspbFrontendTrigger(unittest.TestCase):
    """CmspbFrontendTrigger unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CmspbFrontendTrigger:
        """Test CmspbFrontendTrigger
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CmspbFrontendTrigger`
        """
        model = CmspbFrontendTrigger()
        if include_optional:
            return CmspbFrontendTrigger(
                description = '',
                display_value = '',
                field_label = '',
                field_type = '',
                input_variable_path = '',
                is_configurable = True,
                is_matching = True,
                is_standard = True,
                operator = '',
                trigger_identifier = '',
                validation = randori_api_sdk.models.cmspb/frontend_validation.cmspb.FrontendValidation(
                    error_text = '', 
                    kind = '', 
                    value = '', ),
                value = randori_api_sdk.models.structpb/value.structpb.Value(
                    kind = null, )
            )
        else:
            return CmspbFrontendTrigger(
        )
        """

    def testCmspbFrontendTrigger(self):
        """Test CmspbFrontendTrigger"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()