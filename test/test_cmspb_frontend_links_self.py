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

from randori_api_sdk.models.cmspb_frontend_links_self import CmspbFrontendLinksSelf

class TestCmspbFrontendLinksSelf(unittest.TestCase):
    """CmspbFrontendLinksSelf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CmspbFrontendLinksSelf:
        """Test CmspbFrontendLinksSelf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CmspbFrontendLinksSelf`
        """
        model = CmspbFrontendLinksSelf()
        if include_optional:
            return CmspbFrontendLinksSelf(
                var_self = ''
            )
        else:
            return CmspbFrontendLinksSelf(
        )
        """

    def testCmspbFrontendLinksSelf(self):
        """Test CmspbFrontendLinksSelf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
