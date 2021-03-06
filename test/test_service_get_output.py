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
from randori_api.models.service_get_output import ServiceGetOutput  # noqa: E501
from randori_api.rest import ApiException

class TestServiceGetOutput(unittest.TestCase):
    """ServiceGetOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ServiceGetOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = randori_api.models.service_get_output.ServiceGetOutput()  # noqa: E501
        if include_optional :
            return ServiceGetOutput(
                count = 56, 
                data = [
                    randori_api.models.service.service(
                        applicability = 56, 
                        confidence = 56, 
                        criticality = 56, 
                        deleted = True, 
                        description = '0', 
                        enumerability = 56, 
                        first_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '0', 
                        instance_count = 1.337, 
                        ip_count = 1.337, 
                        last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        lens_id = '0', 
                        lens_view = '0', 
                        name = '0', 
                        org_id = '0', 
                        perspective = '0', 
                        perspective_name = '0', 
                        post_exploit = 56, 
                        private_weakness = 56, 
                        public_weakness = 56, 
                        randori_notes = '0', 
                        reference = '0', 
                        research = 56, 
                        service_id = '0', 
                        target_temptation = 56, 
                        vendor = '0', 
                        version = '0', )
                    ], 
                offset = 56, 
                total = 56
            )
        else :
            return ServiceGetOutput(
        )

    def testServiceGetOutput(self):
        """Test ServiceGetOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
