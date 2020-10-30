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


class NetworkPatchInput(object):
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
        'data': 'NetworkPatchIn',
        'operations': 'list[JsonPatchOperation]',
        'q': 'QuerybuilderRuleGroupSchema'
    }

    attribute_map = {
        'data': 'data',
        'operations': 'operations',
        'q': 'q'
    }

    def __init__(self, data=None, operations=None, q=None, local_vars_configuration=None):  # noqa: E501
        """NetworkPatchInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data = None
        self._operations = None
        self._q = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if operations is not None:
            self.operations = operations
        if q is not None:
            self.q = q

    @property
    def data(self):
        """Gets the data of this NetworkPatchInput.  # noqa: E501

        data fields to update on the object  # noqa: E501

        :return: The data of this NetworkPatchInput.  # noqa: E501
        :rtype: NetworkPatchIn
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this NetworkPatchInput.

        data fields to update on the object  # noqa: E501

        :param data: The data of this NetworkPatchInput.  # noqa: E501
        :type: NetworkPatchIn
        """

        self._data = data

    @property
    def operations(self):
        """Gets the operations of this NetworkPatchInput.  # noqa: E501


        :return: The operations of this NetworkPatchInput.  # noqa: E501
        :rtype: list[JsonPatchOperation]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this NetworkPatchInput.


        :param operations: The operations of this NetworkPatchInput.  # noqa: E501
        :type: list[JsonPatchOperation]
        """

        self._operations = operations

    @property
    def q(self):
        """Gets the q of this NetworkPatchInput.  # noqa: E501

        Querybuilder object  # noqa: E501

        :return: The q of this NetworkPatchInput.  # noqa: E501
        :rtype: QuerybuilderRuleGroupSchema
        """
        return self._q

    @q.setter
    def q(self, q):
        """Sets the q of this NetworkPatchInput.

        Querybuilder object  # noqa: E501

        :param q: The q of this NetworkPatchInput.  # noqa: E501
        :type: QuerybuilderRuleGroupSchema
        """

        self._q = q

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
        if not isinstance(other, NetworkPatchInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkPatchInput):
            return True

        return self.to_dict() != other.to_dict()