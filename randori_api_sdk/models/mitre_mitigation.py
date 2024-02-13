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
from typing import Any, ClassVar, Dict, List, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MitreMitigation(BaseModel):
    """
    MitreMitigation
    """ # noqa: E501
    created: datetime
    created_by_ref: StrictStr
    description: StrictStr
    external_references: List[Dict[str, Any]]
    id: StrictStr
    modified: datetime
    name: StrictStr
    object_marking_refs: List[StrictStr]
    revoked: StrictBool
    type: StrictStr
    x_mitre_domains: List[StrictStr]
    x_mitre_modified_by_ref: StrictStr
    x_mitre_version: Union[StrictFloat, StrictInt]
    __properties: ClassVar[List[str]] = ["created", "created_by_ref", "description", "external_references", "id", "modified", "name", "object_marking_refs", "revoked", "type", "x_mitre_domains", "x_mitre_modified_by_ref", "x_mitre_version"]

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
        """Create an instance of MitreMitigation from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MitreMitigation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created": obj.get("created"),
            "created_by_ref": obj.get("created_by_ref"),
            "description": obj.get("description"),
            "external_references": obj.get("external_references"),
            "id": obj.get("id"),
            "modified": obj.get("modified"),
            "name": obj.get("name"),
            "object_marking_refs": obj.get("object_marking_refs"),
            "revoked": obj.get("revoked"),
            "type": obj.get("type"),
            "x_mitre_domains": obj.get("x_mitre_domains"),
            "x_mitre_modified_by_ref": obj.get("x_mitre_modified_by_ref"),
            "x_mitre_version": obj.get("x_mitre_version")
        })
        return _obj

