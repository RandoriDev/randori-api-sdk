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

from randori_api_sdk.models.attack_redirectors import AttackRedirectors

class TestAttackRedirectors(unittest.TestCase):
    """AttackRedirectors unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttackRedirectors:
        """Test AttackRedirectors
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttackRedirectors`
        """
        model = AttackRedirectors()
        if include_optional:
            return AttackRedirectors(
                bart_id = '',
                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted = True,
                external_ip = '',
                external_ip_str = '',
                id = '',
                org_id = '',
                remote_row_id = 56,
                retired = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = '',
                updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                usage = [
                    ''
                    ]
            )
        else:
            return AttackRedirectors(
                bart_id = '',
                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted = True,
                external_ip = '',
                external_ip_str = '',
                org_id = '',
                remote_row_id = 56,
                status = '',
                usage = [
                    ''
                    ],
        )
        """

    def testAttackRedirectors(self):
        """Test AttackRedirectors"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
