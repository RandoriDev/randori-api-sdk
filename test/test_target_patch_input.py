"""
Copyright © 2022 Randori https://randori.com - All Rights Reserved.
"""

"""
    Randori API

    Endpoints accessible using API tokens  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@randori.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import randori_api
from randori_api.model.hostname_patch_input_operations_inner import HostnamePatchInputOperationsInner
from randori_api.model.hostname_patch_input_q import HostnamePatchInputQ
from randori_api.model.target_patch_input_data import TargetPatchInputData
globals()['HostnamePatchInputOperationsInner'] = HostnamePatchInputOperationsInner
globals()['HostnamePatchInputQ'] = HostnamePatchInputQ
globals()['TargetPatchInputData'] = TargetPatchInputData
from randori_api.model.target_patch_input import TargetPatchInput


class TestTargetPatchInput(unittest.TestCase):
    """TargetPatchInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTargetPatchInput(self):
        """Test TargetPatchInput"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TargetPatchInput()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
