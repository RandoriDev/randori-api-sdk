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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Tagcounts(BaseModel):
    """
    Tagcounts
    """ # noqa: E501
    all_count: StrictInt
    content: StrictStr
    hostname_count: StrictInt
    id: StrictStr
    ip_count: StrictInt
    is_characteristic_tag: StrictBool
    network_count: StrictInt
    org_id: StrictStr
    poc_count: StrictInt
    service_count: StrictInt
    target_count: StrictInt
    __properties: ClassVar[List[str]] = ["all_count", "content", "hostname_count", "id", "ip_count", "is_characteristic_tag", "network_count", "org_id", "poc_count", "service_count", "target_count"]

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
        """Create an instance of Tagcounts from a JSON string"""
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
        """Create an instance of Tagcounts from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "all_count": obj.get("all_count"),
            "content": obj.get("content"),
            "hostname_count": obj.get("hostname_count"),
            "id": obj.get("id"),
            "ip_count": obj.get("ip_count"),
            "is_characteristic_tag": obj.get("is_characteristic_tag"),
            "network_count": obj.get("network_count"),
            "org_id": obj.get("org_id"),
            "poc_count": obj.get("poc_count"),
            "service_count": obj.get("service_count"),
            "target_count": obj.get("target_count")
        })
        return _obj


