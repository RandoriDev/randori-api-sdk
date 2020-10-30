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


class StatusGroupOuterResult(object):
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
        'status_counts': 'list[StatusGroupInnerResult]',
        'total': 'int'
    }

    attribute_map = {
        'status_counts': 'status_counts',
        'total': 'total'
    }

    def __init__(self, status_counts=None, total=None, local_vars_configuration=None):  # noqa: E501
        """StatusGroupOuterResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status_counts = None
        self._total = None
        self.discriminator = None

        if status_counts is not None:
            self.status_counts = status_counts
        if total is not None:
            self.total = total

    @property
    def status_counts(self):
        """Gets the status_counts of this StatusGroupOuterResult.  # noqa: E501


        :return: The status_counts of this StatusGroupOuterResult.  # noqa: E501
        :rtype: list[StatusGroupInnerResult]
        """
        return self._status_counts

    @status_counts.setter
    def status_counts(self, status_counts):
        """Sets the status_counts of this StatusGroupOuterResult.


        :param status_counts: The status_counts of this StatusGroupOuterResult.  # noqa: E501
        :type: list[StatusGroupInnerResult]
        """

        self._status_counts = status_counts

    @property
    def total(self):
        """Gets the total of this StatusGroupOuterResult.  # noqa: E501


        :return: The total of this StatusGroupOuterResult.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this StatusGroupOuterResult.


        :param total: The total of this StatusGroupOuterResult.  # noqa: E501
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
        if not isinstance(other, StatusGroupOuterResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatusGroupOuterResult):
            return True

        return self.to_dict() != other.to_dict()
