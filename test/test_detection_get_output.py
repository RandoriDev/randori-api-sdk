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
from randori_api.models.detection_get_output import DetectionGetOutput  # noqa: E501
from randori_api.rest import ApiException

class TestDetectionGetOutput(unittest.TestCase):
    """DetectionGetOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DetectionGetOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = randori_api.models.detection_get_output.DetectionGetOutput()  # noqa: E501
        if include_optional :
            return DetectionGetOutput(
                count = 56, 
                data = [
                    randori_api.models.detection.detection(
                        detection_criteria = randori_api.models.detection_criteria.detection_criteria(), 
                        hostname_id = '0', 
                        id = '0', 
                        ip_id = '0', 
                        network_id = '0', 
                        org_id = '0', 
                        poc_id = '0', 
                        port_id = '0', )
                    ], 
                offset = 56, 
                total = 56
            )
        else :
            return DetectionGetOutput(
        )

    def testDetectionGetOutput(self):
        """Test DetectionGetOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()