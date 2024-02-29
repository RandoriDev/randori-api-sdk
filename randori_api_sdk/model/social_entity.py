"""
    Randori API SDK

    A python client library for accessing Randori API endpoints using API tokens  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@randori.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from randori_api_sdk.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from randori_api_sdk.exceptions import ApiAttributeError



class SocialEntity(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('affiliation_state',): {
            'NONE': "None",
            'UNAFFILIATED': "Unaffiliated",
        },
        ('authorization_state',): {
            'AUTHORIZED': "Authorized",
            'NONE': "None",
        },
        ('impact_score',): {
            'NONE': "None",
            'LOW': "Low",
            'MEDIUM': "Medium",
            'HIGH': "High",
        },
        ('status',): {
            'NONE': "None",
            'NEEDS_INVESTIGATION': "Needs Investigation",
            'NEEDS_RESOLUTION': "Needs Resolution",
            'NEEDS_REVIEW': "Needs Review",
            'MITIGATED': "Mitigated",
            'ACCEPTED': "Accepted",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'id': (str, none_type,),  # noqa: E501
            'org_id': (str, none_type,),  # noqa: E501
            'address': (str, none_type,),  # noqa: E501
            'affiliation_state': (str,),  # noqa: E501
            'authority': (bool, none_type,),  # noqa: E501
            'authority_distance': (int, none_type,),  # noqa: E501
            'authority_override': (bool, none_type,),  # noqa: E501
            'authorization_state': (str,),  # noqa: E501
            'characteristic_tags': ([str, none_type], none_type,),  # noqa: E501
            'city': (str, none_type,),  # noqa: E501
            'company_name': (str, none_type,),  # noqa: E501
            'confidence': (int, none_type,),  # noqa: E501
            'country': (str, none_type,),  # noqa: E501
            'deleted': (bool, none_type,),  # noqa: E501
            'details': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'domain': (str, none_type,),  # noqa: E501
            'email': (str, none_type,),  # noqa: E501
            'email_type': (str, none_type,),  # noqa: E501
            'first_seen': (datetime, none_type,),  # noqa: E501
            'impact_score': (str,),  # noqa: E501
            'last_seen': (datetime, none_type,),  # noqa: E501
            'lens_id': (str, none_type,),  # noqa: E501
            'lens_view': (str, none_type,),  # noqa: E501
            'only_in_review_targets': (bool, none_type,),  # noqa: E501
            'person_first_name': (str, none_type,),  # noqa: E501
            'person_last_name': (str, none_type,),  # noqa: E501
            'person_middle_name': (str, none_type,),  # noqa: E501
            'person_name': (str, none_type,),  # noqa: E501
            'perspective': (str, none_type,),  # noqa: E501
            'perspective_name': (str, none_type,),  # noqa: E501
            'phone': (str, none_type,),  # noqa: E501
            'postal_code': (str, none_type,),  # noqa: E501
            'priority_impact_factor': (float, none_type,),  # noqa: E501
            'priority_score': (float, none_type,),  # noqa: E501
            'priority_status_factor': (float, none_type,),  # noqa: E501
            'priority_tags_factor': (float, none_type,),  # noqa: E501
            'role': (str, none_type,),  # noqa: E501
            'seniority': (str, none_type,),  # noqa: E501
            'state': (str, none_type,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'sub_role': (str, none_type,),  # noqa: E501
            'target_temptation': (int, none_type,),  # noqa: E501
            'title': (str, none_type,),  # noqa: E501
            'tld': (str, none_type,),  # noqa: E501
            'user_tags': ([str, none_type], none_type,),  # noqa: E501
            'username': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'org_id': 'org_id',  # noqa: E501
        'address': 'address',  # noqa: E501
        'affiliation_state': 'affiliation_state',  # noqa: E501
        'authority': 'authority',  # noqa: E501
        'authority_distance': 'authority_distance',  # noqa: E501
        'authority_override': 'authority_override',  # noqa: E501
        'authorization_state': 'authorization_state',  # noqa: E501
        'characteristic_tags': 'characteristic_tags',  # noqa: E501
        'city': 'city',  # noqa: E501
        'company_name': 'company_name',  # noqa: E501
        'confidence': 'confidence',  # noqa: E501
        'country': 'country',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'details': 'details',  # noqa: E501
        'domain': 'domain',  # noqa: E501
        'email': 'email',  # noqa: E501
        'email_type': 'email_type',  # noqa: E501
        'first_seen': 'first_seen',  # noqa: E501
        'impact_score': 'impact_score',  # noqa: E501
        'last_seen': 'last_seen',  # noqa: E501
        'lens_id': 'lens_id',  # noqa: E501
        'lens_view': 'lens_view',  # noqa: E501
        'only_in_review_targets': 'only_in_review_targets',  # noqa: E501
        'person_first_name': 'person_first_name',  # noqa: E501
        'person_last_name': 'person_last_name',  # noqa: E501
        'person_middle_name': 'person_middle_name',  # noqa: E501
        'person_name': 'person_name',  # noqa: E501
        'perspective': 'perspective',  # noqa: E501
        'perspective_name': 'perspective_name',  # noqa: E501
        'phone': 'phone',  # noqa: E501
        'postal_code': 'postal_code',  # noqa: E501
        'priority_impact_factor': 'priority_impact_factor',  # noqa: E501
        'priority_score': 'priority_score',  # noqa: E501
        'priority_status_factor': 'priority_status_factor',  # noqa: E501
        'priority_tags_factor': 'priority_tags_factor',  # noqa: E501
        'role': 'role',  # noqa: E501
        'seniority': 'seniority',  # noqa: E501
        'state': 'state',  # noqa: E501
        'status': 'status',  # noqa: E501
        'sub_role': 'sub_role',  # noqa: E501
        'target_temptation': 'target_temptation',  # noqa: E501
        'title': 'title',  # noqa: E501
        'tld': 'tld',  # noqa: E501
        'user_tags': 'user_tags',  # noqa: E501
        'username': 'username',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, org_id, *args, **kwargs):  # noqa: E501
        """SocialEntity - a model defined in OpenAPI

        Args:
            id (str, none_type):
            org_id (str, none_type):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            address (str, none_type): [optional]  # noqa: E501
            affiliation_state (str): [optional]  # noqa: E501
            authority (bool, none_type): [optional]  # noqa: E501
            authority_distance (int, none_type): [optional]  # noqa: E501
            authority_override (bool, none_type): [optional]  # noqa: E501
            authorization_state (str): [optional]  # noqa: E501
            characteristic_tags ([str, none_type], none_type): [optional]  # noqa: E501
            city (str, none_type): [optional]  # noqa: E501
            company_name (str, none_type): [optional]  # noqa: E501
            confidence (int, none_type): [optional]  # noqa: E501
            country (str, none_type): [optional]  # noqa: E501
            deleted (bool, none_type): [optional]  # noqa: E501
            details ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            domain (str, none_type): [optional]  # noqa: E501
            email (str, none_type): [optional]  # noqa: E501
            email_type (str, none_type): [optional]  # noqa: E501
            first_seen (datetime, none_type): [optional]  # noqa: E501
            impact_score (str): [optional]  # noqa: E501
            last_seen (datetime, none_type): [optional]  # noqa: E501
            lens_id (str, none_type): [optional]  # noqa: E501
            lens_view (str, none_type): [optional]  # noqa: E501
            only_in_review_targets (bool, none_type): [optional]  # noqa: E501
            person_first_name (str, none_type): [optional]  # noqa: E501
            person_last_name (str, none_type): [optional]  # noqa: E501
            person_middle_name (str, none_type): [optional]  # noqa: E501
            person_name (str, none_type): [optional]  # noqa: E501
            perspective (str, none_type): [optional]  # noqa: E501
            perspective_name (str, none_type): [optional]  # noqa: E501
            phone (str, none_type): [optional]  # noqa: E501
            postal_code (str, none_type): [optional]  # noqa: E501
            priority_impact_factor (float, none_type): [optional]  # noqa: E501
            priority_score (float, none_type): [optional]  # noqa: E501
            priority_status_factor (float, none_type): [optional]  # noqa: E501
            priority_tags_factor (float, none_type): [optional]  # noqa: E501
            role (str, none_type): [optional]  # noqa: E501
            seniority (str, none_type): [optional]  # noqa: E501
            state (str, none_type): [optional]  # noqa: E501
            status (str): [optional]  # noqa: E501
            sub_role (str, none_type): [optional]  # noqa: E501
            target_temptation (int, none_type): [optional]  # noqa: E501
            title (str, none_type): [optional]  # noqa: E501
            tld (str, none_type): [optional]  # noqa: E501
            user_tags ([str, none_type], none_type): [optional]  # noqa: E501
            username (str, none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.org_id = org_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, id, org_id, *args, **kwargs):  # noqa: E501
        """SocialEntity - a model defined in OpenAPI

        Args:
            id (str, none_type):
            org_id (str, none_type):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            address (str, none_type): [optional]  # noqa: E501
            affiliation_state (str): [optional]  # noqa: E501
            authority (bool, none_type): [optional]  # noqa: E501
            authority_distance (int, none_type): [optional]  # noqa: E501
            authority_override (bool, none_type): [optional]  # noqa: E501
            authorization_state (str): [optional]  # noqa: E501
            characteristic_tags ([str, none_type], none_type): [optional]  # noqa: E501
            city (str, none_type): [optional]  # noqa: E501
            company_name (str, none_type): [optional]  # noqa: E501
            confidence (int, none_type): [optional]  # noqa: E501
            country (str, none_type): [optional]  # noqa: E501
            deleted (bool, none_type): [optional]  # noqa: E501
            details ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            domain (str, none_type): [optional]  # noqa: E501
            email (str, none_type): [optional]  # noqa: E501
            email_type (str, none_type): [optional]  # noqa: E501
            first_seen (datetime, none_type): [optional]  # noqa: E501
            impact_score (str): [optional]  # noqa: E501
            last_seen (datetime, none_type): [optional]  # noqa: E501
            lens_id (str, none_type): [optional]  # noqa: E501
            lens_view (str, none_type): [optional]  # noqa: E501
            only_in_review_targets (bool, none_type): [optional]  # noqa: E501
            person_first_name (str, none_type): [optional]  # noqa: E501
            person_last_name (str, none_type): [optional]  # noqa: E501
            person_middle_name (str, none_type): [optional]  # noqa: E501
            person_name (str, none_type): [optional]  # noqa: E501
            perspective (str, none_type): [optional]  # noqa: E501
            perspective_name (str, none_type): [optional]  # noqa: E501
            phone (str, none_type): [optional]  # noqa: E501
            postal_code (str, none_type): [optional]  # noqa: E501
            priority_impact_factor (float, none_type): [optional]  # noqa: E501
            priority_score (float, none_type): [optional]  # noqa: E501
            priority_status_factor (float, none_type): [optional]  # noqa: E501
            priority_tags_factor (float, none_type): [optional]  # noqa: E501
            role (str, none_type): [optional]  # noqa: E501
            seniority (str, none_type): [optional]  # noqa: E501
            state (str, none_type): [optional]  # noqa: E501
            status (str): [optional]  # noqa: E501
            sub_role (str, none_type): [optional]  # noqa: E501
            target_temptation (int, none_type): [optional]  # noqa: E501
            title (str, none_type): [optional]  # noqa: E501
            tld (str, none_type): [optional]  # noqa: E501
            user_tags ([str, none_type], none_type): [optional]  # noqa: E501
            username (str, none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.org_id = org_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
