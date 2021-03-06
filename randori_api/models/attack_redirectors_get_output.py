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


class AttackRedirectorsGetOutput(object):
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
        'count': 'int',
        'data': 'list[AttackRedirectors]',
        'offset': 'int',
        'total': 'int'
    }

    attribute_map = {
        'count': 'count',
        'data': 'data',
        'offset': 'offset',
        'total': 'total'
    }

    def __init__(self, count=None, data=None, offset=None, total=None, local_vars_configuration=None):  # noqa: E501
        """AttackRedirectorsGetOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._data = None
        self._offset = None
        self._total = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if data is not None:
            self.data = data
        if offset is not None:
            self.offset = offset
        if total is not None:
            self.total = total

    @property
    def count(self):
        """Gets the count of this AttackRedirectorsGetOutput.  # noqa: E501

        number of records in this result  # noqa: E501

        :return: The count of this AttackRedirectorsGetOutput.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this AttackRedirectorsGetOutput.

        number of records in this result  # noqa: E501

        :param count: The count of this AttackRedirectorsGetOutput.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def data(self):
        """Gets the data of this AttackRedirectorsGetOutput.  # noqa: E501

        list of objects  # noqa: E501

        :return: The data of this AttackRedirectorsGetOutput.  # noqa: E501
        :rtype: list[AttackRedirectors]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AttackRedirectorsGetOutput.

        list of objects  # noqa: E501

        :param data: The data of this AttackRedirectorsGetOutput.  # noqa: E501
        :type: list[AttackRedirectors]
        """

        self._data = data

    @property
    def offset(self):
        """Gets the offset of this AttackRedirectorsGetOutput.  # noqa: E501

        starting offset after filtering  # noqa: E501

        :return: The offset of this AttackRedirectorsGetOutput.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this AttackRedirectorsGetOutput.

        starting offset after filtering  # noqa: E501

        :param offset: The offset of this AttackRedirectorsGetOutput.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def total(self):
        """Gets the total of this AttackRedirectorsGetOutput.  # noqa: E501

        number of records total after filtering  # noqa: E501

        :return: The total of this AttackRedirectorsGetOutput.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this AttackRedirectorsGetOutput.

        number of records total after filtering  # noqa: E501

        :param total: The total of this AttackRedirectorsGetOutput.  # noqa: E501
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
        if not isinstance(other, AttackRedirectorsGetOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttackRedirectorsGetOutput):
            return True

        return self.to_dict() != other.to_dict()
