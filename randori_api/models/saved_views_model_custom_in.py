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


class SavedViewsModelCustomIn(object):
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
        'description': 'str',
        'entity_type': 'str',
        'filter_data': 'object',
        'name': 'str',
        'sort_data': 'object'
    }

    attribute_map = {
        'description': 'description',
        'entity_type': 'entity_type',
        'filter_data': 'filter_data',
        'name': 'name',
        'sort_data': 'sort_data'
    }

    def __init__(self, description=None, entity_type=None, filter_data=None, name=None, sort_data=None, local_vars_configuration=None):  # noqa: E501
        """SavedViewsModelCustomIn - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._entity_type = None
        self._filter_data = None
        self._name = None
        self._sort_data = None
        self.discriminator = None

        self.description = description
        self.entity_type = entity_type
        self.filter_data = filter_data
        self.name = name
        self.sort_data = sort_data

    @property
    def description(self):
        """Gets the description of this SavedViewsModelCustomIn.  # noqa: E501


        :return: The description of this SavedViewsModelCustomIn.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SavedViewsModelCustomIn.


        :param description: The description of this SavedViewsModelCustomIn.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def entity_type(self):
        """Gets the entity_type of this SavedViewsModelCustomIn.  # noqa: E501


        :return: The entity_type of this SavedViewsModelCustomIn.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this SavedViewsModelCustomIn.


        :param entity_type: The entity_type of this SavedViewsModelCustomIn.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and entity_type is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501
        allowed_values = ["target", "hostname", "service", "ip", "network", "social", "runbook", "implant", "redirector"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and entity_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def filter_data(self):
        """Gets the filter_data of this SavedViewsModelCustomIn.  # noqa: E501


        :return: The filter_data of this SavedViewsModelCustomIn.  # noqa: E501
        :rtype: object
        """
        return self._filter_data

    @filter_data.setter
    def filter_data(self, filter_data):
        """Sets the filter_data of this SavedViewsModelCustomIn.


        :param filter_data: The filter_data of this SavedViewsModelCustomIn.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and filter_data is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_data`, must not be `None`")  # noqa: E501

        self._filter_data = filter_data

    @property
    def name(self):
        """Gets the name of this SavedViewsModelCustomIn.  # noqa: E501


        :return: The name of this SavedViewsModelCustomIn.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SavedViewsModelCustomIn.


        :param name: The name of this SavedViewsModelCustomIn.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sort_data(self):
        """Gets the sort_data of this SavedViewsModelCustomIn.  # noqa: E501


        :return: The sort_data of this SavedViewsModelCustomIn.  # noqa: E501
        :rtype: object
        """
        return self._sort_data

    @sort_data.setter
    def sort_data(self, sort_data):
        """Sets the sort_data of this SavedViewsModelCustomIn.


        :param sort_data: The sort_data of this SavedViewsModelCustomIn.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and sort_data is None:  # noqa: E501
            raise ValueError("Invalid value for `sort_data`, must not be `None`")  # noqa: E501

        self._sort_data = sort_data

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
        if not isinstance(other, SavedViewsModelCustomIn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SavedViewsModelCustomIn):
            return True

        return self.to_dict() != other.to_dict()
