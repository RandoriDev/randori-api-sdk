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
from randori_api.models.artifact_get_output import ArtifactGetOutput  # noqa: E501
from randori_api.rest import ApiException

class TestArtifactGetOutput(unittest.TestCase):
    """ArtifactGetOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ArtifactGetOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = randori_api.models.artifact_get_output.ArtifactGetOutput()  # noqa: E501
        if include_optional :
            return ArtifactGetOutput(
                count = 56, 
                data = [
                    randori_api.models.artifact.artifact(
                        artifact_type = 1.337, 
                        data_hash = '0', 
                        detection_criteria = randori_api.models.detection_criteria.detection_criteria(), 
                        enriched_data = randori_api.models.enriched_data.enriched_data(), 
                        first_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '0', 
                        last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = '0', 
                        src = '0', 
                        src_type = '0', 
                        work_type = '0', )
                    ], 
                offset = 56, 
                total = 56
            )
        else :
            return ArtifactGetOutput(
        )

    def testArtifactGetOutput(self):
        """Test ArtifactGetOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
