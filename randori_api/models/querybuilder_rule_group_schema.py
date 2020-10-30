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


class QuerybuilderRuleGroupSchema(object):
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
        'condition': 'str',
        'label': 'str',
        'rules': 'list[QuerybuilderGroupMemberSchema]',
        'ui_id': 'str'
    }

    attribute_map = {
        'condition': 'condition',
        'label': 'label',
        'rules': 'rules',
        'ui_id': 'ui_id'
    }

    def __init__(self, condition=None, label=None, rules=None, ui_id=None, local_vars_configuration=None):  # noqa: E501
        """QuerybuilderRuleGroupSchema - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._condition = None
        self._label = None
        self._rules = None
        self._ui_id = None
        self.discriminator = None

        self.condition = condition
        if label is not None:
            self.label = label
        self.rules = rules
        if ui_id is not None:
            self.ui_id = ui_id

    @property
    def condition(self):
        """Gets the condition of this QuerybuilderRuleGroupSchema.  # noqa: E501


        :return: The condition of this QuerybuilderRuleGroupSchema.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this QuerybuilderRuleGroupSchema.


        :param condition: The condition of this QuerybuilderRuleGroupSchema.  # noqa: E501
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
    def label(self):
        """Gets the label of this QuerybuilderRuleGroupSchema.  # noqa: E501


        :return: The label of this QuerybuilderRuleGroupSchema.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this QuerybuilderRuleGroupSchema.


        :param label: The label of this QuerybuilderRuleGroupSchema.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def rules(self):
        """Gets the rules of this QuerybuilderRuleGroupSchema.  # noqa: E501


        :return: The rules of this QuerybuilderRuleGroupSchema.  # noqa: E501
        :rtype: list[QuerybuilderGroupMemberSchema]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this QuerybuilderRuleGroupSchema.


        :param rules: The rules of this QuerybuilderRuleGroupSchema.  # noqa: E501
        :type: list[QuerybuilderGroupMemberSchema]
        """
        if self.local_vars_configuration.client_side_validation and rules is None:  # noqa: E501
            raise ValueError("Invalid value for `rules`, must not be `None`")  # noqa: E501

        self._rules = rules

    @property
    def ui_id(self):
        """Gets the ui_id of this QuerybuilderRuleGroupSchema.  # noqa: E501


        :return: The ui_id of this QuerybuilderRuleGroupSchema.  # noqa: E501
        :rtype: str
        """
        return self._ui_id

    @ui_id.setter
    def ui_id(self, ui_id):
        """Sets the ui_id of this QuerybuilderRuleGroupSchema.


        :param ui_id: The ui_id of this QuerybuilderRuleGroupSchema.  # noqa: E501
        :type: str
        """

        self._ui_id = ui_id

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
        if not isinstance(other, QuerybuilderRuleGroupSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuerybuilderRuleGroupSchema):
            return True

        return self.to_dict() != other.to_dict()
