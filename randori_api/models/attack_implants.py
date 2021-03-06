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


class AttackImplants(object):
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
        'arch': 'str',
        'bart_id': 'str',
        'bits': 'int',
        'created_on': 'datetime',
        'host_ips': 'list[str]',
        'hostnames': 'list[str]',
        'id': 'str',
        'last_checkin': 'datetime',
        'method': 'object',
        'next_checkin': 'datetime',
        'nick': 'str',
        'org_id': 'str',
        'os': 'str',
        'ostype': 'str',
        'osver': 'str',
        'status': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'arch': 'arch',
        'bart_id': 'bart_id',
        'bits': 'bits',
        'created_on': 'created_on',
        'host_ips': 'host_ips',
        'hostnames': 'hostnames',
        'id': 'id',
        'last_checkin': 'last_checkin',
        'method': 'method',
        'next_checkin': 'next_checkin',
        'nick': 'nick',
        'org_id': 'org_id',
        'os': 'os',
        'ostype': 'ostype',
        'osver': 'osver',
        'status': 'status',
        'uid': 'uid'
    }

    def __init__(self, arch=None, bart_id=None, bits=None, created_on=None, host_ips=None, hostnames=None, id=None, last_checkin=None, method=None, next_checkin=None, nick=None, org_id=None, os=None, ostype=None, osver=None, status=None, uid=None, local_vars_configuration=None):  # noqa: E501
        """AttackImplants - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._arch = None
        self._bart_id = None
        self._bits = None
        self._created_on = None
        self._host_ips = None
        self._hostnames = None
        self._id = None
        self._last_checkin = None
        self._method = None
        self._next_checkin = None
        self._nick = None
        self._org_id = None
        self._os = None
        self._ostype = None
        self._osver = None
        self._status = None
        self._uid = None
        self.discriminator = None

        self.arch = arch
        self.bart_id = bart_id
        self.bits = bits
        self.created_on = created_on
        if host_ips is not None:
            self.host_ips = host_ips
        self.hostnames = hostnames
        if id is not None:
            self.id = id
        self.last_checkin = last_checkin
        self.method = method
        self.next_checkin = next_checkin
        self.nick = nick
        self.org_id = org_id
        self.os = os
        self.ostype = ostype
        self.osver = osver
        self.status = status
        self.uid = uid

    @property
    def arch(self):
        """Gets the arch of this AttackImplants.  # noqa: E501


        :return: The arch of this AttackImplants.  # noqa: E501
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this AttackImplants.


        :param arch: The arch of this AttackImplants.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and arch is None:  # noqa: E501
            raise ValueError("Invalid value for `arch`, must not be `None`")  # noqa: E501

        self._arch = arch

    @property
    def bart_id(self):
        """Gets the bart_id of this AttackImplants.  # noqa: E501


        :return: The bart_id of this AttackImplants.  # noqa: E501
        :rtype: str
        """
        return self._bart_id

    @bart_id.setter
    def bart_id(self, bart_id):
        """Sets the bart_id of this AttackImplants.


        :param bart_id: The bart_id of this AttackImplants.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and bart_id is None:  # noqa: E501
            raise ValueError("Invalid value for `bart_id`, must not be `None`")  # noqa: E501

        self._bart_id = bart_id

    @property
    def bits(self):
        """Gets the bits of this AttackImplants.  # noqa: E501


        :return: The bits of this AttackImplants.  # noqa: E501
        :rtype: int
        """
        return self._bits

    @bits.setter
    def bits(self, bits):
        """Sets the bits of this AttackImplants.


        :param bits: The bits of this AttackImplants.  # noqa: E501
        :type: int
        """

        self._bits = bits

    @property
    def created_on(self):
        """Gets the created_on of this AttackImplants.  # noqa: E501


        :return: The created_on of this AttackImplants.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this AttackImplants.


        :param created_on: The created_on of this AttackImplants.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_on is None:  # noqa: E501
            raise ValueError("Invalid value for `created_on`, must not be `None`")  # noqa: E501

        self._created_on = created_on

    @property
    def host_ips(self):
        """Gets the host_ips of this AttackImplants.  # noqa: E501


        :return: The host_ips of this AttackImplants.  # noqa: E501
        :rtype: list[str]
        """
        return self._host_ips

    @host_ips.setter
    def host_ips(self, host_ips):
        """Sets the host_ips of this AttackImplants.


        :param host_ips: The host_ips of this AttackImplants.  # noqa: E501
        :type: list[str]
        """

        self._host_ips = host_ips

    @property
    def hostnames(self):
        """Gets the hostnames of this AttackImplants.  # noqa: E501


        :return: The hostnames of this AttackImplants.  # noqa: E501
        :rtype: list[str]
        """
        return self._hostnames

    @hostnames.setter
    def hostnames(self, hostnames):
        """Sets the hostnames of this AttackImplants.


        :param hostnames: The hostnames of this AttackImplants.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and hostnames is None:  # noqa: E501
            raise ValueError("Invalid value for `hostnames`, must not be `None`")  # noqa: E501

        self._hostnames = hostnames

    @property
    def id(self):
        """Gets the id of this AttackImplants.  # noqa: E501


        :return: The id of this AttackImplants.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AttackImplants.


        :param id: The id of this AttackImplants.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_checkin(self):
        """Gets the last_checkin of this AttackImplants.  # noqa: E501


        :return: The last_checkin of this AttackImplants.  # noqa: E501
        :rtype: datetime
        """
        return self._last_checkin

    @last_checkin.setter
    def last_checkin(self, last_checkin):
        """Sets the last_checkin of this AttackImplants.


        :param last_checkin: The last_checkin of this AttackImplants.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_checkin is None:  # noqa: E501
            raise ValueError("Invalid value for `last_checkin`, must not be `None`")  # noqa: E501

        self._last_checkin = last_checkin

    @property
    def method(self):
        """Gets the method of this AttackImplants.  # noqa: E501


        :return: The method of this AttackImplants.  # noqa: E501
        :rtype: object
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this AttackImplants.


        :param method: The method of this AttackImplants.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and method is None:  # noqa: E501
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def next_checkin(self):
        """Gets the next_checkin of this AttackImplants.  # noqa: E501


        :return: The next_checkin of this AttackImplants.  # noqa: E501
        :rtype: datetime
        """
        return self._next_checkin

    @next_checkin.setter
    def next_checkin(self, next_checkin):
        """Sets the next_checkin of this AttackImplants.


        :param next_checkin: The next_checkin of this AttackImplants.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and next_checkin is None:  # noqa: E501
            raise ValueError("Invalid value for `next_checkin`, must not be `None`")  # noqa: E501

        self._next_checkin = next_checkin

    @property
    def nick(self):
        """Gets the nick of this AttackImplants.  # noqa: E501


        :return: The nick of this AttackImplants.  # noqa: E501
        :rtype: str
        """
        return self._nick

    @nick.setter
    def nick(self, nick):
        """Sets the nick of this AttackImplants.


        :param nick: The nick of this AttackImplants.  # noqa: E501
        :type: str
        """

        self._nick = nick

    @property
    def org_id(self):
        """Gets the org_id of this AttackImplants.  # noqa: E501


        :return: The org_id of this AttackImplants.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this AttackImplants.


        :param org_id: The org_id of this AttackImplants.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def os(self):
        """Gets the os of this AttackImplants.  # noqa: E501


        :return: The os of this AttackImplants.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this AttackImplants.


        :param os: The os of this AttackImplants.  # noqa: E501
        :type: str
        """

        self._os = os

    @property
    def ostype(self):
        """Gets the ostype of this AttackImplants.  # noqa: E501


        :return: The ostype of this AttackImplants.  # noqa: E501
        :rtype: str
        """
        return self._ostype

    @ostype.setter
    def ostype(self, ostype):
        """Sets the ostype of this AttackImplants.


        :param ostype: The ostype of this AttackImplants.  # noqa: E501
        :type: str
        """

        self._ostype = ostype

    @property
    def osver(self):
        """Gets the osver of this AttackImplants.  # noqa: E501


        :return: The osver of this AttackImplants.  # noqa: E501
        :rtype: str
        """
        return self._osver

    @osver.setter
    def osver(self, osver):
        """Sets the osver of this AttackImplants.


        :param osver: The osver of this AttackImplants.  # noqa: E501
        :type: str
        """

        self._osver = osver

    @property
    def status(self):
        """Gets the status of this AttackImplants.  # noqa: E501


        :return: The status of this AttackImplants.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AttackImplants.


        :param status: The status of this AttackImplants.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def uid(self):
        """Gets the uid of this AttackImplants.  # noqa: E501


        :return: The uid of this AttackImplants.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this AttackImplants.


        :param uid: The uid of this AttackImplants.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

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
        if not isinstance(other, AttackImplants):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttackImplants):
            return True

        return self.to_dict() != other.to_dict()