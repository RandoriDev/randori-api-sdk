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


class AttackInterfacesForImplant(object):
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
        'bart_id': 'str',
        'id': 'str',
        'implant_id': 'str',
        'ip_strs': 'object',
        'name': 'str',
        'org_id': 'str'
    }

    attribute_map = {
        'address': 'address',
        'bart_id': 'bart_id',
        'id': 'id',
        'implant_id': 'implant_id',
        'ip_strs': 'ip_strs',
        'name': 'name',
        'org_id': 'org_id'
    }

    def __init__(self, address=None, bart_id=None, id=None, implant_id=None, ip_strs=None, name=None, org_id=None, local_vars_configuration=None):  # noqa: E501
        """AttackInterfacesForImplant - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._bart_id = None
        self._id = None
        self._implant_id = None
        self._ip_strs = None
        self._name = None
        self._org_id = None
        self.discriminator = None

        self.address = address
        self.bart_id = bart_id
        self.id = id
        self.implant_id = implant_id
        self.ip_strs = ip_strs
        self.name = name
        self.org_id = org_id

    @property
    def address(self):
        """Gets the address of this AttackInterfacesForImplant.  # noqa: E501


        :return: The address of this AttackInterfacesForImplant.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AttackInterfacesForImplant.


        :param address: The address of this AttackInterfacesForImplant.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def bart_id(self):
        """Gets the bart_id of this AttackInterfacesForImplant.  # noqa: E501


        :return: The bart_id of this AttackInterfacesForImplant.  # noqa: E501
        :rtype: str
        """
        return self._bart_id

    @bart_id.setter
    def bart_id(self, bart_id):
        """Sets the bart_id of this AttackInterfacesForImplant.


        :param bart_id: The bart_id of this AttackInterfacesForImplant.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and bart_id is None:  # noqa: E501
            raise ValueError("Invalid value for `bart_id`, must not be `None`")  # noqa: E501

        self._bart_id = bart_id

    @property
    def id(self):
        """Gets the id of this AttackInterfacesForImplant.  # noqa: E501


        :return: The id of this AttackInterfacesForImplant.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AttackInterfacesForImplant.


        :param id: The id of this AttackInterfacesForImplant.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def implant_id(self):
        """Gets the implant_id of this AttackInterfacesForImplant.  # noqa: E501


        :return: The implant_id of this AttackInterfacesForImplant.  # noqa: E501
        :rtype: str
        """
        return self._implant_id

    @implant_id.setter
    def implant_id(self, implant_id):
        """Sets the implant_id of this AttackInterfacesForImplant.


        :param implant_id: The implant_id of this AttackInterfacesForImplant.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and implant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `implant_id`, must not be `None`")  # noqa: E501

        self._implant_id = implant_id

    @property
    def ip_strs(self):
        """Gets the ip_strs of this AttackInterfacesForImplant.  # noqa: E501


        :return: The ip_strs of this AttackInterfacesForImplant.  # noqa: E501
        :rtype: object
        """
        return self._ip_strs

    @ip_strs.setter
    def ip_strs(self, ip_strs):
        """Sets the ip_strs of this AttackInterfacesForImplant.


        :param ip_strs: The ip_strs of this AttackInterfacesForImplant.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and ip_strs is None:  # noqa: E501
            raise ValueError("Invalid value for `ip_strs`, must not be `None`")  # noqa: E501

        self._ip_strs = ip_strs

    @property
    def name(self):
        """Gets the name of this AttackInterfacesForImplant.  # noqa: E501


        :return: The name of this AttackInterfacesForImplant.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AttackInterfacesForImplant.


        :param name: The name of this AttackInterfacesForImplant.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def org_id(self):
        """Gets the org_id of this AttackInterfacesForImplant.  # noqa: E501


        :return: The org_id of this AttackInterfacesForImplant.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this AttackInterfacesForImplant.


        :param org_id: The org_id of this AttackInterfacesForImplant.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

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
        if not isinstance(other, AttackInterfacesForImplant):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttackInterfacesForImplant):
            return True

        return self.to_dict() != other.to_dict()
