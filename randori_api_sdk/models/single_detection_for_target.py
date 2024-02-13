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

class SingleDetectionForTarget(BaseModel):
    """
    SingleDetectionForTarget
    """ # noqa: E501
    affiliation_state: Optional[StrictStr] = None
    applicability: Optional[StrictInt] = None
    attack_note: Optional[StrictStr] = None
    authority: Optional[StrictBool] = None
    authority_distance: Optional[StrictInt] = None
    authority_override: Optional[StrictBool] = None
    authorization_state: Optional[StrictStr] = None
    authorizing_policies: Optional[List[StrictStr]] = None
    banners_uuid: Optional[StrictStr] = None
    cert_uuid: Optional[StrictStr] = None
    characteristic_tags: Optional[List[StrictStr]] = None
    characteristics_count: Optional[StrictInt] = None
    confidence: Optional[StrictInt] = None
    cpe: Optional[Dict[str, Any]] = None
    criticality: Optional[StrictInt] = None
    deleted: Optional[StrictBool] = None
    description: Optional[StrictStr] = None
    description_source: Optional[StrictStr] = None
    detection_authorization_state: Optional[StrictStr] = None
    detection_criteria: Optional[Dict[str, Any]] = None
    detection_relevance: Optional[StrictInt] = None
    detection_uuid: Optional[StrictStr] = None
    enumerability: Optional[StrictInt] = None
    exploitability: Optional[StrictInt] = None
    first_seen: Optional[datetime] = None
    headers_uuid: Optional[StrictStr] = None
    hostname: Optional[StrictStr] = None
    hostname_id: Optional[StrictStr] = None
    id: StrictStr
    impact_score: Optional[StrictStr] = None
    ip: Optional[StrictStr] = None
    ip_id: Optional[StrictStr] = None
    ip_str: Optional[StrictStr] = None
    last_seen: Optional[datetime] = None
    lens_id: Optional[StrictStr] = None
    lens_view: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    org_id: StrictStr
    path: Optional[StrictStr] = None
    perspective: Optional[StrictStr] = None
    perspective_name: Optional[StrictStr] = None
    poc_email: Optional[StrictStr] = None
    poc_id: Optional[StrictStr] = None
    port: Optional[StrictInt] = None
    post_exploit: Optional[StrictInt] = None
    priority_impact_factor: Optional[Union[StrictFloat, StrictInt]] = None
    priority_score: Optional[Union[StrictFloat, StrictInt]] = None
    priority_status_factor: Optional[Union[StrictFloat, StrictInt]] = None
    priority_tags_factor: Optional[Union[StrictFloat, StrictInt]] = None
    private_weakness: Optional[StrictInt] = None
    protocol: Optional[StrictStr] = None
    public_weakness: Optional[StrictInt] = None
    randori_notes: Optional[StrictStr] = None
    reference: Optional[StrictStr] = None
    research: Optional[StrictInt] = None
    screenshot_uuid: Optional[StrictStr] = None
    service_id: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    target_confidence: Optional[StrictInt] = None
    target_first_seen: Optional[datetime] = None
    target_id: Optional[StrictStr] = None
    target_last_seen: Optional[datetime] = None
    target_num_authorized_detections: Optional[StrictInt] = None
    target_num_detections: Optional[StrictInt] = None
    target_temptation: Optional[StrictInt] = None
    tech_category: Optional[List[StrictStr]] = None
    temptation_last_modified: Optional[datetime] = None
    thumbnail_uuid: Optional[StrictStr] = None
    user_tags: Optional[List[StrictStr]] = None
    validated_vulnerabilities_detection: Optional[List[StrictStr]] = None
    validated_vulnerabilities_detection_count: Optional[StrictInt] = None
    validated_vulnerabilities_target: Optional[List[StrictStr]] = None
    validated_vulnerabilities_target_count: Optional[StrictInt] = None
    vendor: Optional[StrictStr] = None
    version: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["affiliation_state", "applicability", "attack_note", "authority", "authority_distance", "authority_override", "authorization_state", "authorizing_policies", "banners_uuid", "cert_uuid", "characteristic_tags", "characteristics_count", "confidence", "cpe", "criticality", "deleted", "description", "description_source", "detection_authorization_state", "detection_criteria", "detection_relevance", "detection_uuid", "enumerability", "exploitability", "first_seen", "headers_uuid", "hostname", "hostname_id", "id", "impact_score", "ip", "ip_id", "ip_str", "last_seen", "lens_id", "lens_view", "name", "org_id", "path", "perspective", "perspective_name", "poc_email", "poc_id", "port", "post_exploit", "priority_impact_factor", "priority_score", "priority_status_factor", "priority_tags_factor", "private_weakness", "protocol", "public_weakness", "randori_notes", "reference", "research", "screenshot_uuid", "service_id", "status", "target_confidence", "target_first_seen", "target_id", "target_last_seen", "target_num_authorized_detections", "target_num_detections", "target_temptation", "tech_category", "temptation_last_modified", "thumbnail_uuid", "user_tags", "validated_vulnerabilities_detection", "validated_vulnerabilities_detection_count", "validated_vulnerabilities_target", "validated_vulnerabilities_target_count", "vendor", "version"]

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

    @field_validator('description_source')
    def description_source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('default', 'ai'):
            raise ValueError("must be one of enum values ('default', 'ai')")
        return value

    @field_validator('detection_authorization_state')
    def detection_authorization_state_validate_enum(cls, value):
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

    @field_validator('tech_category')
    def tech_category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('App Servers', 'Applications', 'Databases', 'Firewalls', 'IoT', 'Load Balancers', 'Storage Devices', 'VPNs', 'Web Servers', 'Operating Systems', 'Network Services', 'Plugins', 'Network Equipment'):
                raise ValueError("each list item must be one of ('App Servers', 'Applications', 'Databases', 'Firewalls', 'IoT', 'Load Balancers', 'Storage Devices', 'VPNs', 'Web Servers', 'Operating Systems', 'Network Services', 'Plugins', 'Network Equipment')")
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
        """Create an instance of SingleDetectionForTarget from a JSON string"""
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
        """Create an instance of SingleDetectionForTarget from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "affiliation_state": obj.get("affiliation_state"),
            "applicability": obj.get("applicability"),
            "attack_note": obj.get("attack_note"),
            "authority": obj.get("authority"),
            "authority_distance": obj.get("authority_distance"),
            "authority_override": obj.get("authority_override"),
            "authorization_state": obj.get("authorization_state"),
            "authorizing_policies": obj.get("authorizing_policies"),
            "banners_uuid": obj.get("banners_uuid"),
            "cert_uuid": obj.get("cert_uuid"),
            "characteristic_tags": obj.get("characteristic_tags"),
            "characteristics_count": obj.get("characteristics_count"),
            "confidence": obj.get("confidence"),
            "cpe": obj.get("cpe"),
            "criticality": obj.get("criticality"),
            "deleted": obj.get("deleted"),
            "description": obj.get("description"),
            "description_source": obj.get("description_source"),
            "detection_authorization_state": obj.get("detection_authorization_state"),
            "detection_criteria": obj.get("detection_criteria"),
            "detection_relevance": obj.get("detection_relevance"),
            "detection_uuid": obj.get("detection_uuid"),
            "enumerability": obj.get("enumerability"),
            "exploitability": obj.get("exploitability"),
            "first_seen": obj.get("first_seen"),
            "headers_uuid": obj.get("headers_uuid"),
            "hostname": obj.get("hostname"),
            "hostname_id": obj.get("hostname_id"),
            "id": obj.get("id"),
            "impact_score": obj.get("impact_score"),
            "ip": obj.get("ip"),
            "ip_id": obj.get("ip_id"),
            "ip_str": obj.get("ip_str"),
            "last_seen": obj.get("last_seen"),
            "lens_id": obj.get("lens_id"),
            "lens_view": obj.get("lens_view"),
            "name": obj.get("name"),
            "org_id": obj.get("org_id"),
            "path": obj.get("path"),
            "perspective": obj.get("perspective"),
            "perspective_name": obj.get("perspective_name"),
            "poc_email": obj.get("poc_email"),
            "poc_id": obj.get("poc_id"),
            "port": obj.get("port"),
            "post_exploit": obj.get("post_exploit"),
            "priority_impact_factor": obj.get("priority_impact_factor"),
            "priority_score": obj.get("priority_score"),
            "priority_status_factor": obj.get("priority_status_factor"),
            "priority_tags_factor": obj.get("priority_tags_factor"),
            "private_weakness": obj.get("private_weakness"),
            "protocol": obj.get("protocol"),
            "public_weakness": obj.get("public_weakness"),
            "randori_notes": obj.get("randori_notes"),
            "reference": obj.get("reference"),
            "research": obj.get("research"),
            "screenshot_uuid": obj.get("screenshot_uuid"),
            "service_id": obj.get("service_id"),
            "status": obj.get("status"),
            "target_confidence": obj.get("target_confidence"),
            "target_first_seen": obj.get("target_first_seen"),
            "target_id": obj.get("target_id"),
            "target_last_seen": obj.get("target_last_seen"),
            "target_num_authorized_detections": obj.get("target_num_authorized_detections"),
            "target_num_detections": obj.get("target_num_detections"),
            "target_temptation": obj.get("target_temptation"),
            "tech_category": obj.get("tech_category"),
            "temptation_last_modified": obj.get("temptation_last_modified"),
            "thumbnail_uuid": obj.get("thumbnail_uuid"),
            "user_tags": obj.get("user_tags"),
            "validated_vulnerabilities_detection": obj.get("validated_vulnerabilities_detection"),
            "validated_vulnerabilities_detection_count": obj.get("validated_vulnerabilities_detection_count"),
            "validated_vulnerabilities_target": obj.get("validated_vulnerabilities_target"),
            "validated_vulnerabilities_target_count": obj.get("validated_vulnerabilities_target_count"),
            "vendor": obj.get("vendor"),
            "version": obj.get("version")
        })
        return _obj

