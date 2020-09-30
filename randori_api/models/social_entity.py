# coding: utf-8

"""
    Randori API

    Endpoints accessible using API tokens  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@randori.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from randori_api.configuration import Configuration


class SocialEntity(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'address': 'str',
        'affiliation_state': 'str',
        'authorization_state': 'str',
        'city': 'str',
        'company_name': 'str',
        'confidence': 'int',
        'country': 'str',
        'deleted': 'bool',
        'details': 'object',
        'domain': 'str',
        'email': 'str',
        'email_type': 'str',
        'first_seen': 'datetime',
        'id': 'str',
        'impact_score': 'str',
        'last_seen': 'datetime',
        'lens_id': 'str',
        'lens_view': 'str',
        'org_id': 'str',
        'person_first_name': 'str',
        'person_last_name': 'str',
        'person_middle_name': 'str',
        'person_name': 'str',
        'perspective': 'str',
        'perspective_name': 'str',
        'phone': 'str',
        'postal_code': 'str',
        'priority_impact_factor': 'float',
        'priority_score': 'float',
        'priority_status_factor': 'float',
        'priority_tags_factor': 'float',
        'role': 'str',
        'seniority': 'str',
        'state': 'str',
        'status': 'str',
        'sub_role': 'str',
        'tags': 'object',
        'target_temptation': 'int',
        'title': 'str',
        'tld': 'str',
        'username': 'str'
    }

    attribute_map = {
        'address': 'address',
        'affiliation_state': 'affiliation_state',
        'authorization_state': 'authorization_state',
        'city': 'city',
        'company_name': 'company_name',
        'confidence': 'confidence',
        'country': 'country',
        'deleted': 'deleted',
        'details': 'details',
        'domain': 'domain',
        'email': 'email',
        'email_type': 'email_type',
        'first_seen': 'first_seen',
        'id': 'id',
        'impact_score': 'impact_score',
        'last_seen': 'last_seen',
        'lens_id': 'lens_id',
        'lens_view': 'lens_view',
        'org_id': 'org_id',
        'person_first_name': 'person_first_name',
        'person_last_name': 'person_last_name',
        'person_middle_name': 'person_middle_name',
        'person_name': 'person_name',
        'perspective': 'perspective',
        'perspective_name': 'perspective_name',
        'phone': 'phone',
        'postal_code': 'postal_code',
        'priority_impact_factor': 'priority_impact_factor',
        'priority_score': 'priority_score',
        'priority_status_factor': 'priority_status_factor',
        'priority_tags_factor': 'priority_tags_factor',
        'role': 'role',
        'seniority': 'seniority',
        'state': 'state',
        'status': 'status',
        'sub_role': 'sub_role',
        'tags': 'tags',
        'target_temptation': 'target_temptation',
        'title': 'title',
        'tld': 'tld',
        'username': 'username'
    }

    def __init__(self, address=None, affiliation_state=None, authorization_state=None, city=None, company_name=None, confidence=None, country=None, deleted=None, details=None, domain=None, email=None, email_type=None, first_seen=None, id=None, impact_score=None, last_seen=None, lens_id=None, lens_view=None, org_id=None, person_first_name=None, person_last_name=None, person_middle_name=None, person_name=None, perspective=None, perspective_name=None, phone=None, postal_code=None, priority_impact_factor=None, priority_score=None, priority_status_factor=None, priority_tags_factor=None, role=None, seniority=None, state=None, status=None, sub_role=None, tags=None, target_temptation=None, title=None, tld=None, username=None, local_vars_configuration=None):  # noqa: E501
        """SocialEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._affiliation_state = None
        self._authorization_state = None
        self._city = None
        self._company_name = None
        self._confidence = None
        self._country = None
        self._deleted = None
        self._details = None
        self._domain = None
        self._email = None
        self._email_type = None
        self._first_seen = None
        self._id = None
        self._impact_score = None
        self._last_seen = None
        self._lens_id = None
        self._lens_view = None
        self._org_id = None
        self._person_first_name = None
        self._person_last_name = None
        self._person_middle_name = None
        self._person_name = None
        self._perspective = None
        self._perspective_name = None
        self._phone = None
        self._postal_code = None
        self._priority_impact_factor = None
        self._priority_score = None
        self._priority_status_factor = None
        self._priority_tags_factor = None
        self._role = None
        self._seniority = None
        self._state = None
        self._status = None
        self._sub_role = None
        self._tags = None
        self._target_temptation = None
        self._title = None
        self._tld = None
        self._username = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if affiliation_state is not None:
            self.affiliation_state = affiliation_state
        if authorization_state is not None:
            self.authorization_state = authorization_state
        if city is not None:
            self.city = city
        if company_name is not None:
            self.company_name = company_name
        if confidence is not None:
            self.confidence = confidence
        if country is not None:
            self.country = country
        if deleted is not None:
            self.deleted = deleted
        if details is not None:
            self.details = details
        if domain is not None:
            self.domain = domain
        if email is not None:
            self.email = email
        if email_type is not None:
            self.email_type = email_type
        if first_seen is not None:
            self.first_seen = first_seen
        self.id = id
        if impact_score is not None:
            self.impact_score = impact_score
        if last_seen is not None:
            self.last_seen = last_seen
        if lens_id is not None:
            self.lens_id = lens_id
        if lens_view is not None:
            self.lens_view = lens_view
        self.org_id = org_id
        if person_first_name is not None:
            self.person_first_name = person_first_name
        if person_last_name is not None:
            self.person_last_name = person_last_name
        if person_middle_name is not None:
            self.person_middle_name = person_middle_name
        if person_name is not None:
            self.person_name = person_name
        if perspective is not None:
            self.perspective = perspective
        if perspective_name is not None:
            self.perspective_name = perspective_name
        if phone is not None:
            self.phone = phone
        if postal_code is not None:
            self.postal_code = postal_code
        if priority_impact_factor is not None:
            self.priority_impact_factor = priority_impact_factor
        if priority_score is not None:
            self.priority_score = priority_score
        if priority_status_factor is not None:
            self.priority_status_factor = priority_status_factor
        if priority_tags_factor is not None:
            self.priority_tags_factor = priority_tags_factor
        if role is not None:
            self.role = role
        if seniority is not None:
            self.seniority = seniority
        if state is not None:
            self.state = state
        if status is not None:
            self.status = status
        if sub_role is not None:
            self.sub_role = sub_role
        if tags is not None:
            self.tags = tags
        if target_temptation is not None:
            self.target_temptation = target_temptation
        if title is not None:
            self.title = title
        if tld is not None:
            self.tld = tld
        if username is not None:
            self.username = username

    @property
    def address(self):
        """Gets the address of this SocialEntity.  # noqa: E501


        :return: The address of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SocialEntity.


        :param address: The address of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def affiliation_state(self):
        """Gets the affiliation_state of this SocialEntity.  # noqa: E501


        :return: The affiliation_state of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._affiliation_state

    @affiliation_state.setter
    def affiliation_state(self, affiliation_state):
        """Sets the affiliation_state of this SocialEntity.


        :param affiliation_state: The affiliation_state of this SocialEntity.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Affiliated", "Unaffiliated"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and affiliation_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `affiliation_state` ({0}), must be one of {1}"  # noqa: E501
                .format(affiliation_state, allowed_values)
            )

        self._affiliation_state = affiliation_state

    @property
    def authorization_state(self):
        """Gets the authorization_state of this SocialEntity.  # noqa: E501


        :return: The authorization_state of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._authorization_state

    @authorization_state.setter
    def authorization_state(self, authorization_state):
        """Sets the authorization_state of this SocialEntity.


        :param authorization_state: The authorization_state of this SocialEntity.  # noqa: E501
        :type: str
        """
        allowed_values = ["Authorized", "Prohibited", "None"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and authorization_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `authorization_state` ({0}), must be one of {1}"  # noqa: E501
                .format(authorization_state, allowed_values)
            )

        self._authorization_state = authorization_state

    @property
    def city(self):
        """Gets the city of this SocialEntity.  # noqa: E501


        :return: The city of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this SocialEntity.


        :param city: The city of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def company_name(self):
        """Gets the company_name of this SocialEntity.  # noqa: E501


        :return: The company_name of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this SocialEntity.


        :param company_name: The company_name of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def confidence(self):
        """Gets the confidence of this SocialEntity.  # noqa: E501


        :return: The confidence of this SocialEntity.  # noqa: E501
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this SocialEntity.


        :param confidence: The confidence of this SocialEntity.  # noqa: E501
        :type: int
        """

        self._confidence = confidence

    @property
    def country(self):
        """Gets the country of this SocialEntity.  # noqa: E501


        :return: The country of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SocialEntity.


        :param country: The country of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def deleted(self):
        """Gets the deleted of this SocialEntity.  # noqa: E501


        :return: The deleted of this SocialEntity.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this SocialEntity.


        :param deleted: The deleted of this SocialEntity.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def details(self):
        """Gets the details of this SocialEntity.  # noqa: E501


        :return: The details of this SocialEntity.  # noqa: E501
        :rtype: object
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this SocialEntity.


        :param details: The details of this SocialEntity.  # noqa: E501
        :type: object
        """

        self._details = details

    @property
    def domain(self):
        """Gets the domain of this SocialEntity.  # noqa: E501


        :return: The domain of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this SocialEntity.


        :param domain: The domain of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def email(self):
        """Gets the email of this SocialEntity.  # noqa: E501


        :return: The email of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SocialEntity.


        :param email: The email of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def email_type(self):
        """Gets the email_type of this SocialEntity.  # noqa: E501


        :return: The email_type of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._email_type

    @email_type.setter
    def email_type(self, email_type):
        """Sets the email_type of this SocialEntity.


        :param email_type: The email_type of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._email_type = email_type

    @property
    def first_seen(self):
        """Gets the first_seen of this SocialEntity.  # noqa: E501


        :return: The first_seen of this SocialEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._first_seen

    @first_seen.setter
    def first_seen(self, first_seen):
        """Sets the first_seen of this SocialEntity.


        :param first_seen: The first_seen of this SocialEntity.  # noqa: E501
        :type: datetime
        """

        self._first_seen = first_seen

    @property
    def id(self):
        """Gets the id of this SocialEntity.  # noqa: E501


        :return: The id of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SocialEntity.


        :param id: The id of this SocialEntity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def impact_score(self):
        """Gets the impact_score of this SocialEntity.  # noqa: E501


        :return: The impact_score of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._impact_score

    @impact_score.setter
    def impact_score(self, impact_score):
        """Sets the impact_score of this SocialEntity.


        :param impact_score: The impact_score of this SocialEntity.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Low", "Medium", "High"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and impact_score not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `impact_score` ({0}), must be one of {1}"  # noqa: E501
                .format(impact_score, allowed_values)
            )

        self._impact_score = impact_score

    @property
    def last_seen(self):
        """Gets the last_seen of this SocialEntity.  # noqa: E501


        :return: The last_seen of this SocialEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this SocialEntity.


        :param last_seen: The last_seen of this SocialEntity.  # noqa: E501
        :type: datetime
        """

        self._last_seen = last_seen

    @property
    def lens_id(self):
        """Gets the lens_id of this SocialEntity.  # noqa: E501


        :return: The lens_id of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._lens_id

    @lens_id.setter
    def lens_id(self, lens_id):
        """Sets the lens_id of this SocialEntity.


        :param lens_id: The lens_id of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._lens_id = lens_id

    @property
    def lens_view(self):
        """Gets the lens_view of this SocialEntity.  # noqa: E501


        :return: The lens_view of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._lens_view

    @lens_view.setter
    def lens_view(self, lens_view):
        """Sets the lens_view of this SocialEntity.


        :param lens_view: The lens_view of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._lens_view = lens_view

    @property
    def org_id(self):
        """Gets the org_id of this SocialEntity.  # noqa: E501


        :return: The org_id of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this SocialEntity.


        :param org_id: The org_id of this SocialEntity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def person_first_name(self):
        """Gets the person_first_name of this SocialEntity.  # noqa: E501


        :return: The person_first_name of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._person_first_name

    @person_first_name.setter
    def person_first_name(self, person_first_name):
        """Sets the person_first_name of this SocialEntity.


        :param person_first_name: The person_first_name of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._person_first_name = person_first_name

    @property
    def person_last_name(self):
        """Gets the person_last_name of this SocialEntity.  # noqa: E501


        :return: The person_last_name of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._person_last_name

    @person_last_name.setter
    def person_last_name(self, person_last_name):
        """Sets the person_last_name of this SocialEntity.


        :param person_last_name: The person_last_name of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._person_last_name = person_last_name

    @property
    def person_middle_name(self):
        """Gets the person_middle_name of this SocialEntity.  # noqa: E501


        :return: The person_middle_name of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._person_middle_name

    @person_middle_name.setter
    def person_middle_name(self, person_middle_name):
        """Sets the person_middle_name of this SocialEntity.


        :param person_middle_name: The person_middle_name of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._person_middle_name = person_middle_name

    @property
    def person_name(self):
        """Gets the person_name of this SocialEntity.  # noqa: E501


        :return: The person_name of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._person_name

    @person_name.setter
    def person_name(self, person_name):
        """Sets the person_name of this SocialEntity.


        :param person_name: The person_name of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._person_name = person_name

    @property
    def perspective(self):
        """Gets the perspective of this SocialEntity.  # noqa: E501


        :return: The perspective of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._perspective

    @perspective.setter
    def perspective(self, perspective):
        """Sets the perspective of this SocialEntity.


        :param perspective: The perspective of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._perspective = perspective

    @property
    def perspective_name(self):
        """Gets the perspective_name of this SocialEntity.  # noqa: E501


        :return: The perspective_name of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._perspective_name

    @perspective_name.setter
    def perspective_name(self, perspective_name):
        """Sets the perspective_name of this SocialEntity.


        :param perspective_name: The perspective_name of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._perspective_name = perspective_name

    @property
    def phone(self):
        """Gets the phone of this SocialEntity.  # noqa: E501


        :return: The phone of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this SocialEntity.


        :param phone: The phone of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def postal_code(self):
        """Gets the postal_code of this SocialEntity.  # noqa: E501


        :return: The postal_code of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this SocialEntity.


        :param postal_code: The postal_code of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def priority_impact_factor(self):
        """Gets the priority_impact_factor of this SocialEntity.  # noqa: E501


        :return: The priority_impact_factor of this SocialEntity.  # noqa: E501
        :rtype: float
        """
        return self._priority_impact_factor

    @priority_impact_factor.setter
    def priority_impact_factor(self, priority_impact_factor):
        """Sets the priority_impact_factor of this SocialEntity.


        :param priority_impact_factor: The priority_impact_factor of this SocialEntity.  # noqa: E501
        :type: float
        """

        self._priority_impact_factor = priority_impact_factor

    @property
    def priority_score(self):
        """Gets the priority_score of this SocialEntity.  # noqa: E501


        :return: The priority_score of this SocialEntity.  # noqa: E501
        :rtype: float
        """
        return self._priority_score

    @priority_score.setter
    def priority_score(self, priority_score):
        """Sets the priority_score of this SocialEntity.


        :param priority_score: The priority_score of this SocialEntity.  # noqa: E501
        :type: float
        """

        self._priority_score = priority_score

    @property
    def priority_status_factor(self):
        """Gets the priority_status_factor of this SocialEntity.  # noqa: E501


        :return: The priority_status_factor of this SocialEntity.  # noqa: E501
        :rtype: float
        """
        return self._priority_status_factor

    @priority_status_factor.setter
    def priority_status_factor(self, priority_status_factor):
        """Sets the priority_status_factor of this SocialEntity.


        :param priority_status_factor: The priority_status_factor of this SocialEntity.  # noqa: E501
        :type: float
        """

        self._priority_status_factor = priority_status_factor

    @property
    def priority_tags_factor(self):
        """Gets the priority_tags_factor of this SocialEntity.  # noqa: E501


        :return: The priority_tags_factor of this SocialEntity.  # noqa: E501
        :rtype: float
        """
        return self._priority_tags_factor

    @priority_tags_factor.setter
    def priority_tags_factor(self, priority_tags_factor):
        """Sets the priority_tags_factor of this SocialEntity.


        :param priority_tags_factor: The priority_tags_factor of this SocialEntity.  # noqa: E501
        :type: float
        """

        self._priority_tags_factor = priority_tags_factor

    @property
    def role(self):
        """Gets the role of this SocialEntity.  # noqa: E501


        :return: The role of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this SocialEntity.


        :param role: The role of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def seniority(self):
        """Gets the seniority of this SocialEntity.  # noqa: E501


        :return: The seniority of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._seniority

    @seniority.setter
    def seniority(self, seniority):
        """Sets the seniority of this SocialEntity.


        :param seniority: The seniority of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._seniority = seniority

    @property
    def state(self):
        """Gets the state of this SocialEntity.  # noqa: E501


        :return: The state of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SocialEntity.


        :param state: The state of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def status(self):
        """Gets the status of this SocialEntity.  # noqa: E501


        :return: The status of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SocialEntity.


        :param status: The status of this SocialEntity.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Investigate", "In-progress", "Reviewed", "Resolved"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def sub_role(self):
        """Gets the sub_role of this SocialEntity.  # noqa: E501


        :return: The sub_role of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._sub_role

    @sub_role.setter
    def sub_role(self, sub_role):
        """Sets the sub_role of this SocialEntity.


        :param sub_role: The sub_role of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._sub_role = sub_role

    @property
    def tags(self):
        """Gets the tags of this SocialEntity.  # noqa: E501


        :return: The tags of this SocialEntity.  # noqa: E501
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SocialEntity.


        :param tags: The tags of this SocialEntity.  # noqa: E501
        :type: object
        """

        self._tags = tags

    @property
    def target_temptation(self):
        """Gets the target_temptation of this SocialEntity.  # noqa: E501


        :return: The target_temptation of this SocialEntity.  # noqa: E501
        :rtype: int
        """
        return self._target_temptation

    @target_temptation.setter
    def target_temptation(self, target_temptation):
        """Sets the target_temptation of this SocialEntity.


        :param target_temptation: The target_temptation of this SocialEntity.  # noqa: E501
        :type: int
        """

        self._target_temptation = target_temptation

    @property
    def title(self):
        """Gets the title of this SocialEntity.  # noqa: E501


        :return: The title of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SocialEntity.


        :param title: The title of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def tld(self):
        """Gets the tld of this SocialEntity.  # noqa: E501


        :return: The tld of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._tld

    @tld.setter
    def tld(self, tld):
        """Sets the tld of this SocialEntity.


        :param tld: The tld of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._tld = tld

    @property
    def username(self):
        """Gets the username of this SocialEntity.  # noqa: E501


        :return: The username of this SocialEntity.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SocialEntity.


        :param username: The username of this SocialEntity.  # noqa: E501
        :type: str
        """

        self._username = username

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SocialEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SocialEntity):
            return True

        return self.to_dict() != other.to_dict()
