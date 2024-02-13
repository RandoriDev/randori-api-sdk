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
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SocialEntity(BaseModel):
    """
    SocialEntity
    """ # noqa: E501
    address: Optional[StrictStr] = None
    affiliation_state: Optional[StrictStr] = None
    authority: Optional[StrictBool] = None
    authority_distance: Optional[StrictInt] = None
    authority_override: Optional[StrictBool] = None
    authorization_state: Optional[StrictStr] = None
    characteristic_tags: Optional[List[StrictStr]] = None
    city: Optional[StrictStr] = None
    company_name: Optional[StrictStr] = None
    confidence: Optional[StrictInt] = None
    country: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    details: Optional[Dict[str, Any]] = None
    domain: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    email_type: Optional[StrictStr] = None
    first_seen: Optional[datetime] = None
    id: StrictStr
    impact_score: Optional[StrictStr] = None
    last_seen: Optional[datetime] = None
    lens_id: Optional[StrictStr] = None
    lens_view: Optional[StrictStr] = None
    only_in_review_targets: Optional[StrictBool] = None
    org_id: StrictStr
    person_first_name: Optional[StrictStr] = None
    person_last_name: Optional[StrictStr] = None
    person_middle_name: Optional[StrictStr] = None
    person_name: Optional[StrictStr] = None
    perspective: Optional[StrictStr] = None
    perspective_name: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = None
    priority_impact_factor: Optional[Union[StrictFloat, StrictInt]] = None
    priority_score: Optional[Union[StrictFloat, StrictInt]] = None
    priority_status_factor: Optional[Union[StrictFloat, StrictInt]] = None
    priority_tags_factor: Optional[Union[StrictFloat, StrictInt]] = None
    role: Optional[StrictStr] = None
    seniority: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    sub_role: Optional[StrictStr] = None
    target_temptation: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    tld: Optional[StrictStr] = None
    user_tags: Optional[List[StrictStr]] = None
    username: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["address", "affiliation_state", "authority", "authority_distance", "authority_override", "authorization_state", "characteristic_tags", "city", "company_name", "confidence", "country", "deleted", "details", "domain", "email", "email_type", "first_seen", "id", "impact_score", "last_seen", "lens_id", "lens_view", "only_in_review_targets", "org_id", "person_first_name", "person_last_name", "person_middle_name", "person_name", "perspective", "perspective_name", "phone", "postal_code", "priority_impact_factor", "priority_score", "priority_status_factor", "priority_tags_factor", "role", "seniority", "state", "status", "sub_role", "target_temptation", "title", "tld", "user_tags", "username"]

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
        """Create an instance of SocialEntity from a JSON string"""
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
        """Create an instance of SocialEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "affiliation_state": obj.get("affiliation_state"),
            "authority": obj.get("authority"),
            "authority_distance": obj.get("authority_distance"),
            "authority_override": obj.get("authority_override"),
            "authorization_state": obj.get("authorization_state"),
            "characteristic_tags": obj.get("characteristic_tags"),
            "city": obj.get("city"),
            "company_name": obj.get("company_name"),
            "confidence": obj.get("confidence"),
            "country": obj.get("country"),
            "deleted": obj.get("deleted"),
            "details": obj.get("details"),
            "domain": obj.get("domain"),
            "email": obj.get("email"),
            "email_type": obj.get("email_type"),
            "first_seen": obj.get("first_seen"),
            "id": obj.get("id"),
            "impact_score": obj.get("impact_score"),
            "last_seen": obj.get("last_seen"),
            "lens_id": obj.get("lens_id"),
            "lens_view": obj.get("lens_view"),
            "only_in_review_targets": obj.get("only_in_review_targets"),
            "org_id": obj.get("org_id"),
            "person_first_name": obj.get("person_first_name"),
            "person_last_name": obj.get("person_last_name"),
            "person_middle_name": obj.get("person_middle_name"),
            "person_name": obj.get("person_name"),
            "perspective": obj.get("perspective"),
            "perspective_name": obj.get("perspective_name"),
            "phone": obj.get("phone"),
            "postal_code": obj.get("postal_code"),
            "priority_impact_factor": obj.get("priority_impact_factor"),
            "priority_score": obj.get("priority_score"),
            "priority_status_factor": obj.get("priority_status_factor"),
            "priority_tags_factor": obj.get("priority_tags_factor"),
            "role": obj.get("role"),
            "seniority": obj.get("seniority"),
            "state": obj.get("state"),
            "status": obj.get("status"),
            "sub_role": obj.get("sub_role"),
            "target_temptation": obj.get("target_temptation"),
            "title": obj.get("title"),
            "tld": obj.get("tld"),
            "user_tags": obj.get("user_tags"),
            "username": obj.get("username")
        })
        return _obj

