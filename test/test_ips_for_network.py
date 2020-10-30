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
from randori_api.models.ips_for_network import IpsForNetwork  # noqa: E501
from randori_api.rest import ApiException

class TestIpsForNetwork(unittest.TestCase):
    """IpsForNetwork unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IpsForNetwork
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = randori_api.models.ips_for_network.IpsForNetwork()  # noqa: E501
        if include_optional :
            return IpsForNetwork(
                affiliation_state = 'None', 
                confidence = 56, 
                country = '0', 
                deleted = True, 
                hostname = '0', 
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
                network = '0', 
                network_id = '0', 
                network_str = '0', 
                open_port_count = 56, 
                org_id = '0', 
                perspective = '0', 
                perspective_name = '0', 
                radius = 1.337, 
                service_count = 56, 
                status = 'None', 
                tags = randori_api.models.tags.tags(), 
                target_count = 56, 
                target_temptation = 56
            )
        else :
            return IpsForNetwork(
                id = '0',
                org_id = '0',
        )

    def testIpsForNetwork(self):
        """Test IpsForNetwork"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
