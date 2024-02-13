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

from randori_api_sdk.models.permission_group import PermissionGroup

class TestPermissionGroup(unittest.TestCase):
    """PermissionGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermissionGroup:
        """Test PermissionGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PermissionGroup`
        """
        model = PermissionGroup()
        if include_optional:
            return PermissionGroup(
                perm_groups = [
                    null
                    ],
                target_user_id = ''
            )
        else:
            return PermissionGroup(
                target_user_id = '',
        )
        """

    def testPermissionGroup(self):
        """Test PermissionGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()