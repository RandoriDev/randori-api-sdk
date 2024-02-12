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
from pydantic import BaseModel, StrictBool, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CommentResponseSchema(BaseModel):
    """
    CommentResponseSchema
    """ # noqa: E501
    action: Optional[Dict[str, Any]] = None
    comment: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    id: Optional[StrictStr] = None
    is_author: Optional[StrictBool] = None
    is_bulk_applied: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    rel_id: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["action", "comment", "created_at", "id", "is_author", "is_bulk_applied", "name", "rel_id", "status"]

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
        """Create an instance of CommentResponseSchema from a JSON string"""
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
        # set to None if action (nullable) is None
        # and model_fields_set contains the field
        if self.action is None and "action" in self.model_fields_set:
            _dict['action'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CommentResponseSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "comment": obj.get("comment"),
            "created_at": obj.get("created_at"),
            "id": obj.get("id"),
            "is_author": obj.get("is_author"),
            "is_bulk_applied": obj.get("is_bulk_applied"),
            "name": obj.get("name"),
            "rel_id": obj.get("rel_id"),
            "status": obj.get("status")
        })
        return _obj


