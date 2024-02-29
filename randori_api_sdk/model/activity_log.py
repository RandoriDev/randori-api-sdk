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



class ActivityLog(ModelNormal):
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
            'instance__most_recent_instance_id': (str, none_type,),  # noqa: E501
            'matching_entity__id': (str, none_type,),  # noqa: E501
            'org_id': (str, none_type,),  # noqa: E501
            'configuration__description': (str, none_type,),  # noqa: E501
            'configuration__id': (str, none_type,),  # noqa: E501
            'configuration__name': (str, none_type,),  # noqa: E501
            'configuration__version_id': (str, none_type,),  # noqa: E501
            'count__artifacts': (int, none_type,),  # noqa: E501
            'count__entities_updated': (int, none_type,),  # noqa: E501
            'count__relationships_deleted': (int, none_type,),  # noqa: E501
            'instance__perspective': (str, none_type,),  # noqa: E501
            'instance__state': (str, none_type,),  # noqa: E501
            'instance__time_duration': (int, none_type,),  # noqa: E501
            'instance__time_end': (datetime, none_type,),  # noqa: E501
            'instance__time_start': (datetime, none_type,),  # noqa: E501
            'matching_entity__detection': (str, none_type,),  # noqa: E501
            'matching_entity__email': (str, none_type,),  # noqa: E501
            'matching_entity__hostname': (str, none_type,),  # noqa: E501
            'matching_entity__ip': (str, none_type,),  # noqa: E501
            'matching_entity__name': (str, none_type,),  # noqa: E501
            'matching_entity__network': (str, none_type,),  # noqa: E501
            'matching_entity__target': (str, none_type,),  # noqa: E501
            'matching_entity__term': (str, none_type,),  # noqa: E501
            'matching_entity__type': (str, none_type,),  # noqa: E501
            'mitre__mitigations': ([str, none_type], none_type,),  # noqa: E501
            'mitre__tactics': ([str, none_type], none_type,),  # noqa: E501
            'mitre__techniques': ([str, none_type], none_type,),  # noqa: E501
            'objective__attacker_perspective': (str, none_type,),  # noqa: E501
            'objective__description': (str, none_type,),  # noqa: E501
            'objective__implication': (str, none_type,),  # noqa: E501
            'objective__status': (str, none_type,),  # noqa: E501
            'traffic_destination': (str, none_type,),  # noqa: E501
            'traffic_destination_detail': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'traffic_source__ip_name': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'instance__most_recent_instance_id': 'instance__most_recent_instance_id',  # noqa: E501
        'matching_entity__id': 'matching_entity__id',  # noqa: E501
        'org_id': 'org_id',  # noqa: E501
        'configuration__description': 'configuration__description',  # noqa: E501
        'configuration__id': 'configuration__id',  # noqa: E501
        'configuration__name': 'configuration__name',  # noqa: E501
        'configuration__version_id': 'configuration__version_id',  # noqa: E501
        'count__artifacts': 'count__artifacts',  # noqa: E501
        'count__entities_updated': 'count__entities_updated',  # noqa: E501
        'count__relationships_deleted': 'count__relationships_deleted',  # noqa: E501
        'instance__perspective': 'instance__perspective',  # noqa: E501
        'instance__state': 'instance__state',  # noqa: E501
        'instance__time_duration': 'instance__time_duration',  # noqa: E501
        'instance__time_end': 'instance__time_end',  # noqa: E501
        'instance__time_start': 'instance__time_start',  # noqa: E501
        'matching_entity__detection': 'matching_entity__detection',  # noqa: E501
        'matching_entity__email': 'matching_entity__email',  # noqa: E501
        'matching_entity__hostname': 'matching_entity__hostname',  # noqa: E501
        'matching_entity__ip': 'matching_entity__ip',  # noqa: E501
        'matching_entity__name': 'matching_entity__name',  # noqa: E501
        'matching_entity__network': 'matching_entity__network',  # noqa: E501
        'matching_entity__target': 'matching_entity__target',  # noqa: E501
        'matching_entity__term': 'matching_entity__term',  # noqa: E501
        'matching_entity__type': 'matching_entity__type',  # noqa: E501
        'mitre__mitigations': 'mitre__mitigations',  # noqa: E501
        'mitre__tactics': 'mitre__tactics',  # noqa: E501
        'mitre__techniques': 'mitre__techniques',  # noqa: E501
        'objective__attacker_perspective': 'objective__attacker_perspective',  # noqa: E501
        'objective__description': 'objective__description',  # noqa: E501
        'objective__implication': 'objective__implication',  # noqa: E501
        'objective__status': 'objective__status',  # noqa: E501
        'traffic_destination': 'traffic_destination',  # noqa: E501
        'traffic_destination_detail': 'traffic_destination_detail',  # noqa: E501
        'traffic_source__ip_name': 'traffic_source__ip_name',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, instance__most_recent_instance_id, matching_entity__id, org_id, *args, **kwargs):  # noqa: E501
        """ActivityLog - a model defined in OpenAPI

        Args:
            id (str, none_type):
            instance__most_recent_instance_id (str, none_type):
            matching_entity__id (str, none_type):
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
            configuration__description (str, none_type): [optional]  # noqa: E501
            configuration__id (str, none_type): [optional]  # noqa: E501
            configuration__name (str, none_type): [optional]  # noqa: E501
            configuration__version_id (str, none_type): [optional]  # noqa: E501
            count__artifacts (int, none_type): [optional]  # noqa: E501
            count__entities_updated (int, none_type): [optional]  # noqa: E501
            count__relationships_deleted (int, none_type): [optional]  # noqa: E501
            instance__perspective (str, none_type): [optional]  # noqa: E501
            instance__state (str, none_type): [optional]  # noqa: E501
            instance__time_duration (int, none_type): [optional]  # noqa: E501
            instance__time_end (datetime, none_type): [optional]  # noqa: E501
            instance__time_start (datetime, none_type): [optional]  # noqa: E501
            matching_entity__detection (str, none_type): [optional]  # noqa: E501
            matching_entity__email (str, none_type): [optional]  # noqa: E501
            matching_entity__hostname (str, none_type): [optional]  # noqa: E501
            matching_entity__ip (str, none_type): [optional]  # noqa: E501
            matching_entity__name (str, none_type): [optional]  # noqa: E501
            matching_entity__network (str, none_type): [optional]  # noqa: E501
            matching_entity__target (str, none_type): [optional]  # noqa: E501
            matching_entity__term (str, none_type): [optional]  # noqa: E501
            matching_entity__type (str, none_type): [optional]  # noqa: E501
            mitre__mitigations ([str, none_type], none_type): [optional]  # noqa: E501
            mitre__tactics ([str, none_type], none_type): [optional]  # noqa: E501
            mitre__techniques ([str, none_type], none_type): [optional]  # noqa: E501
            objective__attacker_perspective (str, none_type): [optional]  # noqa: E501
            objective__description (str, none_type): [optional]  # noqa: E501
            objective__implication (str, none_type): [optional]  # noqa: E501
            objective__status (str, none_type): [optional]  # noqa: E501
            traffic_destination (str, none_type): [optional]  # noqa: E501
            traffic_destination_detail ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            traffic_source__ip_name (str, none_type): [optional]  # noqa: E501
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
        self.instance__most_recent_instance_id = instance__most_recent_instance_id
        self.matching_entity__id = matching_entity__id
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
    def __init__(self, id, instance__most_recent_instance_id, matching_entity__id, org_id, *args, **kwargs):  # noqa: E501
        """ActivityLog - a model defined in OpenAPI

        Args:
            id (str, none_type):
            instance__most_recent_instance_id (str, none_type):
            matching_entity__id (str, none_type):
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
            configuration__description (str, none_type): [optional]  # noqa: E501
            configuration__id (str, none_type): [optional]  # noqa: E501
            configuration__name (str, none_type): [optional]  # noqa: E501
            configuration__version_id (str, none_type): [optional]  # noqa: E501
            count__artifacts (int, none_type): [optional]  # noqa: E501
            count__entities_updated (int, none_type): [optional]  # noqa: E501
            count__relationships_deleted (int, none_type): [optional]  # noqa: E501
            instance__perspective (str, none_type): [optional]  # noqa: E501
            instance__state (str, none_type): [optional]  # noqa: E501
            instance__time_duration (int, none_type): [optional]  # noqa: E501
            instance__time_end (datetime, none_type): [optional]  # noqa: E501
            instance__time_start (datetime, none_type): [optional]  # noqa: E501
            matching_entity__detection (str, none_type): [optional]  # noqa: E501
            matching_entity__email (str, none_type): [optional]  # noqa: E501
            matching_entity__hostname (str, none_type): [optional]  # noqa: E501
            matching_entity__ip (str, none_type): [optional]  # noqa: E501
            matching_entity__name (str, none_type): [optional]  # noqa: E501
            matching_entity__network (str, none_type): [optional]  # noqa: E501
            matching_entity__target (str, none_type): [optional]  # noqa: E501
            matching_entity__term (str, none_type): [optional]  # noqa: E501
            matching_entity__type (str, none_type): [optional]  # noqa: E501
            mitre__mitigations ([str, none_type], none_type): [optional]  # noqa: E501
            mitre__tactics ([str, none_type], none_type): [optional]  # noqa: E501
            mitre__techniques ([str, none_type], none_type): [optional]  # noqa: E501
            objective__attacker_perspective (str, none_type): [optional]  # noqa: E501
            objective__description (str, none_type): [optional]  # noqa: E501
            objective__implication (str, none_type): [optional]  # noqa: E501
            objective__status (str, none_type): [optional]  # noqa: E501
            traffic_destination (str, none_type): [optional]  # noqa: E501
            traffic_destination_detail ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            traffic_source__ip_name (str, none_type): [optional]  # noqa: E501
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
        self.instance__most_recent_instance_id = instance__most_recent_instance_id
        self.matching_entity__id = matching_entity__id
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
