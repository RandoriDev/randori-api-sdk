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


class IpPatchIn(object):
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
        'impact_score': 'str',
        'status': 'str'
    }

    attribute_map = {
        'affiliation_state': 'affiliation_state',
        'impact_score': 'impact_score',
        'status': 'status'
    }

    def __init__(self, affiliation_state=None, impact_score=None, status=None, local_vars_configuration=None):  # noqa: E501
        """IpPatchIn - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._affiliation_state = None
        self._impact_score = None
        self._status = None
        self.discriminator = None

        if affiliation_state is not None:
            self.affiliation_state = affiliation_state
        if impact_score is not None:
            self.impact_score = impact_score
        if status is not None:
            self.status = status

    @property
    def affiliation_state(self):
        """Gets the affiliation_state of this IpPatchIn.  # noqa: E501


        :return: The affiliation_state of this IpPatchIn.  # noqa: E501
        :rtype: str
        """
        return self._affiliation_state

    @affiliation_state.setter
    def affiliation_state(self, affiliation_state):
        """Sets the affiliation_state of this IpPatchIn.


        :param affiliation_state: The affiliation_state of this IpPatchIn.  # noqa: E501
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
    def impact_score(self):
        """Gets the impact_score of this IpPatchIn.  # noqa: E501


        :return: The impact_score of this IpPatchIn.  # noqa: E501
        :rtype: str
        """
        return self._impact_score

    @impact_score.setter
    def impact_score(self, impact_score):
        """Sets the impact_score of this IpPatchIn.


        :param impact_score: The impact_score of this IpPatchIn.  # noqa: E501
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
    def status(self):
        """Gets the status of this IpPatchIn.  # noqa: E501


        :return: The status of this IpPatchIn.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IpPatchIn.


        :param status: The status of this IpPatchIn.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Needs Investigation", "Needs Resolution", "Needs Review", "Mitigated", "Accepted"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if not isinstance(other, IpPatchIn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IpPatchIn):
            return True

        return self.to_dict() != other.to_dict()
