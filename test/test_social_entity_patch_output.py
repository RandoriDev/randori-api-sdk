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

from randori_api_sdk.models.social_entity_patch_output import SocialEntityPatchOutput

class TestSocialEntityPatchOutput(unittest.TestCase):
    """SocialEntityPatchOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SocialEntityPatchOutput:
        """Test SocialEntityPatchOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SocialEntityPatchOutput`
        """
        model = SocialEntityPatchOutput()
        if include_optional:
            return SocialEntityPatchOutput(
                count = 56
            )
        else:
            return SocialEntityPatchOutput(
        )
        """

    def testSocialEntityPatchOutput(self):
        """Test SocialEntityPatchOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
