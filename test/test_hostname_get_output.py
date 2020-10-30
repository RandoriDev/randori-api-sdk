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
from randori_api.models.hostname_get_output import HostnameGetOutput  # noqa: E501
from randori_api.rest import ApiException

class TestHostnameGetOutput(unittest.TestCase):
    """HostnameGetOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HostnameGetOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = randori_api.models.hostname_get_output.HostnameGetOutput()  # noqa: E501
        if include_optional :
            return HostnameGetOutput(
                count = 56, 
                data = [
                    randori_api.models.hostname.hostname(
                        affiliation_state = 'None', 
                        confidence = 56, 
                        deleted = True, 
                        first_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        hostname = '0', 
                        id = '0', 
                        impact_score = 'None', 
                        ip_count = 56, 
                        is_prime = True, 
                        last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        lens_id = '0', 
                        lens_view = '0', 
                        max_confidence = 56, 
                        name_type = 56, 
                        only_in_review_targets = True, 
                        org_id = '0', 
                        perspective = '0', 
                        perspective_name = '0', 
                        priority_impact_factor = 1.337, 
                        priority_score = 1.337, 
                        priority_status_factor = 1.337, 
                        priority_tags_factor = 1.337, 
                        status = 'None', 
                        tags = randori_api.models.tags.tags(), 
                        target_temptation = 56, )
                    ], 
                offset = 56, 
                total = 56
            )
        else :
            return HostnameGetOutput(
        )

    def testHostnameGetOutput(self):
        """Test HostnameGetOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
