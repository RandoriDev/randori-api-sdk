# coding: utf-8

"""
    Randori API

    Endpoints accessible using API tokens  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@randori.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from randori_api.configuration import Configuration


class Target(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'affiliation_state': 'str',
        'applicability': 'int',
        'authorization_state': 'str',
        'confidence': 'int',
        'criticality': 'int',
        'deleted': 'bool',
        'description': 'str',
        'enumerability': 'int',
        'first_seen': 'datetime',
        'id': 'str',
        'impact_score': 'str',
        'last_seen': 'datetime',
        'lens_id': 'str',
        'lens_view': 'str',
        'name': 'str',
        'org_id': 'str',
        'perspective': 'str',
        'perspective_name': 'str',
        'post_exploit': 'int',
        'priority_impact_factor': 'float',
        'priority_score': 'float',
        'priority_status_factor': 'float',
        'priority_tags_factor': 'float',
        'private_weakness': 'int',
        'public_weakness': 'int',
        'randori_notes': 'str',
        'reference': 'str',
        'research': 'int',
        'service_id': 'str',
        'status': 'str',
        'tags': 'object',
        'target_temptation': 'int',
        'vendor': 'str',
        'version': 'str'
    }

    attribute_map = {
        'affiliation_state': 'affiliation_state',
        'applicability': 'applicability',
        'authorization_state': 'authorization_state',
        'confidence': 'confidence',
        'criticality': 'criticality',
        'deleted': 'deleted',
        'description': 'description',
        'enumerability': 'enumerability',
        'first_seen': 'first_seen',
        'id': 'id',
        'impact_score': 'impact_score',
        'last_seen': 'last_seen',
        'lens_id': 'lens_id',
        'lens_view': 'lens_view',
        'name': 'name',
        'org_id': 'org_id',
        'perspective': 'perspective',
        'perspective_name': 'perspective_name',
        'post_exploit': 'post_exploit',
        'priority_impact_factor': 'priority_impact_factor',
        'priority_score': 'priority_score',
        'priority_status_factor': 'priority_status_factor',
        'priority_tags_factor': 'priority_tags_factor',
        'private_weakness': 'private_weakness',
        'public_weakness': 'public_weakness',
        'randori_notes': 'randori_notes',
        'reference': 'reference',
        'research': 'research',
        'service_id': 'service_id',
        'status': 'status',
        'tags': 'tags',
        'target_temptation': 'target_temptation',
        'vendor': 'vendor',
        'version': 'version'
    }

    def __init__(self, affiliation_state=None, applicability=None, authorization_state=None, confidence=None, criticality=None, deleted=None, description=None, enumerability=None, first_seen=None, id=None, impact_score=None, last_seen=None, lens_id=None, lens_view=None, name=None, org_id=None, perspective=None, perspective_name=None, post_exploit=None, priority_impact_factor=None, priority_score=None, priority_status_factor=None, priority_tags_factor=None, private_weakness=None, public_weakness=None, randori_notes=None, reference=None, research=None, service_id=None, status=None, tags=None, target_temptation=None, vendor=None, version=None, local_vars_configuration=None):  # noqa: E501
        """Target - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._affiliation_state = None
        self._applicability = None
        self._authorization_state = None
        self._confidence = None
        self._criticality = None
        self._deleted = None
        self._description = None
        self._enumerability = None
        self._first_seen = None
        self._id = None
        self._impact_score = None
        self._last_seen = None
        self._lens_id = None
        self._lens_view = None
        self._name = None
        self._org_id = None
        self._perspective = None
        self._perspective_name = None
        self._post_exploit = None
        self._priority_impact_factor = None
        self._priority_score = None
        self._priority_status_factor = None
        self._priority_tags_factor = None
        self._private_weakness = None
        self._public_weakness = None
        self._randori_notes = None
        self._reference = None
        self._research = None
        self._service_id = None
        self._status = None
        self._tags = None
        self._target_temptation = None
        self._vendor = None
        self._version = None
        self.discriminator = None

        if affiliation_state is not None:
            self.affiliation_state = affiliation_state
        if applicability is not None:
            self.applicability = applicability
        if authorization_state is not None:
            self.authorization_state = authorization_state
        if confidence is not None:
            self.confidence = confidence
        if criticality is not None:
            self.criticality = criticality
        if deleted is not None:
            self.deleted = deleted
        if description is not None:
            self.description = description
        if enumerability is not None:
            self.enumerability = enumerability
        if first_seen is not None:
            self.first_seen = first_seen
        self.id = id
        if impact_score is not None:
            self.impact_score = impact_score
        if last_seen is not None:
            self.last_seen = last_seen
        if lens_id is not None:
            self.lens_id = lens_id
        if lens_view is not None:
            self.lens_view = lens_view
        if name is not None:
            self.name = name
        self.org_id = org_id
        if perspective is not None:
            self.perspective = perspective
        if perspective_name is not None:
            self.perspective_name = perspective_name
        if post_exploit is not None:
            self.post_exploit = post_exploit
        if priority_impact_factor is not None:
            self.priority_impact_factor = priority_impact_factor
        if priority_score is not None:
            self.priority_score = priority_score
        if priority_status_factor is not None:
            self.priority_status_factor = priority_status_factor
        if priority_tags_factor is not None:
            self.priority_tags_factor = priority_tags_factor
        if private_weakness is not None:
            self.private_weakness = private_weakness
        if public_weakness is not None:
            self.public_weakness = public_weakness
        if randori_notes is not None:
            self.randori_notes = randori_notes
        if reference is not None:
            self.reference = reference
        if research is not None:
            self.research = research
        if service_id is not None:
            self.service_id = service_id
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if target_temptation is not None:
            self.target_temptation = target_temptation
        if vendor is not None:
            self.vendor = vendor
        if version is not None:
            self.version = version

    @property
    def affiliation_state(self):
        """Gets the affiliation_state of this Target.  # noqa: E501


        :return: The affiliation_state of this Target.  # noqa: E501
        :rtype: str
        """
        return self._affiliation_state

    @affiliation_state.setter
    def affiliation_state(self, affiliation_state):
        """Sets the affiliation_state of this Target.


        :param affiliation_state: The affiliation_state of this Target.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Affiliated", "Unaffiliated"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and affiliation_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `affiliation_state` ({0}), must be one of {1}"  # noqa: E501
                .format(affiliation_state, allowed_values)
            )

        self._affiliation_state = affiliation_state

    @property
    def applicability(self):
        """Gets the applicability of this Target.  # noqa: E501


        :return: The applicability of this Target.  # noqa: E501
        :rtype: int
        """
        return self._applicability

    @applicability.setter
    def applicability(self, applicability):
        """Sets the applicability of this Target.


        :param applicability: The applicability of this Target.  # noqa: E501
        :type: int
        """

        self._applicability = applicability

    @property
    def authorization_state(self):
        """Gets the authorization_state of this Target.  # noqa: E501


        :return: The authorization_state of this Target.  # noqa: E501
        :rtype: str
        """
        return self._authorization_state

    @authorization_state.setter
    def authorization_state(self, authorization_state):
        """Sets the authorization_state of this Target.


        :param authorization_state: The authorization_state of this Target.  # noqa: E501
        :type: str
        """
        allowed_values = ["Authorized", "Prohibited", "None"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and authorization_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `authorization_state` ({0}), must be one of {1}"  # noqa: E501
                .format(authorization_state, allowed_values)
            )

        self._authorization_state = authorization_state

    @property
    def confidence(self):
        """Gets the confidence of this Target.  # noqa: E501


        :return: The confidence of this Target.  # noqa: E501
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this Target.


        :param confidence: The confidence of this Target.  # noqa: E501
        :type: int
        """

        self._confidence = confidence

    @property
    def criticality(self):
        """Gets the criticality of this Target.  # noqa: E501


        :return: The criticality of this Target.  # noqa: E501
        :rtype: int
        """
        return self._criticality

    @criticality.setter
    def criticality(self, criticality):
        """Sets the criticality of this Target.


        :param criticality: The criticality of this Target.  # noqa: E501
        :type: int
        """

        self._criticality = criticality

    @property
    def deleted(self):
        """Gets the deleted of this Target.  # noqa: E501


        :return: The deleted of this Target.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Target.


        :param deleted: The deleted of this Target.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def description(self):
        """Gets the description of this Target.  # noqa: E501


        :return: The description of this Target.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Target.


        :param description: The description of this Target.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enumerability(self):
        """Gets the enumerability of this Target.  # noqa: E501


        :return: The enumerability of this Target.  # noqa: E501
        :rtype: int
        """
        return self._enumerability

    @enumerability.setter
    def enumerability(self, enumerability):
        """Sets the enumerability of this Target.


        :param enumerability: The enumerability of this Target.  # noqa: E501
        :type: int
        """

        self._enumerability = enumerability

    @property
    def first_seen(self):
        """Gets the first_seen of this Target.  # noqa: E501


        :return: The first_seen of this Target.  # noqa: E501
        :rtype: datetime
        """
        return self._first_seen

    @first_seen.setter
    def first_seen(self, first_seen):
        """Sets the first_seen of this Target.


        :param first_seen: The first_seen of this Target.  # noqa: E501
        :type: datetime
        """

        self._first_seen = first_seen

    @property
    def id(self):
        """Gets the id of this Target.  # noqa: E501


        :return: The id of this Target.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Target.


        :param id: The id of this Target.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def impact_score(self):
        """Gets the impact_score of this Target.  # noqa: E501


        :return: The impact_score of this Target.  # noqa: E501
        :rtype: str
        """
        return self._impact_score

    @impact_score.setter
    def impact_score(self, impact_score):
        """Sets the impact_score of this Target.


        :param impact_score: The impact_score of this Target.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Low", "Medium", "High"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and impact_score not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `impact_score` ({0}), must be one of {1}"  # noqa: E501
                .format(impact_score, allowed_values)
            )

        self._impact_score = impact_score

    @property
    def last_seen(self):
        """Gets the last_seen of this Target.  # noqa: E501


        :return: The last_seen of this Target.  # noqa: E501
        :rtype: datetime
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this Target.


        :param last_seen: The last_seen of this Target.  # noqa: E501
        :type: datetime
        """

        self._last_seen = last_seen

    @property
    def lens_id(self):
        """Gets the lens_id of this Target.  # noqa: E501


        :return: The lens_id of this Target.  # noqa: E501
        :rtype: str
        """
        return self._lens_id

    @lens_id.setter
    def lens_id(self, lens_id):
        """Sets the lens_id of this Target.


        :param lens_id: The lens_id of this Target.  # noqa: E501
        :type: str
        """

        self._lens_id = lens_id

    @property
    def lens_view(self):
        """Gets the lens_view of this Target.  # noqa: E501


        :return: The lens_view of this Target.  # noqa: E501
        :rtype: str
        """
        return self._lens_view

    @lens_view.setter
    def lens_view(self, lens_view):
        """Sets the lens_view of this Target.


        :param lens_view: The lens_view of this Target.  # noqa: E501
        :type: str
        """

        self._lens_view = lens_view

    @property
    def name(self):
        """Gets the name of this Target.  # noqa: E501


        :return: The name of this Target.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Target.


        :param name: The name of this Target.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def org_id(self):
        """Gets the org_id of this Target.  # noqa: E501


        :return: The org_id of this Target.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Target.


        :param org_id: The org_id of this Target.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def perspective(self):
        """Gets the perspective of this Target.  # noqa: E501


        :return: The perspective of this Target.  # noqa: E501
        :rtype: str
        """
        return self._perspective

    @perspective.setter
    def perspective(self, perspective):
        """Sets the perspective of this Target.


        :param perspective: The perspective of this Target.  # noqa: E501
        :type: str
        """

        self._perspective = perspective

    @property
    def perspective_name(self):
        """Gets the perspective_name of this Target.  # noqa: E501


        :return: The perspective_name of this Target.  # noqa: E501
        :rtype: str
        """
        return self._perspective_name

    @perspective_name.setter
    def perspective_name(self, perspective_name):
        """Sets the perspective_name of this Target.


        :param perspective_name: The perspective_name of this Target.  # noqa: E501
        :type: str
        """

        self._perspective_name = perspective_name

    @property
    def post_exploit(self):
        """Gets the post_exploit of this Target.  # noqa: E501


        :return: The post_exploit of this Target.  # noqa: E501
        :rtype: int
        """
        return self._post_exploit

    @post_exploit.setter
    def post_exploit(self, post_exploit):
        """Sets the post_exploit of this Target.


        :param post_exploit: The post_exploit of this Target.  # noqa: E501
        :type: int
        """

        self._post_exploit = post_exploit

    @property
    def priority_impact_factor(self):
        """Gets the priority_impact_factor of this Target.  # noqa: E501


        :return: The priority_impact_factor of this Target.  # noqa: E501
        :rtype: float
        """
        return self._priority_impact_factor

    @priority_impact_factor.setter
    def priority_impact_factor(self, priority_impact_factor):
        """Sets the priority_impact_factor of this Target.


        :param priority_impact_factor: The priority_impact_factor of this Target.  # noqa: E501
        :type: float
        """

        self._priority_impact_factor = priority_impact_factor

    @property
    def priority_score(self):
        """Gets the priority_score of this Target.  # noqa: E501


        :return: The priority_score of this Target.  # noqa: E501
        :rtype: float
        """
        return self._priority_score

    @priority_score.setter
    def priority_score(self, priority_score):
        """Sets the priority_score of this Target.


        :param priority_score: The priority_score of this Target.  # noqa: E501
        :type: float
        """

        self._priority_score = priority_score

    @property
    def priority_status_factor(self):
        """Gets the priority_status_factor of this Target.  # noqa: E501


        :return: The priority_status_factor of this Target.  # noqa: E501
        :rtype: float
        """
        return self._priority_status_factor

    @priority_status_factor.setter
    def priority_status_factor(self, priority_status_factor):
        """Sets the priority_status_factor of this Target.


        :param priority_status_factor: The priority_status_factor of this Target.  # noqa: E501
        :type: float
        """

        self._priority_status_factor = priority_status_factor

    @property
    def priority_tags_factor(self):
        """Gets the priority_tags_factor of this Target.  # noqa: E501


        :return: The priority_tags_factor of this Target.  # noqa: E501
        :rtype: float
        """
        return self._priority_tags_factor

    @priority_tags_factor.setter
    def priority_tags_factor(self, priority_tags_factor):
        """Sets the priority_tags_factor of this Target.


        :param priority_tags_factor: The priority_tags_factor of this Target.  # noqa: E501
        :type: float
        """

        self._priority_tags_factor = priority_tags_factor

    @property
    def private_weakness(self):
        """Gets the private_weakness of this Target.  # noqa: E501


        :return: The private_weakness of this Target.  # noqa: E501
        :rtype: int
        """
        return self._private_weakness

    @private_weakness.setter
    def private_weakness(self, private_weakness):
        """Sets the private_weakness of this Target.


        :param private_weakness: The private_weakness of this Target.  # noqa: E501
        :type: int
        """

        self._private_weakness = private_weakness

    @property
    def public_weakness(self):
        """Gets the public_weakness of this Target.  # noqa: E501


        :return: The public_weakness of this Target.  # noqa: E501
        :rtype: int
        """
        return self._public_weakness

    @public_weakness.setter
    def public_weakness(self, public_weakness):
        """Sets the public_weakness of this Target.


        :param public_weakness: The public_weakness of this Target.  # noqa: E501
        :type: int
        """

        self._public_weakness = public_weakness

    @property
    def randori_notes(self):
        """Gets the randori_notes of this Target.  # noqa: E501


        :return: The randori_notes of this Target.  # noqa: E501
        :rtype: str
        """
        return self._randori_notes

    @randori_notes.setter
    def randori_notes(self, randori_notes):
        """Sets the randori_notes of this Target.


        :param randori_notes: The randori_notes of this Target.  # noqa: E501
        :type: str
        """

        self._randori_notes = randori_notes

    @property
    def reference(self):
        """Gets the reference of this Target.  # noqa: E501


        :return: The reference of this Target.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Target.


        :param reference: The reference of this Target.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def research(self):
        """Gets the research of this Target.  # noqa: E501


        :return: The research of this Target.  # noqa: E501
        :rtype: int
        """
        return self._research

    @research.setter
    def research(self, research):
        """Sets the research of this Target.


        :param research: The research of this Target.  # noqa: E501
        :type: int
        """

        self._research = research

    @property
    def service_id(self):
        """Gets the service_id of this Target.  # noqa: E501


        :return: The service_id of this Target.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this Target.


        :param service_id: The service_id of this Target.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def status(self):
        """Gets the status of this Target.  # noqa: E501


        :return: The status of this Target.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Target.


        :param status: The status of this Target.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Needs Investigation", "Needs Resolution", "Needs Review", "Mitigated", "Accepted"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this Target.  # noqa: E501


        :return: The tags of this Target.  # noqa: E501
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Target.


        :param tags: The tags of this Target.  # noqa: E501
        :type: object
        """

        self._tags = tags

    @property
    def target_temptation(self):
        """Gets the target_temptation of this Target.  # noqa: E501


        :return: The target_temptation of this Target.  # noqa: E501
        :rtype: int
        """
        return self._target_temptation

    @target_temptation.setter
    def target_temptation(self, target_temptation):
        """Sets the target_temptation of this Target.


        :param target_temptation: The target_temptation of this Target.  # noqa: E501
        :type: int
        """

        self._target_temptation = target_temptation

    @property
    def vendor(self):
        """Gets the vendor of this Target.  # noqa: E501


        :return: The vendor of this Target.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this Target.


        :param vendor: The vendor of this Target.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def version(self):
        """Gets the version of this Target.  # noqa: E501


        :return: The version of this Target.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Target.


        :param version: The version of this Target.  # noqa: E501
        :type: str
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Target):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Target):
            return True

        return self.to_dict() != other.to_dict()
