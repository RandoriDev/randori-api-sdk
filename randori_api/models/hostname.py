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


class Hostname(object):
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
        'affiliation_state': 'str',
        'confidence': 'int',
        'deleted': 'bool',
        'first_seen': 'datetime',
        'hostname': 'str',
        'id': 'str',
        'impact_score': 'str',
        'ip_count': 'int',
        'is_prime': 'bool',
        'last_seen': 'datetime',
        'lens_id': 'str',
        'lens_view': 'str',
        'max_confidence': 'int',
        'name_type': 'int',
        'only_in_review_targets': 'bool',
        'org_id': 'str',
        'perspective': 'str',
        'perspective_name': 'str',
        'priority_impact_factor': 'float',
        'priority_score': 'float',
        'priority_status_factor': 'float',
        'priority_tags_factor': 'float',
        'status': 'str',
        'tags': 'object',
        'target_temptation': 'int'
    }

    attribute_map = {
        'affiliation_state': 'affiliation_state',
        'confidence': 'confidence',
        'deleted': 'deleted',
        'first_seen': 'first_seen',
        'hostname': 'hostname',
        'id': 'id',
        'impact_score': 'impact_score',
        'ip_count': 'ip_count',
        'is_prime': 'is_prime',
        'last_seen': 'last_seen',
        'lens_id': 'lens_id',
        'lens_view': 'lens_view',
        'max_confidence': 'max_confidence',
        'name_type': 'name_type',
        'only_in_review_targets': 'only_in_review_targets',
        'org_id': 'org_id',
        'perspective': 'perspective',
        'perspective_name': 'perspective_name',
        'priority_impact_factor': 'priority_impact_factor',
        'priority_score': 'priority_score',
        'priority_status_factor': 'priority_status_factor',
        'priority_tags_factor': 'priority_tags_factor',
        'status': 'status',
        'tags': 'tags',
        'target_temptation': 'target_temptation'
    }

    def __init__(self, affiliation_state=None, confidence=None, deleted=None, first_seen=None, hostname=None, id=None, impact_score=None, ip_count=None, is_prime=None, last_seen=None, lens_id=None, lens_view=None, max_confidence=None, name_type=None, only_in_review_targets=None, org_id=None, perspective=None, perspective_name=None, priority_impact_factor=None, priority_score=None, priority_status_factor=None, priority_tags_factor=None, status=None, tags=None, target_temptation=None, local_vars_configuration=None):  # noqa: E501
        """Hostname - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._affiliation_state = None
        self._confidence = None
        self._deleted = None
        self._first_seen = None
        self._hostname = None
        self._id = None
        self._impact_score = None
        self._ip_count = None
        self._is_prime = None
        self._last_seen = None
        self._lens_id = None
        self._lens_view = None
        self._max_confidence = None
        self._name_type = None
        self._only_in_review_targets = None
        self._org_id = None
        self._perspective = None
        self._perspective_name = None
        self._priority_impact_factor = None
        self._priority_score = None
        self._priority_status_factor = None
        self._priority_tags_factor = None
        self._status = None
        self._tags = None
        self._target_temptation = None
        self.discriminator = None

        if affiliation_state is not None:
            self.affiliation_state = affiliation_state
        if confidence is not None:
            self.confidence = confidence
        if deleted is not None:
            self.deleted = deleted
        if first_seen is not None:
            self.first_seen = first_seen
        if hostname is not None:
            self.hostname = hostname
        self.id = id
        if impact_score is not None:
            self.impact_score = impact_score
        if ip_count is not None:
            self.ip_count = ip_count
        if is_prime is not None:
            self.is_prime = is_prime
        if last_seen is not None:
            self.last_seen = last_seen
        if lens_id is not None:
            self.lens_id = lens_id
        if lens_view is not None:
            self.lens_view = lens_view
        if max_confidence is not None:
            self.max_confidence = max_confidence
        if name_type is not None:
            self.name_type = name_type
        if only_in_review_targets is not None:
            self.only_in_review_targets = only_in_review_targets
        self.org_id = org_id
        if perspective is not None:
            self.perspective = perspective
        if perspective_name is not None:
            self.perspective_name = perspective_name
        if priority_impact_factor is not None:
            self.priority_impact_factor = priority_impact_factor
        if priority_score is not None:
            self.priority_score = priority_score
        if priority_status_factor is not None:
            self.priority_status_factor = priority_status_factor
        if priority_tags_factor is not None:
            self.priority_tags_factor = priority_tags_factor
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if target_temptation is not None:
            self.target_temptation = target_temptation

    @property
    def affiliation_state(self):
        """Gets the affiliation_state of this Hostname.  # noqa: E501


        :return: The affiliation_state of this Hostname.  # noqa: E501
        :rtype: str
        """
        return self._affiliation_state

    @affiliation_state.setter
    def affiliation_state(self, affiliation_state):
        """Sets the affiliation_state of this Hostname.


        :param affiliation_state: The affiliation_state of this Hostname.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Unaffiliated"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and affiliation_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `affiliation_state` ({0}), must be one of {1}"  # noqa: E501
                .format(affiliation_state, allowed_values)
            )

        self._affiliation_state = affiliation_state

    @property
    def confidence(self):
        """Gets the confidence of this Hostname.  # noqa: E501


        :return: The confidence of this Hostname.  # noqa: E501
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this Hostname.


        :param confidence: The confidence of this Hostname.  # noqa: E501
        :type: int
        """

        self._confidence = confidence

    @property
    def deleted(self):
        """Gets the deleted of this Hostname.  # noqa: E501


        :return: The deleted of this Hostname.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Hostname.


        :param deleted: The deleted of this Hostname.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def first_seen(self):
        """Gets the first_seen of this Hostname.  # noqa: E501


        :return: The first_seen of this Hostname.  # noqa: E501
        :rtype: datetime
        """
        return self._first_seen

    @first_seen.setter
    def first_seen(self, first_seen):
        """Sets the first_seen of this Hostname.


        :param first_seen: The first_seen of this Hostname.  # noqa: E501
        :type: datetime
        """

        self._first_seen = first_seen

    @property
    def hostname(self):
        """Gets the hostname of this Hostname.  # noqa: E501


        :return: The hostname of this Hostname.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Hostname.


        :param hostname: The hostname of this Hostname.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def id(self):
        """Gets the id of this Hostname.  # noqa: E501


        :return: The id of this Hostname.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Hostname.


        :param id: The id of this Hostname.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def impact_score(self):
        """Gets the impact_score of this Hostname.  # noqa: E501


        :return: The impact_score of this Hostname.  # noqa: E501
        :rtype: str
        """
        return self._impact_score

    @impact_score.setter
    def impact_score(self, impact_score):
        """Sets the impact_score of this Hostname.


        :param impact_score: The impact_score of this Hostname.  # noqa: E501
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
    def ip_count(self):
        """Gets the ip_count of this Hostname.  # noqa: E501


        :return: The ip_count of this Hostname.  # noqa: E501
        :rtype: int
        """
        return self._ip_count

    @ip_count.setter
    def ip_count(self, ip_count):
        """Sets the ip_count of this Hostname.


        :param ip_count: The ip_count of this Hostname.  # noqa: E501
        :type: int
        """

        self._ip_count = ip_count

    @property
    def is_prime(self):
        """Gets the is_prime of this Hostname.  # noqa: E501


        :return: The is_prime of this Hostname.  # noqa: E501
        :rtype: bool
        """
        return self._is_prime

    @is_prime.setter
    def is_prime(self, is_prime):
        """Sets the is_prime of this Hostname.


        :param is_prime: The is_prime of this Hostname.  # noqa: E501
        :type: bool
        """

        self._is_prime = is_prime

    @property
    def last_seen(self):
        """Gets the last_seen of this Hostname.  # noqa: E501


        :return: The last_seen of this Hostname.  # noqa: E501
        :rtype: datetime
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this Hostname.


        :param last_seen: The last_seen of this Hostname.  # noqa: E501
        :type: datetime
        """

        self._last_seen = last_seen

    @property
    def lens_id(self):
        """Gets the lens_id of this Hostname.  # noqa: E501


        :return: The lens_id of this Hostname.  # noqa: E501
        :rtype: str
        """
        return self._lens_id

    @lens_id.setter
    def lens_id(self, lens_id):
        """Sets the lens_id of this Hostname.


        :param lens_id: The lens_id of this Hostname.  # noqa: E501
        :type: str
        """

        self._lens_id = lens_id

    @property
    def lens_view(self):
        """Gets the lens_view of this Hostname.  # noqa: E501


        :return: The lens_view of this Hostname.  # noqa: E501
        :rtype: str
        """
        return self._lens_view

    @lens_view.setter
    def lens_view(self, lens_view):
        """Sets the lens_view of this Hostname.


        :param lens_view: The lens_view of this Hostname.  # noqa: E501
        :type: str
        """

        self._lens_view = lens_view

    @property
    def max_confidence(self):
        """Gets the max_confidence of this Hostname.  # noqa: E501


        :return: The max_confidence of this Hostname.  # noqa: E501
        :rtype: int
        """
        return self._max_confidence

    @max_confidence.setter
    def max_confidence(self, max_confidence):
        """Sets the max_confidence of this Hostname.


        :param max_confidence: The max_confidence of this Hostname.  # noqa: E501
        :type: int
        """

        self._max_confidence = max_confidence

    @property
    def name_type(self):
        """Gets the name_type of this Hostname.  # noqa: E501


        :return: The name_type of this Hostname.  # noqa: E501
        :rtype: int
        """
        return self._name_type

    @name_type.setter
    def name_type(self, name_type):
        """Sets the name_type of this Hostname.


        :param name_type: The name_type of this Hostname.  # noqa: E501
        :type: int
        """

        self._name_type = name_type

    @property
    def only_in_review_targets(self):
        """Gets the only_in_review_targets of this Hostname.  # noqa: E501


        :return: The only_in_review_targets of this Hostname.  # noqa: E501
        :rtype: bool
        """
        return self._only_in_review_targets

    @only_in_review_targets.setter
    def only_in_review_targets(self, only_in_review_targets):
        """Sets the only_in_review_targets of this Hostname.


        :param only_in_review_targets: The only_in_review_targets of this Hostname.  # noqa: E501
        :type: bool
        """

        self._only_in_review_targets = only_in_review_targets

    @property
    def org_id(self):
        """Gets the org_id of this Hostname.  # noqa: E501


        :return: The org_id of this Hostname.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Hostname.


        :param org_id: The org_id of this Hostname.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def perspective(self):
        """Gets the perspective of this Hostname.  # noqa: E501


        :return: The perspective of this Hostname.  # noqa: E501
        :rtype: str
        """
        return self._perspective

    @perspective.setter
    def perspective(self, perspective):
        """Sets the perspective of this Hostname.


        :param perspective: The perspective of this Hostname.  # noqa: E501
        :type: str
        """

        self._perspective = perspective

    @property
    def perspective_name(self):
        """Gets the perspective_name of this Hostname.  # noqa: E501


        :return: The perspective_name of this Hostname.  # noqa: E501
        :rtype: str
        """
        return self._perspective_name

    @perspective_name.setter
    def perspective_name(self, perspective_name):
        """Sets the perspective_name of this Hostname.


        :param perspective_name: The perspective_name of this Hostname.  # noqa: E501
        :type: str
        """

        self._perspective_name = perspective_name

    @property
    def priority_impact_factor(self):
        """Gets the priority_impact_factor of this Hostname.  # noqa: E501


        :return: The priority_impact_factor of this Hostname.  # noqa: E501
        :rtype: float
        """
        return self._priority_impact_factor

    @priority_impact_factor.setter
    def priority_impact_factor(self, priority_impact_factor):
        """Sets the priority_impact_factor of this Hostname.


        :param priority_impact_factor: The priority_impact_factor of this Hostname.  # noqa: E501
        :type: float
        """

        self._priority_impact_factor = priority_impact_factor

    @property
    def priority_score(self):
        """Gets the priority_score of this Hostname.  # noqa: E501


        :return: The priority_score of this Hostname.  # noqa: E501
        :rtype: float
        """
        return self._priority_score

    @priority_score.setter
    def priority_score(self, priority_score):
        """Sets the priority_score of this Hostname.


        :param priority_score: The priority_score of this Hostname.  # noqa: E501
        :type: float
        """

        self._priority_score = priority_score

    @property
    def priority_status_factor(self):
        """Gets the priority_status_factor of this Hostname.  # noqa: E501


        :return: The priority_status_factor of this Hostname.  # noqa: E501
        :rtype: float
        """
        return self._priority_status_factor

    @priority_status_factor.setter
    def priority_status_factor(self, priority_status_factor):
        """Sets the priority_status_factor of this Hostname.


        :param priority_status_factor: The priority_status_factor of this Hostname.  # noqa: E501
        :type: float
        """

        self._priority_status_factor = priority_status_factor

    @property
    def priority_tags_factor(self):
        """Gets the priority_tags_factor of this Hostname.  # noqa: E501


        :return: The priority_tags_factor of this Hostname.  # noqa: E501
        :rtype: float
        """
        return self._priority_tags_factor

    @priority_tags_factor.setter
    def priority_tags_factor(self, priority_tags_factor):
        """Sets the priority_tags_factor of this Hostname.


        :param priority_tags_factor: The priority_tags_factor of this Hostname.  # noqa: E501
        :type: float
        """

        self._priority_tags_factor = priority_tags_factor

    @property
    def status(self):
        """Gets the status of this Hostname.  # noqa: E501


        :return: The status of this Hostname.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Hostname.


        :param status: The status of this Hostname.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Needs Investigation", "Needs Resolution", "Needs Review", "Mitigated", "Accepted"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this Hostname.  # noqa: E501


        :return: The tags of this Hostname.  # noqa: E501
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Hostname.


        :param tags: The tags of this Hostname.  # noqa: E501
        :type: object
        """

        self._tags = tags

    @property
    def target_temptation(self):
        """Gets the target_temptation of this Hostname.  # noqa: E501


        :return: The target_temptation of this Hostname.  # noqa: E501
        :rtype: int
        """
        return self._target_temptation

    @target_temptation.setter
    def target_temptation(self, target_temptation):
        """Sets the target_temptation of this Hostname.


        :param target_temptation: The target_temptation of this Hostname.  # noqa: E501
        :type: int
        """

        self._target_temptation = target_temptation

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
        if not isinstance(other, Hostname):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Hostname):
            return True

        return self.to_dict() != other.to_dict()
