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


class Tagcounts(object):
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
        'all_count': 'int',
        'content': 'str',
        'first_seen': 'str',
        'hostname_count': 'int',
        'id': 'str',
        'ip_count': 'int',
        'last_seen': 'str',
        'network_count': 'int',
        'org_id': 'str',
        'poc_count': 'int',
        'service_count': 'int',
        'tags': 'object',
        'target_count': 'int'
    }

    attribute_map = {
        'all_count': 'all_count',
        'content': 'content',
        'first_seen': 'first_seen',
        'hostname_count': 'hostname_count',
        'id': 'id',
        'ip_count': 'ip_count',
        'last_seen': 'last_seen',
        'network_count': 'network_count',
        'org_id': 'org_id',
        'poc_count': 'poc_count',
        'service_count': 'service_count',
        'tags': 'tags',
        'target_count': 'target_count'
    }

    def __init__(self, all_count=None, content=None, first_seen=None, hostname_count=None, id=None, ip_count=None, last_seen=None, network_count=None, org_id=None, poc_count=None, service_count=None, tags=None, target_count=None, local_vars_configuration=None):  # noqa: E501
        """Tagcounts - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._all_count = None
        self._content = None
        self._first_seen = None
        self._hostname_count = None
        self._id = None
        self._ip_count = None
        self._last_seen = None
        self._network_count = None
        self._org_id = None
        self._poc_count = None
        self._service_count = None
        self._tags = None
        self._target_count = None
        self.discriminator = None

        self.all_count = all_count
        self.content = content
        if first_seen is not None:
            self.first_seen = first_seen
        self.hostname_count = hostname_count
        self.id = id
        self.ip_count = ip_count
        if last_seen is not None:
            self.last_seen = last_seen
        self.network_count = network_count
        self.org_id = org_id
        self.poc_count = poc_count
        self.service_count = service_count
        if tags is not None:
            self.tags = tags
        self.target_count = target_count

    @property
    def all_count(self):
        """Gets the all_count of this Tagcounts.  # noqa: E501


        :return: The all_count of this Tagcounts.  # noqa: E501
        :rtype: int
        """
        return self._all_count

    @all_count.setter
    def all_count(self, all_count):
        """Sets the all_count of this Tagcounts.


        :param all_count: The all_count of this Tagcounts.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and all_count is None:  # noqa: E501
            raise ValueError("Invalid value for `all_count`, must not be `None`")  # noqa: E501

        self._all_count = all_count

    @property
    def content(self):
        """Gets the content of this Tagcounts.  # noqa: E501


        :return: The content of this Tagcounts.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Tagcounts.


        :param content: The content of this Tagcounts.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def first_seen(self):
        """Gets the first_seen of this Tagcounts.  # noqa: E501


        :return: The first_seen of this Tagcounts.  # noqa: E501
        :rtype: str
        """
        return self._first_seen

    @first_seen.setter
    def first_seen(self, first_seen):
        """Sets the first_seen of this Tagcounts.


        :param first_seen: The first_seen of this Tagcounts.  # noqa: E501
        :type: str
        """

        self._first_seen = first_seen

    @property
    def hostname_count(self):
        """Gets the hostname_count of this Tagcounts.  # noqa: E501


        :return: The hostname_count of this Tagcounts.  # noqa: E501
        :rtype: int
        """
        return self._hostname_count

    @hostname_count.setter
    def hostname_count(self, hostname_count):
        """Sets the hostname_count of this Tagcounts.


        :param hostname_count: The hostname_count of this Tagcounts.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and hostname_count is None:  # noqa: E501
            raise ValueError("Invalid value for `hostname_count`, must not be `None`")  # noqa: E501

        self._hostname_count = hostname_count

    @property
    def id(self):
        """Gets the id of this Tagcounts.  # noqa: E501


        :return: The id of this Tagcounts.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Tagcounts.


        :param id: The id of this Tagcounts.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def ip_count(self):
        """Gets the ip_count of this Tagcounts.  # noqa: E501


        :return: The ip_count of this Tagcounts.  # noqa: E501
        :rtype: int
        """
        return self._ip_count

    @ip_count.setter
    def ip_count(self, ip_count):
        """Sets the ip_count of this Tagcounts.


        :param ip_count: The ip_count of this Tagcounts.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and ip_count is None:  # noqa: E501
            raise ValueError("Invalid value for `ip_count`, must not be `None`")  # noqa: E501

        self._ip_count = ip_count

    @property
    def last_seen(self):
        """Gets the last_seen of this Tagcounts.  # noqa: E501


        :return: The last_seen of this Tagcounts.  # noqa: E501
        :rtype: str
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this Tagcounts.


        :param last_seen: The last_seen of this Tagcounts.  # noqa: E501
        :type: str
        """

        self._last_seen = last_seen

    @property
    def network_count(self):
        """Gets the network_count of this Tagcounts.  # noqa: E501


        :return: The network_count of this Tagcounts.  # noqa: E501
        :rtype: int
        """
        return self._network_count

    @network_count.setter
    def network_count(self, network_count):
        """Sets the network_count of this Tagcounts.


        :param network_count: The network_count of this Tagcounts.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and network_count is None:  # noqa: E501
            raise ValueError("Invalid value for `network_count`, must not be `None`")  # noqa: E501

        self._network_count = network_count

    @property
    def org_id(self):
        """Gets the org_id of this Tagcounts.  # noqa: E501


        :return: The org_id of this Tagcounts.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Tagcounts.


        :param org_id: The org_id of this Tagcounts.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def poc_count(self):
        """Gets the poc_count of this Tagcounts.  # noqa: E501


        :return: The poc_count of this Tagcounts.  # noqa: E501
        :rtype: int
        """
        return self._poc_count

    @poc_count.setter
    def poc_count(self, poc_count):
        """Sets the poc_count of this Tagcounts.


        :param poc_count: The poc_count of this Tagcounts.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and poc_count is None:  # noqa: E501
            raise ValueError("Invalid value for `poc_count`, must not be `None`")  # noqa: E501

        self._poc_count = poc_count

    @property
    def service_count(self):
        """Gets the service_count of this Tagcounts.  # noqa: E501


        :return: The service_count of this Tagcounts.  # noqa: E501
        :rtype: int
        """
        return self._service_count

    @service_count.setter
    def service_count(self, service_count):
        """Sets the service_count of this Tagcounts.


        :param service_count: The service_count of this Tagcounts.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and service_count is None:  # noqa: E501
            raise ValueError("Invalid value for `service_count`, must not be `None`")  # noqa: E501

        self._service_count = service_count

    @property
    def tags(self):
        """Gets the tags of this Tagcounts.  # noqa: E501


        :return: The tags of this Tagcounts.  # noqa: E501
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Tagcounts.


        :param tags: The tags of this Tagcounts.  # noqa: E501
        :type: object
        """

        self._tags = tags

    @property
    def target_count(self):
        """Gets the target_count of this Tagcounts.  # noqa: E501


        :return: The target_count of this Tagcounts.  # noqa: E501
        :rtype: int
        """
        return self._target_count

    @target_count.setter
    def target_count(self, target_count):
        """Sets the target_count of this Tagcounts.


        :param target_count: The target_count of this Tagcounts.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and target_count is None:  # noqa: E501
            raise ValueError("Invalid value for `target_count`, must not be `None`")  # noqa: E501

        self._target_count = target_count

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
        if not isinstance(other, Tagcounts):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Tagcounts):
            return True

        return self.to_dict() != other.to_dict()