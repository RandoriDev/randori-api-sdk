# coding: utf-8

"""
    Randori API

    Endpoints accessible using API tokens

    The version of the OpenAPI document: 1.0
    Contact: support@randori.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SavedViewsModelCustomIn(BaseModel):
    """
    SavedViewsModelCustomIn
    """ # noqa: E501
    description: Optional[StrictStr] = None
    entity_type: StrictStr
    filter_data: Dict[str, Any]
    is_favorite: Optional[StrictBool] = None
    is_global: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    sort_data: Dict[str, Any]
    __properties: ClassVar[List[str]] = ["description", "entity_type", "filter_data", "is_favorite", "is_global", "name", "sort_data"]

    @field_validator('entity_type')
    def entity_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('target', 'hostname', 'service', 'ip', 'network', 'social', 'runbook', 'implant', 'redirector', 'topLevelDetection', 'activity_instance', 'activity_configuration'):
            raise ValueError("must be one of enum values ('target', 'hostname', 'service', 'ip', 'network', 'social', 'runbook', 'implant', 'redirector', 'topLevelDetection', 'activity_instance', 'activity_configuration')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SavedViewsModelCustomIn from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if is_favorite (nullable) is None
        # and model_fields_set contains the field
        if self.is_favorite is None and "is_favorite" in self.model_fields_set:
            _dict['is_favorite'] = None

        # set to None if is_global (nullable) is None
        # and model_fields_set contains the field
        if self.is_global is None and "is_global" in self.model_fields_set:
            _dict['is_global'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SavedViewsModelCustomIn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "entity_type": obj.get("entity_type"),
            "filter_data": obj.get("filter_data"),
            "is_favorite": obj.get("is_favorite"),
            "is_global": obj.get("is_global"),
            "name": obj.get("name"),
            "sort_data": obj.get("sort_data")
        })
        return _obj


