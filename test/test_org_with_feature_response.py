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

from randori_api_sdk.models.org_with_feature_response import OrgWithFeatureResponse

class TestOrgWithFeatureResponse(unittest.TestCase):
    """OrgWithFeatureResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrgWithFeatureResponse:
        """Test OrgWithFeatureResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrgWithFeatureResponse`
        """
        model = OrgWithFeatureResponse()
        if include_optional:
            return OrgWithFeatureResponse(
                end_time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                feature_name = None,
                feature_type = None,
                feature_uuid = '',
                org_name = '',
                org_uuid = '',
                start_time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return OrgWithFeatureResponse(
        )
        """

    def testOrgWithFeatureResponse(self):
        """Test OrgWithFeatureResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
