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
from randori_api.models.ips_for_service_get_output import IpsForServiceGetOutput  # noqa: E501
from randori_api.rest import ApiException

class TestIpsForServiceGetOutput(unittest.TestCase):
    """IpsForServiceGetOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IpsForServiceGetOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = randori_api.models.ips_for_service_get_output.IpsForServiceGetOutput()  # noqa: E501
        if include_optional :
            return IpsForServiceGetOutput(
                count = 56, 
                data = [
                    randori_api.models.ips_for_service.ips-for-service(
                        affiliation_state = 'None', 
                        confidence = 56, 
                        country = '0', 
                        deleted = True, 
                        first_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '0', 
                        impact_score = 'None', 
                        ip = '0', 
                        ip_id = '0', 
                        ip_str = '0', 
                        last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        latitude = 1.337, 
                        lens_id = '0', 
                        lens_view = '0', 
                        longitude = 1.337, 
                        open_port_count = 56, 
                        org_id = '0', 
                        perspective = '0', 
                        perspective_name = '0', 
                        radius = 1.337, 
                        service_count = 56, 
                        service_id = '0', 
                        status = 'None', 
                        target_count = 56, 
                        target_temptation = 56, )
                    ], 
                offset = 56, 
                total = 56
            )
        else :
            return IpsForServiceGetOutput(
        )

    def testIpsForServiceGetOutput(self):
        """Test IpsForServiceGetOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
