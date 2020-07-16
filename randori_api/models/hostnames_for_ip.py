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


class HostnamesForIp(object):
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
        'first_seen': 'str',
        'hostname': 'str',
        'hostname_id': 'str',
        'id': 'str',
        'impact_score': 'str',
        'ip_id': 'str',
        'last_seen': 'str',
        'max_confidence': 'int',
        'org_id': 'str',
        'perspective': 'str',
        'perspective_name': 'str',
        'refreshed': 'bool',
        'status': 'str',
        'tags': 'object'
    }

    attribute_map = {
        'affiliation_state': 'affiliation_state',
        'confidence': 'confidence',
        'deleted': 'deleted',
        'first_seen': 'first_seen',
        'hostname': 'hostname',
        'hostname_id': 'hostname_id',
        'id': 'id',
        'impact_score': 'impact_score',
        'ip_id': 'ip_id',
        'last_seen': 'last_seen',
        'max_confidence': 'max_confidence',
        'org_id': 'org_id',
        'perspective': 'perspective',
        'perspective_name': 'perspective_name',
        'refreshed': 'refreshed',
        'status': 'status',
        'tags': 'tags'
    }

    def __init__(self, affiliation_state=None, confidence=None, deleted=None, first_seen=None, hostname=None, hostname_id=None, id=None, impact_score=None, ip_id=None, last_seen=None, max_confidence=None, org_id=None, perspective=None, perspective_name=None, refreshed=None, status=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """HostnamesForIp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._affiliation_state = None
        self._confidence = None
        self._deleted = None
        self._first_seen = None
        self._hostname = None
        self._hostname_id = None
        self._id = None
        self._impact_score = None
        self._ip_id = None
        self._last_seen = None
        self._max_confidence = None
        self._org_id = None
        self._perspective = None
        self._perspective_name = None
        self._refreshed = None
        self._status = None
        self._tags = None
        self.discriminator = None

        if affiliation_state is not None:
            self.affiliation_state = affiliation_state
        self.confidence = confidence
        if deleted is not None:
            self.deleted = deleted
        if first_seen is not None:
            self.first_seen = first_seen
        self.hostname = hostname
        self.hostname_id = hostname_id
        self.id = id
        if impact_score is not None:
            self.impact_score = impact_score
        self.ip_id = ip_id
        if last_seen is not None:
            self.last_seen = last_seen
        self.max_confidence = max_confidence
        self.org_id = org_id
        self.perspective = perspective
        self.perspective_name = perspective_name
        if refreshed is not None:
            self.refreshed = refreshed
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags

    @property
    def affiliation_state(self):
        """Gets the affiliation_state of this HostnamesForIp.  # noqa: E501


        :return: The affiliation_state of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._affiliation_state

    @affiliation_state.setter
    def affiliation_state(self, affiliation_state):
        """Sets the affiliation_state of this HostnamesForIp.


        :param affiliation_state: The affiliation_state of this HostnamesForIp.  # noqa: E501
        :type: str
        """
        allowed_values = ["Affiliated", "Unaffiliated", "None"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and affiliation_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `affiliation_state` ({0}), must be one of {1}"  # noqa: E501
                .format(affiliation_state, allowed_values)
            )

        self._affiliation_state = affiliation_state

    @property
    def confidence(self):
        """Gets the confidence of this HostnamesForIp.  # noqa: E501


        :return: The confidence of this HostnamesForIp.  # noqa: E501
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this HostnamesForIp.


        :param confidence: The confidence of this HostnamesForIp.  # noqa: E501
        :type: int
        """

        self._confidence = confidence

    @property
    def deleted(self):
        """Gets the deleted of this HostnamesForIp.  # noqa: E501


        :return: The deleted of this HostnamesForIp.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this HostnamesForIp.


        :param deleted: The deleted of this HostnamesForIp.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def first_seen(self):
        """Gets the first_seen of this HostnamesForIp.  # noqa: E501


        :return: The first_seen of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._first_seen

    @first_seen.setter
    def first_seen(self, first_seen):
        """Sets the first_seen of this HostnamesForIp.


        :param first_seen: The first_seen of this HostnamesForIp.  # noqa: E501
        :type: str
        """

        self._first_seen = first_seen

    @property
    def hostname(self):
        """Gets the hostname of this HostnamesForIp.  # noqa: E501


        :return: The hostname of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this HostnamesForIp.


        :param hostname: The hostname of this HostnamesForIp.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def hostname_id(self):
        """Gets the hostname_id of this HostnamesForIp.  # noqa: E501


        :return: The hostname_id of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._hostname_id

    @hostname_id.setter
    def hostname_id(self, hostname_id):
        """Sets the hostname_id of this HostnamesForIp.


        :param hostname_id: The hostname_id of this HostnamesForIp.  # noqa: E501
        :type: str
        """

        self._hostname_id = hostname_id

    @property
    def id(self):
        """Gets the id of this HostnamesForIp.  # noqa: E501


        :return: The id of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HostnamesForIp.


        :param id: The id of this HostnamesForIp.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def impact_score(self):
        """Gets the impact_score of this HostnamesForIp.  # noqa: E501


        :return: The impact_score of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._impact_score

    @impact_score.setter
    def impact_score(self, impact_score):
        """Sets the impact_score of this HostnamesForIp.


        :param impact_score: The impact_score of this HostnamesForIp.  # noqa: E501
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
    def ip_id(self):
        """Gets the ip_id of this HostnamesForIp.  # noqa: E501


        :return: The ip_id of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._ip_id

    @ip_id.setter
    def ip_id(self, ip_id):
        """Sets the ip_id of this HostnamesForIp.


        :param ip_id: The ip_id of this HostnamesForIp.  # noqa: E501
        :type: str
        """

        self._ip_id = ip_id

    @property
    def last_seen(self):
        """Gets the last_seen of this HostnamesForIp.  # noqa: E501


        :return: The last_seen of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this HostnamesForIp.


        :param last_seen: The last_seen of this HostnamesForIp.  # noqa: E501
        :type: str
        """

        self._last_seen = last_seen

    @property
    def max_confidence(self):
        """Gets the max_confidence of this HostnamesForIp.  # noqa: E501


        :return: The max_confidence of this HostnamesForIp.  # noqa: E501
        :rtype: int
        """
        return self._max_confidence

    @max_confidence.setter
    def max_confidence(self, max_confidence):
        """Sets the max_confidence of this HostnamesForIp.


        :param max_confidence: The max_confidence of this HostnamesForIp.  # noqa: E501
        :type: int
        """

        self._max_confidence = max_confidence

    @property
    def org_id(self):
        """Gets the org_id of this HostnamesForIp.  # noqa: E501


        :return: The org_id of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this HostnamesForIp.


        :param org_id: The org_id of this HostnamesForIp.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def perspective(self):
        """Gets the perspective of this HostnamesForIp.  # noqa: E501


        :return: The perspective of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._perspective

    @perspective.setter
    def perspective(self, perspective):
        """Sets the perspective of this HostnamesForIp.


        :param perspective: The perspective of this HostnamesForIp.  # noqa: E501
        :type: str
        """

        self._perspective = perspective

    @property
    def perspective_name(self):
        """Gets the perspective_name of this HostnamesForIp.  # noqa: E501


        :return: The perspective_name of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._perspective_name

    @perspective_name.setter
    def perspective_name(self, perspective_name):
        """Sets the perspective_name of this HostnamesForIp.


        :param perspective_name: The perspective_name of this HostnamesForIp.  # noqa: E501
        :type: str
        """

        self._perspective_name = perspective_name

    @property
    def refreshed(self):
        """Gets the refreshed of this HostnamesForIp.  # noqa: E501


        :return: The refreshed of this HostnamesForIp.  # noqa: E501
        :rtype: bool
        """
        return self._refreshed

    @refreshed.setter
    def refreshed(self, refreshed):
        """Sets the refreshed of this HostnamesForIp.


        :param refreshed: The refreshed of this HostnamesForIp.  # noqa: E501
        :type: bool
        """

        self._refreshed = refreshed

    @property
    def status(self):
        """Gets the status of this HostnamesForIp.  # noqa: E501


        :return: The status of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HostnamesForIp.


        :param status: The status of this HostnamesForIp.  # noqa: E501
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
        """Gets the tags of this HostnamesForIp.  # noqa: E501


        :return: The tags of this HostnamesForIp.  # noqa: E501
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this HostnamesForIp.


        :param tags: The tags of this HostnamesForIp.  # noqa: E501
        :type: object
        """

        self._tags = tags

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
        if not isinstance(other, HostnamesForIp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HostnamesForIp):
            return True

        return self.to_dict() != other.to_dict()
