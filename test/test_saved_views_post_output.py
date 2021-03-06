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
from randori_api.models.saved_views_post_output import SavedViewsPostOutput  # noqa: E501
from randori_api.rest import ApiException

class TestSavedViewsPostOutput(unittest.TestCase):
    """SavedViewsPostOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SavedViewsPostOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = randori_api.models.saved_views_post_output.SavedViewsPostOutput()  # noqa: E501
        if include_optional :
            return SavedViewsPostOutput(
                ids = [
                    '0'
                    ]
            )
        else :
            return SavedViewsPostOutput(
        )

    def testSavedViewsPostOutput(self):
        """Test SavedViewsPostOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
