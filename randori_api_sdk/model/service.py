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



class Service(ModelNormal):
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
        ('description_source',): {
            'DEFAULT': "default",
            'AI': "ai",
        },
        ('tech_category',): {
            'None': None,
            'APP_SERVERS': "App Servers",
            'APPLICATIONS': "Applications",
            'DATABASES': "Databases",
            'FIREWALLS': "Firewalls",
            'IOT': "IoT",
            'LOAD_BALANCERS': "Load Balancers",
            'STORAGE_DEVICES': "Storage Devices",
            'VPNS': "VPNs",
            'WEB_SERVERS': "Web Servers",
            'OPERATING_SYSTEMS': "Operating Systems",
            'NETWORK_SERVICES': "Network Services",
            'PLUGINS': "Plugins",
            'NETWORK_EQUIPMENT': "Network Equipment",
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
            'applicability': (int, none_type,),  # noqa: E501
            'attack_note': (str, none_type,),  # noqa: E501
            'confidence': (int, none_type,),  # noqa: E501
            'cpe': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'criticality': (int, none_type,),  # noqa: E501
            'deleted': (bool, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'description_source': (str,),  # noqa: E501
            'enumerability': (int, none_type,),  # noqa: E501
            'exploitability': (int, none_type,),  # noqa: E501
            'first_seen': (datetime, none_type,),  # noqa: E501
            'instance_count': (float, none_type,),  # noqa: E501
            'ip_count': (float, none_type,),  # noqa: E501
            'last_seen': (datetime, none_type,),  # noqa: E501
            'lens_id': (str, none_type,),  # noqa: E501
            'lens_view': (str, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'perspective': (str, none_type,),  # noqa: E501
            'perspective_name': (str, none_type,),  # noqa: E501
            'post_exploit': (int, none_type,),  # noqa: E501
            'private_weakness': (int, none_type,),  # noqa: E501
            'public_weakness': (int, none_type,),  # noqa: E501
            'randori_notes': (str, none_type,),  # noqa: E501
            'reference': (str, none_type,),  # noqa: E501
            'research': (int, none_type,),  # noqa: E501
            'service_id': (str, none_type,),  # noqa: E501
            'target_temptation': (int, none_type,),  # noqa: E501
            'tech_category': ([str], none_type,),  # noqa: E501
            'temptation_last_modified': (datetime, none_type,),  # noqa: E501
            'vendor': (str, none_type,),  # noqa: E501
            'version': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'org_id': 'org_id',  # noqa: E501
        'applicability': 'applicability',  # noqa: E501
        'attack_note': 'attack_note',  # noqa: E501
        'confidence': 'confidence',  # noqa: E501
        'cpe': 'cpe',  # noqa: E501
        'criticality': 'criticality',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'description': 'description',  # noqa: E501
        'description_source': 'description_source',  # noqa: E501
        'enumerability': 'enumerability',  # noqa: E501
        'exploitability': 'exploitability',  # noqa: E501
        'first_seen': 'first_seen',  # noqa: E501
        'instance_count': 'instance_count',  # noqa: E501
        'ip_count': 'ip_count',  # noqa: E501
        'last_seen': 'last_seen',  # noqa: E501
        'lens_id': 'lens_id',  # noqa: E501
        'lens_view': 'lens_view',  # noqa: E501
        'name': 'name',  # noqa: E501
        'perspective': 'perspective',  # noqa: E501
        'perspective_name': 'perspective_name',  # noqa: E501
        'post_exploit': 'post_exploit',  # noqa: E501
        'private_weakness': 'private_weakness',  # noqa: E501
        'public_weakness': 'public_weakness',  # noqa: E501
        'randori_notes': 'randori_notes',  # noqa: E501
        'reference': 'reference',  # noqa: E501
        'research': 'research',  # noqa: E501
        'service_id': 'service_id',  # noqa: E501
        'target_temptation': 'target_temptation',  # noqa: E501
        'tech_category': 'tech_category',  # noqa: E501
        'temptation_last_modified': 'temptation_last_modified',  # noqa: E501
        'vendor': 'vendor',  # noqa: E501
        'version': 'version',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, org_id, *args, **kwargs):  # noqa: E501
        """Service - a model defined in OpenAPI

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
            applicability (int, none_type): [optional]  # noqa: E501
            attack_note (str, none_type): [optional]  # noqa: E501
            confidence (int, none_type): [optional]  # noqa: E501
            cpe ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            criticality (int, none_type): [optional]  # noqa: E501
            deleted (bool, none_type): [optional]  # noqa: E501
            description (str, none_type): [optional]  # noqa: E501
            description_source (str): [optional]  # noqa: E501
            enumerability (int, none_type): [optional]  # noqa: E501
            exploitability (int, none_type): [optional]  # noqa: E501
            first_seen (datetime, none_type): [optional]  # noqa: E501
            instance_count (float, none_type): [optional]  # noqa: E501
            ip_count (float, none_type): [optional]  # noqa: E501
            last_seen (datetime, none_type): [optional]  # noqa: E501
            lens_id (str, none_type): [optional]  # noqa: E501
            lens_view (str, none_type): [optional]  # noqa: E501
            name (str, none_type): [optional]  # noqa: E501
            perspective (str, none_type): [optional]  # noqa: E501
            perspective_name (str, none_type): [optional]  # noqa: E501
            post_exploit (int, none_type): [optional]  # noqa: E501
            private_weakness (int, none_type): [optional]  # noqa: E501
            public_weakness (int, none_type): [optional]  # noqa: E501
            randori_notes (str, none_type): [optional]  # noqa: E501
            reference (str, none_type): [optional]  # noqa: E501
            research (int, none_type): [optional]  # noqa: E501
            service_id (str, none_type): [optional]  # noqa: E501
            target_temptation (int, none_type): [optional]  # noqa: E501
            tech_category ([str], none_type): [optional]  # noqa: E501
            temptation_last_modified (datetime, none_type): [optional]  # noqa: E501
            vendor (str, none_type): [optional]  # noqa: E501
            version (str, none_type): [optional]  # noqa: E501
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
        """Service - a model defined in OpenAPI

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
            applicability (int, none_type): [optional]  # noqa: E501
            attack_note (str, none_type): [optional]  # noqa: E501
            confidence (int, none_type): [optional]  # noqa: E501
            cpe ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            criticality (int, none_type): [optional]  # noqa: E501
            deleted (bool, none_type): [optional]  # noqa: E501
            description (str, none_type): [optional]  # noqa: E501
            description_source (str): [optional]  # noqa: E501
            enumerability (int, none_type): [optional]  # noqa: E501
            exploitability (int, none_type): [optional]  # noqa: E501
            first_seen (datetime, none_type): [optional]  # noqa: E501
            instance_count (float, none_type): [optional]  # noqa: E501
            ip_count (float, none_type): [optional]  # noqa: E501
            last_seen (datetime, none_type): [optional]  # noqa: E501
            lens_id (str, none_type): [optional]  # noqa: E501
            lens_view (str, none_type): [optional]  # noqa: E501
            name (str, none_type): [optional]  # noqa: E501
            perspective (str, none_type): [optional]  # noqa: E501
            perspective_name (str, none_type): [optional]  # noqa: E501
            post_exploit (int, none_type): [optional]  # noqa: E501
            private_weakness (int, none_type): [optional]  # noqa: E501
            public_weakness (int, none_type): [optional]  # noqa: E501
            randori_notes (str, none_type): [optional]  # noqa: E501
            reference (str, none_type): [optional]  # noqa: E501
            research (int, none_type): [optional]  # noqa: E501
            service_id (str, none_type): [optional]  # noqa: E501
            target_temptation (int, none_type): [optional]  # noqa: E501
            tech_category ([str], none_type): [optional]  # noqa: E501
            temptation_last_modified (datetime, none_type): [optional]  # noqa: E501
            vendor (str, none_type): [optional]  # noqa: E501
            version (str, none_type): [optional]  # noqa: E501
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
