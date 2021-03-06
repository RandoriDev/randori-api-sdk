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
from randori_api.models.single_detection_for_target_get_output import SingleDetectionForTargetGetOutput  # noqa: E501
from randori_api.rest import ApiException

class TestSingleDetectionForTargetGetOutput(unittest.TestCase):
    """SingleDetectionForTargetGetOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SingleDetectionForTargetGetOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = randori_api.models.single_detection_for_target_get_output.SingleDetectionForTargetGetOutput()  # noqa: E501
        if include_optional :
            return SingleDetectionForTargetGetOutput(
                count = 56, 
                data = [
                    randori_api.models.single_detection_for_target.single-detection-for-target(
                        affiliation_state = 'None', 
                        applicability = 56, 
                        authorization_state = 'Authorized', 
                        banners_uuid = '0', 
                        cert_uuid = '0', 
                        confidence = 56, 
                        criticality = 56, 
                        deleted = True, 
                        description = '0', 
                        detection_criteria = randori_api.models.detection_criteria.detection_criteria(), 
                        detection_relevance = 56, 
                        enumerability = 56, 
                        first_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        headers_uuid = '0', 
                        hostname = '0', 
                        hostname_id = '0', 
                        id = '0', 
                        impact_score = 'None', 
                        ip = '0', 
                        ip_id = '0', 
                        ip_str = '0', 
                        last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        lens_id = '0', 
                        lens_view = '0', 
                        name = '0', 
                        org_id = '0', 
                        path = '0', 
                        perspective = '0', 
                        perspective_name = '0', 
                        poc_email = '0', 
                        poc_id = '0', 
                        port = 56, 
                        post_exploit = 56, 
                        priority_impact_factor = 1.337, 
                        priority_score = 1.337, 
                        priority_status_factor = 1.337, 
                        priority_tags_factor = 1.337, 
                        private_weakness = 56, 
                        protocol = '0', 
                        public_weakness = 56, 
                        randori_notes = '0', 
                        reference = '0', 
                        research = 56, 
                        screenshot_uuid = '0', 
                        service_id = '0', 
                        status = 'None', 
                        tags = randori_api.models.tags.tags(), 
                        target_confidence = 56, 
                        target_first_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        target_id = '0', 
                        target_last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        target_temptation = 56, 
                        thumbnail_uuid = '0', 
                        vendor = '0', 
                        version = '0', )
                    ], 
                offset = 56, 
                total = 56
            )
        else :
            return SingleDetectionForTargetGetOutput(
        )

    def testSingleDetectionForTargetGetOutput(self):
        """Test SingleDetectionForTargetGetOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
