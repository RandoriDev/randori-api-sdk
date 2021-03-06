# coding: utf-8

"""
    Randori API

    Endpoints accessible using API tokens  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@randori.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import randori_api
from randori_api.models.attack_implants_get_output import AttackImplantsGetOutput  # noqa: E501
from randori_api.rest import ApiException

class TestAttackImplantsGetOutput(unittest.TestCase):
    """AttackImplantsGetOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AttackImplantsGetOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = randori_api.models.attack_implants_get_output.AttackImplantsGetOutput()  # noqa: E501
        if include_optional :
            return AttackImplantsGetOutput(
                count = 56, 
                data = [
                    randori_api.models.attack_implants.attack-implants(
                        arch = '0', 
                        bart_id = '0', 
                        bits = 56, 
                        created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        host_ips = [
                            '0'
                            ], 
                        hostnames = [
                            '0'
                            ], 
                        id = '0', 
                        last_checkin = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        method = randori_api.models.method.method(), 
                        next_checkin = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        nick = '0', 
                        org_id = '0', 
                        os = '0', 
                        ostype = '0', 
                        osver = '0', 
                        status = '0', 
                        uid = '0', )
                    ], 
                offset = 56, 
                total = 56
            )
        else :
            return AttackImplantsGetOutput(
        )

    def testAttackImplantsGetOutput(self):
        """Test AttackImplantsGetOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
