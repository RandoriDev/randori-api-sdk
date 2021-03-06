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


class QuerybuilderGroupMemberSchema3(object):
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
        'field': 'str',
        'id': 'str',
        'input': 'str',
        'label': 'str',
        'operator': 'str',
        'type': 'str',
        'ui_id': 'str',
        'value': 'str',
        'condition': 'str',
        'rules': 'list[QuerybuilderGroupMemberSchema4]'
    }

    attribute_map = {
        'field': 'field',
        'id': 'id',
        'input': 'input',
        'label': 'label',
        'operator': 'operator',
        'type': 'type',
        'ui_id': 'ui_id',
        'value': 'value',
        'condition': 'condition',
        'rules': 'rules'
    }

    def __init__(self, field=None, id=None, input=None, label=None, operator=None, type=None, ui_id=None, value=None, condition=None, rules=None, local_vars_configuration=None):  # noqa: E501
        """QuerybuilderGroupMemberSchema3 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field = None
        self._id = None
        self._input = None
        self._label = None
        self._operator = None
        self._type = None
        self._ui_id = None
        self._value = None
        self._condition = None
        self._rules = None
        self.discriminator = None

        self.field = field
        if id is not None:
            self.id = id
        if input is not None:
            self.input = input
        if label is not None:
            self.label = label
        self.operator = operator
        if type is not None:
            self.type = type
        if ui_id is not None:
            self.ui_id = ui_id
        self.value = value
        self.condition = condition
        self.rules = rules

    @property
    def field(self):
        """Gets the field of this QuerybuilderGroupMemberSchema3.  # noqa: E501


        :return: The field of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this QuerybuilderGroupMemberSchema3.


        :param field: The field of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and field is None:  # noqa: E501
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    @property
    def id(self):
        """Gets the id of this QuerybuilderGroupMemberSchema3.  # noqa: E501


        :return: The id of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuerybuilderGroupMemberSchema3.


        :param id: The id of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def input(self):
        """Gets the input of this QuerybuilderGroupMemberSchema3.  # noqa: E501


        :return: The input of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this QuerybuilderGroupMemberSchema3.


        :param input: The input of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :type: str
        """

        self._input = input

    @property
    def label(self):
        """Gets the label of this QuerybuilderGroupMemberSchema3.  # noqa: E501


        :return: The label of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this QuerybuilderGroupMemberSchema3.


        :param label: The label of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def operator(self):
        """Gets the operator of this QuerybuilderGroupMemberSchema3.  # noqa: E501


        :return: The operator of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this QuerybuilderGroupMemberSchema3.


        :param operator: The operator of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501
        allowed_values = ["not_in", "less", "not_contains_element", "less_or_equal_utc_seconds_ago", "is_null", "not_ends_with", "between", "has_key", "icontains", "not_contains", "is_empty", "matches", "not_begins_with", "in", "not_icontains", "greater", "less_utc_seconds_ago", "is_not_null", "greater_or_equal_utc_seconds_ago", "contains", "begins_with", "contains_element", "not_has_key", "greater_or_equal", "less_or_equal", "ends_with", "not_equal", "is_not_empty", "contained_by", "matched_by", "not_contained_by", "greater_utc_seconds_ago", "equal"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and operator not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `operator` ({0}), must be one of {1}"  # noqa: E501
                .format(operator, allowed_values)
            )

        self._operator = operator

    @property
    def type(self):
        """Gets the type of this QuerybuilderGroupMemberSchema3.  # noqa: E501


        :return: The type of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuerybuilderGroupMemberSchema3.


        :param type: The type of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def ui_id(self):
        """Gets the ui_id of this QuerybuilderGroupMemberSchema3.  # noqa: E501


        :return: The ui_id of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :rtype: str
        """
        return self._ui_id

    @ui_id.setter
    def ui_id(self, ui_id):
        """Sets the ui_id of this QuerybuilderGroupMemberSchema3.


        :param ui_id: The ui_id of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :type: str
        """

        self._ui_id = ui_id

    @property
    def value(self):
        """Gets the value of this QuerybuilderGroupMemberSchema3.  # noqa: E501


        :return: The value of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this QuerybuilderGroupMemberSchema3.


        :param value: The value of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def condition(self):
        """Gets the condition of this QuerybuilderGroupMemberSchema3.  # noqa: E501


        :return: The condition of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this QuerybuilderGroupMemberSchema3.


        :param condition: The condition of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and condition is None:  # noqa: E501
            raise ValueError("Invalid value for `condition`, must not be `None`")  # noqa: E501
        allowed_values = ["AND", "OR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and condition not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"  # noqa: E501
                .format(condition, allowed_values)
            )

        self._condition = condition

    @property
    def rules(self):
        """Gets the rules of this QuerybuilderGroupMemberSchema3.  # noqa: E501


        :return: The rules of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :rtype: list[QuerybuilderGroupMemberSchema4]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this QuerybuilderGroupMemberSchema3.


        :param rules: The rules of this QuerybuilderGroupMemberSchema3.  # noqa: E501
        :type: list[QuerybuilderGroupMemberSchema4]
        """
        if self.local_vars_configuration.client_side_validation and rules is None:  # noqa: E501
            raise ValueError("Invalid value for `rules`, must not be `None`")  # noqa: E501

        self._rules = rules

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
        if not isinstance(other, QuerybuilderGroupMemberSchema3):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuerybuilderGroupMemberSchema3):
            return True

        return self.to_dict() != other.to_dict()
