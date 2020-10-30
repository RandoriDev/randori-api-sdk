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
from randori_api.models.target_temptation_group_outer_result import TargetTemptationGroupOuterResult  # noqa: E501
from randori_api.rest import ApiException

class TestTargetTemptationGroupOuterResult(unittest.TestCase):
    """TargetTemptationGroupOuterResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TargetTemptationGroupOuterResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = randori_api.models.target_temptation_group_outer_result.TargetTemptationGroupOuterResult()  # noqa: E501
        if include_optional :
            return TargetTemptationGroupOuterResult(
                total_in_ranges = 56, 
                total_other = 56, 
                tt_counts = [
                    randori_api.models.target_temptation_group_inner_result.target_temptation_group_inner_result(
                        total = 56, 
                        tt_range_name = '0', )
                    ]
            )
        else :
            return TargetTemptationGroupOuterResult(
        )

    def testTargetTemptationGroupOuterResult(self):
        """Test TargetTemptationGroupOuterResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
