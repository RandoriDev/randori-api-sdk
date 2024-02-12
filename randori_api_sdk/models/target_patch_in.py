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
from pydantic import BaseModel, StrictStr, field_validator
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TargetPatchIn(BaseModel):
    """
    TargetPatchIn
    """ # noqa: E501
    affiliation_state: Optional[StrictStr] = None
    authorization_state: Optional[StrictStr] = None
    impact_score: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["affiliation_state", "authorization_state", "impact_score", "status"]

    @field_validator('affiliation_state')
    def affiliation_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('None', 'Unaffiliated'):
            raise ValueError("must be one of enum values ('None', 'Unaffiliated')")
        return value

    @field_validator('authorization_state')
    def authorization_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Authorized', 'None'):
            raise ValueError("must be one of enum values ('Authorized', 'None')")
        return value

    @field_validator('impact_score')
    def impact_score_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('None', 'Low', 'Medium', 'High'):
            raise ValueError("must be one of enum values ('None', 'Low', 'Medium', 'High')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('None', 'Needs Investigation', 'Needs Resolution', 'Needs Review', 'Mitigated', 'Accepted'):
            raise ValueError("must be one of enum values ('None', 'Needs Investigation', 'Needs Resolution', 'Needs Review', 'Mitigated', 'Accepted')")
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
        """Create an instance of TargetPatchIn from a JSON string"""
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
        """Create an instance of TargetPatchIn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "affiliation_state": obj.get("affiliation_state"),
            "authorization_state": obj.get("authorization_state"),
            "impact_score": obj.get("impact_score"),
            "status": obj.get("status")
        })
        return _obj


