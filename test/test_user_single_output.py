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

from randori_api_sdk.models.user_single_output import UserSingleOutput

class TestUserSingleOutput(unittest.TestCase):
    """UserSingleOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserSingleOutput:
        """Test UserSingleOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSingleOutput`
        """
        model = UserSingleOutput()
        if include_optional:
            return UserSingleOutput(
                data = randori_api_sdk.models.user.user(
                    created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    email = '', 
                    id = '', 
                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    lock_expiry = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    lock_reason = '', 
                    locked = True, 
                    login_type = 'invalid', 
                    managed_personnel = True, 
                    name = 'IRY\"s'eeJ6P6xyTi7xXCY', 
                    password_failures = 56, 
                    title = 'OMaJW=kMowtJ2 'm9Tlc2', 
                    tos_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    tos_version = 56, 
                    totp_failures = 56, 
                    username = 'AWfRPSSEW@gFbDSx9mxCS', 
                    view_org = '', )
            )
        else:
            return UserSingleOutput(
        )
        """

    def testUserSingleOutput(self):
        """Test UserSingleOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()