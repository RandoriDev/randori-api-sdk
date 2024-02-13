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

from randori_api_sdk.api.cms_api import CmsApi


class TestCmsApi(unittest.TestCase):
    """CmsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CmsApi()

    def tearDown(self) -> None:
        pass

    def test_frontend_edit_activity_configuration(self) -> None:
        """Test case for frontend_edit_activity_configuration

        Edit activity configurations
        """
        pass

    def test_frontend_edit_activity_configuration_criteria(self) -> None:
        """Test case for frontend_edit_activity_configuration_criteria

        Edit activity configuration criteria
        """
        pass

    def test_frontend_edit_activity_configuration_parameter(self) -> None:
        """Test case for frontend_edit_activity_configuration_parameter

        Edit activity configuration parameter
        """
        pass

    def test_frontend_get_activity_configuration(self) -> None:
        """Test case for frontend_get_activity_configuration

        Get activity configurations
        """
        pass

    def test_frontend_get_configuration_criteria(self) -> None:
        """Test case for frontend_get_configuration_criteria

        Get activity configuration criteria
        """
        pass

    def test_frontend_get_configuration_parameter(self) -> None:
        """Test case for frontend_get_configuration_parameter

        Get activity configuration parameter
        """
        pass

    def test_frontend_list_activity_configuration(self) -> None:
        """Test case for frontend_list_activity_configuration

        List activity configurations
        """
        pass

    def test_frontend_list_activity_configuration_criteria(self) -> None:
        """Test case for frontend_list_activity_configuration_criteria

        List activity configuration criteria
        """
        pass

    def test_frontend_list_activity_configuration_parameters(self) -> None:
        """Test case for frontend_list_activity_configuration_parameters

        List activity configuration parameters
        """
        pass

    def test_frontend_list_applicable_activities(self) -> None:
        """Test case for frontend_list_applicable_activities

        List applicable activity configurations
        """
        pass

    def test_frontend_list_applicable_entities_parameters(self) -> None:
        """Test case for frontend_list_applicable_entities_parameters

        List applicable entities for a configuration
        """
        pass

    def test_frontend_validate_now(self) -> None:
        """Test case for frontend_validate_now

        Start validate now job
        """
        pass


if __name__ == '__main__':
    unittest.main()