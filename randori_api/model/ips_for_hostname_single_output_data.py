"""
Copyright © 2022 Randori https://randori.com - All Rights Reserved.
"""

"""
    Randori API

    Endpoints accessible using API tokens  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@randori.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from randori_api.model_utils import (  # noqa: F401
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
from randori_api.exceptions import ApiAttributeError


def lazy_import():
    from randori_api.model.ips_for_hostname import IpsForHostname
    globals()['IpsForHostname'] = IpsForHostname


class IpsForHostnameSingleOutputData(ModelComposed):
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
        lazy_import()
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
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'org_id': (str,),  # noqa: E501
            'affiliation_state': (str,),  # noqa: E501
            'confidence': (int,),  # noqa: E501
            'country': (str, none_type,),  # noqa: E501
            'deleted': (bool,),  # noqa: E501
            'hostname_id': (str,),  # noqa: E501
            'impact_score': (str,),  # noqa: E501
            'ip': (str,),  # noqa: E501
            'ip_id': (str,),  # noqa: E501
            'ip_str': (str,),  # noqa: E501
            'last_seen': (datetime,),  # noqa: E501
            'latitude': (float, none_type,),  # noqa: E501
            'lens_id': (str,),  # noqa: E501
            'lens_view': (str,),  # noqa: E501
            'longitude': (float, none_type,),  # noqa: E501
            'open_port_count': (int,),  # noqa: E501
            'perspective': (str,),  # noqa: E501
            'perspective_name': (str,),  # noqa: E501
            'radius': (float, none_type,),  # noqa: E501
            'service_count': (int, none_type,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'target_count': (int,),  # noqa: E501
            'target_temptation': (int, none_type,),  # noqa: E501
            'top_hostname': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'org_id': 'org_id',  # noqa: E501
        'affiliation_state': 'affiliation_state',  # noqa: E501
        'confidence': 'confidence',  # noqa: E501
        'country': 'country',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'hostname_id': 'hostname_id',  # noqa: E501
        'impact_score': 'impact_score',  # noqa: E501
        'ip': 'ip',  # noqa: E501
        'ip_id': 'ip_id',  # noqa: E501
        'ip_str': 'ip_str',  # noqa: E501
        'last_seen': 'last_seen',  # noqa: E501
        'latitude': 'latitude',  # noqa: E501
        'lens_id': 'lens_id',  # noqa: E501
        'lens_view': 'lens_view',  # noqa: E501
        'longitude': 'longitude',  # noqa: E501
        'open_port_count': 'open_port_count',  # noqa: E501
        'perspective': 'perspective',  # noqa: E501
        'perspective_name': 'perspective_name',  # noqa: E501
        'radius': 'radius',  # noqa: E501
        'service_count': 'service_count',  # noqa: E501
        'status': 'status',  # noqa: E501
        'target_count': 'target_count',  # noqa: E501
        'target_temptation': 'target_temptation',  # noqa: E501
        'top_hostname': 'top_hostname',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """IpsForHostnameSingleOutputData - a model defined in OpenAPI

        Keyword Args:
            id (str):
            org_id (str):
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
            affiliation_state (str): [optional]  # noqa: E501
            confidence (int): [optional]  # noqa: E501
            country (str, none_type): [optional]  # noqa: E501
            deleted (bool): [optional]  # noqa: E501
            hostname_id (str): [optional]  # noqa: E501
            impact_score (str): [optional]  # noqa: E501
            ip (str): [optional]  # noqa: E501
            ip_id (str): [optional]  # noqa: E501
            ip_str (str): [optional]  # noqa: E501
            last_seen (datetime): [optional]  # noqa: E501
            latitude (float, none_type): [optional]  # noqa: E501
            lens_id (str): [optional]  # noqa: E501
            lens_view (str): [optional]  # noqa: E501
            longitude (float, none_type): [optional]  # noqa: E501
            open_port_count (int): [optional]  # noqa: E501
            perspective (str): [optional]  # noqa: E501
            perspective_name (str): [optional]  # noqa: E501
            radius (float, none_type): [optional]  # noqa: E501
            service_count (int, none_type): [optional]  # noqa: E501
            status (str): [optional]  # noqa: E501
            target_count (int): [optional]  # noqa: E501
            target_temptation (int, none_type): [optional]  # noqa: E501
            top_hostname (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
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
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """IpsForHostnameSingleOutputData - a model defined in OpenAPI

        Keyword Args:
            id (str):
            org_id (str):
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
            affiliation_state (str): [optional]  # noqa: E501
            confidence (int): [optional]  # noqa: E501
            country (str, none_type): [optional]  # noqa: E501
            deleted (bool): [optional]  # noqa: E501
            hostname_id (str): [optional]  # noqa: E501
            impact_score (str): [optional]  # noqa: E501
            ip (str): [optional]  # noqa: E501
            ip_id (str): [optional]  # noqa: E501
            ip_str (str): [optional]  # noqa: E501
            last_seen (datetime): [optional]  # noqa: E501
            latitude (float, none_type): [optional]  # noqa: E501
            lens_id (str): [optional]  # noqa: E501
            lens_view (str): [optional]  # noqa: E501
            longitude (float, none_type): [optional]  # noqa: E501
            open_port_count (int): [optional]  # noqa: E501
            perspective (str): [optional]  # noqa: E501
            perspective_name (str): [optional]  # noqa: E501
            radius (float, none_type): [optional]  # noqa: E501
            service_count (int, none_type): [optional]  # noqa: E501
            status (str): [optional]  # noqa: E501
            target_count (int): [optional]  # noqa: E501
            target_temptation (int, none_type): [optional]  # noqa: E501
            top_hostname (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              IpsForHostname,
          ],
          'oneOf': [
          ],
        }
