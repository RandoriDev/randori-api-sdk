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


class ImpactScoreGroupInnerResult(object):
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
        'impact_score': 'str',
        'total': 'int'
    }

    attribute_map = {
        'impact_score': 'impact_score',
        'total': 'total'
    }

    def __init__(self, impact_score=None, total=None, local_vars_configuration=None):  # noqa: E501
        """ImpactScoreGroupInnerResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._impact_score = None
        self._total = None
        self.discriminator = None

        if impact_score is not None:
            self.impact_score = impact_score
        if total is not None:
            self.total = total

    @property
    def impact_score(self):
        """Gets the impact_score of this ImpactScoreGroupInnerResult.  # noqa: E501


        :return: The impact_score of this ImpactScoreGroupInnerResult.  # noqa: E501
        :rtype: str
        """
        return self._impact_score

    @impact_score.setter
    def impact_score(self, impact_score):
        """Sets the impact_score of this ImpactScoreGroupInnerResult.


        :param impact_score: The impact_score of this ImpactScoreGroupInnerResult.  # noqa: E501
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
    def total(self):
        """Gets the total of this ImpactScoreGroupInnerResult.  # noqa: E501


        :return: The total of this ImpactScoreGroupInnerResult.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ImpactScoreGroupInnerResult.


        :param total: The total of this ImpactScoreGroupInnerResult.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if not isinstance(other, ImpactScoreGroupInnerResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImpactScoreGroupInnerResult):
            return True

        return self.to_dict() != other.to_dict()