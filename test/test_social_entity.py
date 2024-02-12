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

from randori_api_sdk.models.social_entity import SocialEntity

class TestSocialEntity(unittest.TestCase):
    """SocialEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SocialEntity:
        """Test SocialEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SocialEntity`
        """
        model = SocialEntity()
        if include_optional:
            return SocialEntity(
                address = '',
                affiliation_state = 'None',
                authority = True,
                authority_distance = 56,
                authority_override = True,
                authorization_state = 'Authorized',
                characteristic_tags = [
                    ''
                    ],
                city = '',
                company_name = '',
                confidence = 56,
                country = '',
                deleted = True,
                details = randori_api_sdk.models.details.details(),
                domain = '',
                email = '',
                email_type = '',
                first_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                impact_score = 'None',
                last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                lens_id = '',
                lens_view = '',
                only_in_review_targets = True,
                org_id = '',
                person_first_name = '',
                person_last_name = '',
                person_middle_name = '',
                person_name = '',
                perspective = '',
                perspective_name = '',
                phone = '',
                postal_code = '',
                priority_impact_factor = 1.337,
                priority_score = 1.337,
                priority_status_factor = 1.337,
                priority_tags_factor = 1.337,
                role = '',
                seniority = '',
                state = '',
                status = 'None',
                sub_role = '',
                target_temptation = 56,
                title = '',
                tld = '',
                user_tags = [
                    ''
                    ],
                username = ''
            )
        else:
            return SocialEntity(
                id = '',
                org_id = '',
        )
        """

    def testSocialEntity(self):
        """Test SocialEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
