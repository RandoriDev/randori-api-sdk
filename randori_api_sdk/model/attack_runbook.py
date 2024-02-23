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



class AttackRunbook(ModelNormal):
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
        ('comment',): {
            'max_length': 280,
            'min_length': 1,
        },
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
            'dst_search': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'org_id': (str,),  # noqa: E501
            'runbook_id': (str,),  # noqa: E501
            'src_search': (str,),  # noqa: E501
            'start_time': (datetime,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'technique_ids': ([str],),  # noqa: E501
            'uid': (str,),  # noqa: E501
            'comment': (str,),  # noqa: E501
            'deleted': (bool, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'dst_email': ([str], none_type,),  # noqa: E501
            'dst_host': ([str], none_type,),  # noqa: E501
            'dst_ip': ([str],),  # noqa: E501
            'dst_mac': ([str], none_type,),  # noqa: E501
            'dst_misc': ([str], none_type,),  # noqa: E501
            'dst_network': ([str],),  # noqa: E501
            'dst_path': ([str], none_type,),  # noqa: E501
            'dst_port': ([int], none_type,),  # noqa: E501
            'end_time': (datetime, none_type,),  # noqa: E501
            'guidance': (str, none_type,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'implant_ids': ([str], none_type,),  # noqa: E501
            'implant_nick': (str, none_type,),  # noqa: E501
            'implant_src_host': ([str], none_type,),  # noqa: E501
            'implant_src_ip': ([str],),  # noqa: E501
            'instance_label': (str, none_type,),  # noqa: E501
            'objective': (str, none_type,),  # noqa: E501
            'perspective_metadata': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}], none_type,),  # noqa: E501
            'randori_notes': (str, none_type,),  # noqa: E501
            'results': (str, none_type,),  # noqa: E501
            'src_email': ([str], none_type,),  # noqa: E501
            'src_host': ([str], none_type,),  # noqa: E501
            'src_ip': ([str],),  # noqa: E501
            'src_mac': ([str], none_type,),  # noqa: E501
            'src_misc': ([str], none_type,),  # noqa: E501
            'trigger': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'dst_search': 'dst_search',  # noqa: E501
        'name': 'name',  # noqa: E501
        'org_id': 'org_id',  # noqa: E501
        'runbook_id': 'runbook_id',  # noqa: E501
        'src_search': 'src_search',  # noqa: E501
        'start_time': 'start_time',  # noqa: E501
        'status': 'status',  # noqa: E501
        'technique_ids': 'technique_ids',  # noqa: E501
        'uid': 'uid',  # noqa: E501
        'comment': 'comment',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'description': 'description',  # noqa: E501
        'dst_email': 'dst_email',  # noqa: E501
        'dst_host': 'dst_host',  # noqa: E501
        'dst_ip': 'dst_ip',  # noqa: E501
        'dst_mac': 'dst_mac',  # noqa: E501
        'dst_misc': 'dst_misc',  # noqa: E501
        'dst_network': 'dst_network',  # noqa: E501
        'dst_path': 'dst_path',  # noqa: E501
        'dst_port': 'dst_port',  # noqa: E501
        'end_time': 'end_time',  # noqa: E501
        'guidance': 'guidance',  # noqa: E501
        'id': 'id',  # noqa: E501
        'implant_ids': 'implant_ids',  # noqa: E501
        'implant_nick': 'implant_nick',  # noqa: E501
        'implant_src_host': 'implant_src_host',  # noqa: E501
        'implant_src_ip': 'implant_src_ip',  # noqa: E501
        'instance_label': 'instance_label',  # noqa: E501
        'objective': 'objective',  # noqa: E501
        'perspective_metadata': 'perspective_metadata',  # noqa: E501
        'randori_notes': 'randori_notes',  # noqa: E501
        'results': 'results',  # noqa: E501
        'src_email': 'src_email',  # noqa: E501
        'src_host': 'src_host',  # noqa: E501
        'src_ip': 'src_ip',  # noqa: E501
        'src_mac': 'src_mac',  # noqa: E501
        'src_misc': 'src_misc',  # noqa: E501
        'trigger': 'trigger',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, dst_search, name, org_id, runbook_id, src_search, start_time, status, technique_ids, uid, *args, **kwargs):  # noqa: E501
        """AttackRunbook - a model defined in OpenAPI

        Args:
            dst_search (str):
            name (str):
            org_id (str):
            runbook_id (str):
            src_search (str):
            start_time (datetime):
            status (str):
            technique_ids ([str]):
            uid (str):

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
            comment (str): [optional]  # noqa: E501
            deleted (bool, none_type): [optional]  # noqa: E501
            description (str, none_type): [optional]  # noqa: E501
            dst_email ([str], none_type): [optional]  # noqa: E501
            dst_host ([str], none_type): [optional]  # noqa: E501
            dst_ip ([str]): [optional]  # noqa: E501
            dst_mac ([str], none_type): [optional]  # noqa: E501
            dst_misc ([str], none_type): [optional]  # noqa: E501
            dst_network ([str]): [optional]  # noqa: E501
            dst_path ([str], none_type): [optional]  # noqa: E501
            dst_port ([int], none_type): [optional]  # noqa: E501
            end_time (datetime, none_type): [optional]  # noqa: E501
            guidance (str, none_type): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            implant_ids ([str], none_type): [optional]  # noqa: E501
            implant_nick (str, none_type): [optional]  # noqa: E501
            implant_src_host ([str], none_type): [optional]  # noqa: E501
            implant_src_ip ([str]): [optional]  # noqa: E501
            instance_label (str, none_type): [optional]  # noqa: E501
            objective (str, none_type): [optional]  # noqa: E501
            perspective_metadata ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}], none_type): [optional]  # noqa: E501
            randori_notes (str, none_type): [optional]  # noqa: E501
            results (str, none_type): [optional]  # noqa: E501
            src_email ([str], none_type): [optional]  # noqa: E501
            src_host ([str], none_type): [optional]  # noqa: E501
            src_ip ([str]): [optional]  # noqa: E501
            src_mac ([str], none_type): [optional]  # noqa: E501
            src_misc ([str], none_type): [optional]  # noqa: E501
            trigger ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}], none_type): [optional]  # noqa: E501
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

        self.dst_search = dst_search
        self.name = name
        self.org_id = org_id
        self.runbook_id = runbook_id
        self.src_search = src_search
        self.start_time = start_time
        self.status = status
        self.technique_ids = technique_ids
        self.uid = uid
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
    def __init__(self, dst_search, name, org_id, runbook_id, src_search, start_time, status, technique_ids, uid, *args, **kwargs):  # noqa: E501
        """AttackRunbook - a model defined in OpenAPI

        Args:
            dst_search (str):
            name (str):
            org_id (str):
            runbook_id (str):
            src_search (str):
            start_time (datetime):
            status (str):
            technique_ids ([str]):
            uid (str):

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
            comment (str): [optional]  # noqa: E501
            deleted (bool, none_type): [optional]  # noqa: E501
            description (str, none_type): [optional]  # noqa: E501
            dst_email ([str], none_type): [optional]  # noqa: E501
            dst_host ([str], none_type): [optional]  # noqa: E501
            dst_ip ([str]): [optional]  # noqa: E501
            dst_mac ([str], none_type): [optional]  # noqa: E501
            dst_misc ([str], none_type): [optional]  # noqa: E501
            dst_network ([str]): [optional]  # noqa: E501
            dst_path ([str], none_type): [optional]  # noqa: E501
            dst_port ([int], none_type): [optional]  # noqa: E501
            end_time (datetime, none_type): [optional]  # noqa: E501
            guidance (str, none_type): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            implant_ids ([str], none_type): [optional]  # noqa: E501
            implant_nick (str, none_type): [optional]  # noqa: E501
            implant_src_host ([str], none_type): [optional]  # noqa: E501
            implant_src_ip ([str]): [optional]  # noqa: E501
            instance_label (str, none_type): [optional]  # noqa: E501
            objective (str, none_type): [optional]  # noqa: E501
            perspective_metadata ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}], none_type): [optional]  # noqa: E501
            randori_notes (str, none_type): [optional]  # noqa: E501
            results (str, none_type): [optional]  # noqa: E501
            src_email ([str], none_type): [optional]  # noqa: E501
            src_host ([str], none_type): [optional]  # noqa: E501
            src_ip ([str]): [optional]  # noqa: E501
            src_mac ([str], none_type): [optional]  # noqa: E501
            src_misc ([str], none_type): [optional]  # noqa: E501
            trigger ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}], none_type): [optional]  # noqa: E501
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

        self.dst_search = dst_search
        self.name = name
        self.org_id = org_id
        self.runbook_id = runbook_id
        self.src_search = src_search
        self.start_time = start_time
        self.status = status
        self.technique_ids = technique_ids
        self.uid = uid
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
