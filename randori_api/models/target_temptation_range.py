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


class TargetTemptationRange(object):
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
        'tt_max': 'int',
        'tt_min': 'int',
        'tt_range_name': 'str'
    }

    attribute_map = {
        'tt_max': 'tt_max',
        'tt_min': 'tt_min',
        'tt_range_name': 'tt_range_name'
    }

    def __init__(self, tt_max=None, tt_min=None, tt_range_name=None, local_vars_configuration=None):  # noqa: E501
        """TargetTemptationRange - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tt_max = None
        self._tt_min = None
        self._tt_range_name = None
        self.discriminator = None

        self.tt_max = tt_max
        self.tt_min = tt_min
        self.tt_range_name = tt_range_name

    @property
    def tt_max(self):
        """Gets the tt_max of this TargetTemptationRange.  # noqa: E501

        Inclusive of provided value  # noqa: E501

        :return: The tt_max of this TargetTemptationRange.  # noqa: E501
        :rtype: int
        """
        return self._tt_max

    @tt_max.setter
    def tt_max(self, tt_max):
        """Sets the tt_max of this TargetTemptationRange.

        Inclusive of provided value  # noqa: E501

        :param tt_max: The tt_max of this TargetTemptationRange.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and tt_max is None:  # noqa: E501
            raise ValueError("Invalid value for `tt_max`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tt_max is not None and tt_max > 100):  # noqa: E501
            raise ValueError("Invalid value for `tt_max`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tt_max is not None and tt_max < 0):  # noqa: E501
            raise ValueError("Invalid value for `tt_max`, must be a value greater than or equal to `0`")  # noqa: E501

        self._tt_max = tt_max

    @property
    def tt_min(self):
        """Gets the tt_min of this TargetTemptationRange.  # noqa: E501

        Inclusive of provided value  # noqa: E501

        :return: The tt_min of this TargetTemptationRange.  # noqa: E501
        :rtype: int
        """
        return self._tt_min

    @tt_min.setter
    def tt_min(self, tt_min):
        """Sets the tt_min of this TargetTemptationRange.

        Inclusive of provided value  # noqa: E501

        :param tt_min: The tt_min of this TargetTemptationRange.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and tt_min is None:  # noqa: E501
            raise ValueError("Invalid value for `tt_min`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tt_min is not None and tt_min > 100):  # noqa: E501
            raise ValueError("Invalid value for `tt_min`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tt_min is not None and tt_min < 0):  # noqa: E501
            raise ValueError("Invalid value for `tt_min`, must be a value greater than or equal to `0`")  # noqa: E501

        self._tt_min = tt_min

    @property
    def tt_range_name(self):
        """Gets the tt_range_name of this TargetTemptationRange.  # noqa: E501


        :return: The tt_range_name of this TargetTemptationRange.  # noqa: E501
        :rtype: str
        """
        return self._tt_range_name

    @tt_range_name.setter
    def tt_range_name(self, tt_range_name):
        """Sets the tt_range_name of this TargetTemptationRange.


        :param tt_range_name: The tt_range_name of this TargetTemptationRange.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tt_range_name is None:  # noqa: E501
            raise ValueError("Invalid value for `tt_range_name`, must not be `None`")  # noqa: E501
        allowed_values = ["critical", "medium", "high", "low"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and tt_range_name not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `tt_range_name` ({0}), must be one of {1}"  # noqa: E501
                .format(tt_range_name, allowed_values)
            )

        self._tt_range_name = tt_range_name

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
        if not isinstance(other, TargetTemptationRange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetTemptationRange):
            return True

        return self.to_dict() != other.to_dict()