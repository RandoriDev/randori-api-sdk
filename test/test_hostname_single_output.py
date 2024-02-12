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

from randori_api_sdk.models.hostname_single_output import HostnameSingleOutput

class TestHostnameSingleOutput(unittest.TestCase):
    """HostnameSingleOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HostnameSingleOutput:
        """Test HostnameSingleOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HostnameSingleOutput`
        """
        model = HostnameSingleOutput()
        if include_optional:
            return HostnameSingleOutput(
                data = randori_api_sdk.models.hostname.hostname(
                    affiliation_state = 'None', 
                    authority = True, 
                    authority_distance = 56, 
                    authority_override = True, 
                    characteristic_tags = [
                        ''
                        ], 
                    confidence = 56, 
                    deleted = True, 
                    first_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    hostname = '', 
                    id = '', 
                    impact_score = 'None', 
                    ip_count = 56, 
                    ips = [
                        ''
                        ], 
                    is_prime = True, 
                    last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    lens_id = '', 
                    lens_view = '', 
                    max_confidence = 56, 
                    name_type = 56, 
                    only_in_review_targets = True, 
                    org_id = '', 
                    perspective = '', 
                    perspective_name = '', 
                    priority_impact_factor = 1.337, 
                    priority_score = 1.337, 
                    priority_status_factor = 1.337, 
                    priority_tags_factor = 1.337, 
                    status = 'None', 
                    target_temptation = 56, 
                    user_tags = [
                        ''
                        ], )
            )
        else:
            return HostnameSingleOutput(
        )
        """

    def testHostnameSingleOutput(self):
        """Test HostnameSingleOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
