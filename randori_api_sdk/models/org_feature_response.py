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
from pydantic import BaseModel, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrgFeatureResponse(BaseModel):
    """
    OrgFeatureResponse
    """ # noqa: E501
    end_time_utc: Optional[datetime] = None
    feature_uuid: Optional[StrictStr] = None
    name: Optional[Any] = None
    org_uuid: Optional[StrictStr] = None
    start_time_utc: Optional[datetime] = None
    type: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["end_time_utc", "feature_uuid", "name", "org_uuid", "start_time_utc", "type"]

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
        """Create an instance of OrgFeatureResponse from a JSON string"""
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
        # set to None if end_time_utc (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_utc is None and "end_time_utc" in self.model_fields_set:
            _dict['end_time_utc'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if start_time_utc (nullable) is None
        # and model_fields_set contains the field
        if self.start_time_utc is None and "start_time_utc" in self.model_fields_set:
            _dict['start_time_utc'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrgFeatureResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "end_time_utc": obj.get("end_time_utc"),
            "feature_uuid": obj.get("feature_uuid"),
            "name": obj.get("name"),
            "org_uuid": obj.get("org_uuid"),
            "start_time_utc": obj.get("start_time_utc"),
            "type": obj.get("type")
        })
        return _obj

