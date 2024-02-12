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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AuthorizationPolicy(BaseModel):
    """
    AuthorizationPolicy
    """ # noqa: E501
    actions: Optional[List[Dict[str, Any]]] = None
    created_at: datetime
    edited_at: datetime
    entity_types: List[StrictStr]
    expires_at: Optional[datetime] = None
    filter_data: Dict[str, Any]
    id: Optional[StrictStr] = None
    is_active: StrictBool
    is_deleted: Optional[StrictBool] = None
    is_dirty: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    notes: Optional[StrictStr] = None
    org_id: StrictStr
    version: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["actions", "created_at", "edited_at", "entity_types", "expires_at", "filter_data", "id", "is_active", "is_deleted", "is_dirty", "name", "notes", "org_id", "version"]

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
        """Create an instance of AuthorizationPolicy from a JSON string"""
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
        # set to None if expires_at (nullable) is None
        # and model_fields_set contains the field
        if self.expires_at is None and "expires_at" in self.model_fields_set:
            _dict['expires_at'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AuthorizationPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actions": obj.get("actions"),
            "created_at": obj.get("created_at"),
            "edited_at": obj.get("edited_at"),
            "entity_types": obj.get("entity_types"),
            "expires_at": obj.get("expires_at"),
            "filter_data": obj.get("filter_data"),
            "id": obj.get("id"),
            "is_active": obj.get("is_active"),
            "is_deleted": obj.get("is_deleted"),
            "is_dirty": obj.get("is_dirty"),
            "name": obj.get("name"),
            "notes": obj.get("notes"),
            "org_id": obj.get("org_id"),
            "version": obj.get("version")
        })
        return _obj


