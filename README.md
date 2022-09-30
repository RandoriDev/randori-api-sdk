# Randori-API
Endpoints accessible using API tokens

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.5.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.randori.com/contact/](https://www.randori.com/contact/)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/RandoriDev/randori-api-sdk
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import randori_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import randori_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import randori_api
from pprint import pprint
from randori_api.api import default_api
from randori_api.model.action_metadata_get_output import ActionMetadataGetOutput
from randori_api.model.action_metadata_single_output import ActionMetadataSingleOutput
from randori_api.model.all_detections_for_target_get_output import AllDetectionsForTargetGetOutput
from randori_api.model.artifactsrc import Artifactsrc
from randori_api.model.artifactsrc_many import ArtifactsrcMany
from randori_api.model.attack_checkins_for_implant_get_output import AttackCheckinsForImplantGetOutput
from randori_api.model.attack_implants_get_output import AttackImplantsGetOutput
from randori_api.model.attack_implants_single_output import AttackImplantsSingleOutput
from randori_api.model.attack_interfaces_for_implant_get_output import AttackInterfacesForImplantGetOutput
from randori_api.model.attack_redirectors_get_output import AttackRedirectorsGetOutput
from randori_api.model.attack_runbook_get_output import AttackRunbookGetOutput
from randori_api.model.attack_statistics_get_output import AttackStatisticsGetOutput
from randori_api.model.attack_user_action_descriptions_get_output import AttackUserActionDescriptionsGetOutput
from randori_api.model.attack_user_action_descriptions_patch_single_input import AttackUserActionDescriptionsPatchSingleInput
from randori_api.model.attack_user_action_descriptions_post_input import AttackUserActionDescriptionsPostInput
from randori_api.model.attack_user_action_descriptions_post_output import AttackUserActionDescriptionsPostOutput
from randori_api.model.attack_user_action_descriptions_single_output import AttackUserActionDescriptionsSingleOutput
from randori_api.model.attack_user_autoapprove_get_output import AttackUserAutoapproveGetOutput
from randori_api.model.attack_user_autoapprove_patch_single_input import AttackUserAutoapprovePatchSingleInput
from randori_api.model.attack_user_autoapprove_post_input import AttackUserAutoapprovePostInput
from randori_api.model.attack_user_autoapprove_post_output import AttackUserAutoapprovePostOutput
from randori_api.model.attack_user_autoapprove_single_output import AttackUserAutoapproveSingleOutput
from randori_api.model.attack_user_runbook_descriptions_get_output import AttackUserRunbookDescriptionsGetOutput
from randori_api.model.attack_user_runbook_descriptions_patch_single_input import AttackUserRunbookDescriptionsPatchSingleInput
from randori_api.model.attack_user_runbook_descriptions_post_input import AttackUserRunbookDescriptionsPostInput
from randori_api.model.attack_user_runbook_descriptions_post_output import AttackUserRunbookDescriptionsPostOutput
from randori_api.model.attack_user_runbook_descriptions_single_output import AttackUserRunbookDescriptionsSingleOutput
from randori_api.model.comment_creation_schema import CommentCreationSchema
from randori_api.model.comment_response_collection_schema import CommentResponseCollectionSchema
from randori_api.model.comment_response_schema import CommentResponseSchema
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.external_comment_creation_schema import ExternalCommentCreationSchema
from randori_api.model.hostname_get_output import HostnameGetOutput
from randori_api.model.hostname_patch_input import HostnamePatchInput
from randori_api.model.hostname_patch_output import HostnamePatchOutput
from randori_api.model.hostname_single_output import HostnameSingleOutput
from randori_api.model.hostnames_for_ip_get_output import HostnamesForIpGetOutput
from randori_api.model.hostnames_for_ip_single_output import HostnamesForIpSingleOutput
from randori_api.model.impact_score_entity_req import ImpactScoreEntityReq
from randori_api.model.impact_score_group_outer_result import ImpactScoreGroupOuterResult
from randori_api.model.ip_get_output import IpGetOutput
from randori_api.model.ip_patch_input import IpPatchInput
from randori_api.model.ip_patch_output import IpPatchOutput
from randori_api.model.ip_single_output import IpSingleOutput
from randori_api.model.ips_for_hostname_get_output import IpsForHostnameGetOutput
from randori_api.model.ips_for_hostname_single_output import IpsForHostnameSingleOutput
from randori_api.model.ips_for_network_get_output import IpsForNetworkGetOutput
from randori_api.model.ips_for_network_single_output import IpsForNetworkSingleOutput
from randori_api.model.ips_for_service_get_output import IpsForServiceGetOutput
from randori_api.model.ips_for_service_single_output import IpsForServiceSingleOutput
from randori_api.model.network_get_output import NetworkGetOutput
from randori_api.model.network_patch_input import NetworkPatchInput
from randori_api.model.network_patch_output import NetworkPatchOutput
from randori_api.model.network_single_output import NetworkSingleOutput
from randori_api.model.paths_output_schema import PathsOutputSchema
from randori_api.model.peer_get_output import PeerGetOutput
from randori_api.model.peer_map_get_output import PeerMapGetOutput
from randori_api.model.peer_map_patch_single_input import PeerMapPatchSingleInput
from randori_api.model.peer_map_post_input import PeerMapPostInput
from randori_api.model.peer_map_post_output import PeerMapPostOutput
from randori_api.model.peer_map_single_output import PeerMapSingleOutput
from randori_api.model.peer_post_input import PeerPostInput
from randori_api.model.peer_post_output import PeerPostOutput
from randori_api.model.peer_single_output import PeerSingleOutput
from randori_api.model.policy_get_output import PolicyGetOutput
from randori_api.model.policy_patch_single_input import PolicyPatchSingleInput
from randori_api.model.policy_post_input import PolicyPostInput
from randori_api.model.policy_post_output import PolicyPostOutput
from randori_api.model.policy_single_input import PolicySingleInput
from randori_api.model.policy_single_output import PolicySingleOutput
from randori_api.model.ports_for_ip_get_output import PortsForIpGetOutput
from randori_api.model.ports_for_ip_single_output import PortsForIpSingleOutput
from randori_api.model.prime_get_output import PrimeGetOutput
from randori_api.model.priority_entity_req import PriorityEntityReq
from randori_api.model.priority_group_outer_result import PriorityGroupOuterResult
from randori_api.model.recon_worker_node_ips import ReconWorkerNodeIps
from randori_api.model.report_get_output import ReportGetOutput
from randori_api.model.report_single_output import ReportSingleOutput
from randori_api.model.saved_views_get_output import SavedViewsGetOutput
from randori_api.model.saved_views_patch_single_input import SavedViewsPatchSingleInput
from randori_api.model.saved_views_post_input import SavedViewsPostInput
from randori_api.model.saved_views_post_output import SavedViewsPostOutput
from randori_api.model.saved_views_single_input import SavedViewsSingleInput
from randori_api.model.saved_views_single_output import SavedViewsSingleOutput
from randori_api.model.service_get_output import ServiceGetOutput
from randori_api.model.service_single_output import ServiceSingleOutput
from randori_api.model.single_detection_for_target_get_output import SingleDetectionForTargetGetOutput
from randori_api.model.social_entity_get_output import SocialEntityGetOutput
from randori_api.model.social_entity_patch_input import SocialEntityPatchInput
from randori_api.model.social_entity_patch_output import SocialEntityPatchOutput
from randori_api.model.statistics_get_output import StatisticsGetOutput
from randori_api.model.status_entity_req import StatusEntityReq
from randori_api.model.status_group_outer_result import StatusGroupOuterResult
from randori_api.model.tagcounts_get_output import TagcountsGetOutput
from randori_api.model.tagcounts_single_output import TagcountsSingleOutput
from randori_api.model.target_get_output import TargetGetOutput
from randori_api.model.target_patch_input import TargetPatchInput
from randori_api.model.target_patch_output import TargetPatchOutput
from randori_api.model.target_single_output import TargetSingleOutput
from randori_api.model.target_temptation_entity_req import TargetTemptationEntityReq
from randori_api.model.target_temptation_group_outer_result import TargetTemptationGroupOuterResult
from randori_api.model.user_ap_action_instances_get_output import UserApActionInstancesGetOutput
from randori_api.model.user_ap_action_instances_patch_single_input import UserApActionInstancesPatchSingleInput
from randori_api.model.user_ap_action_instances_post_input import UserApActionInstancesPostInput
from randori_api.model.user_ap_action_instances_post_output import UserApActionInstancesPostOutput
from randori_api.model.user_ap_action_instances_single_output import UserApActionInstancesSingleOutput
from randori_api.model.user_artifact_query import UserArtifactQuery
from randori_api.model.user_tag_name_list import UserTagNameList
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    try:
        api_instance.add_affiliation()
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->add_affiliation: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://app.randori.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**add_affiliation**](docs/DefaultApi.md#add_affiliation) | **POST** /artifactstore/api/v1/add_affiliation | 
*DefaultApi* | [**add_affiliation_file**](docs/DefaultApi.md#add_affiliation_file) | **POST** /artifactstore/api/v1/add_affiliation_file | 
*DefaultApi* | [**artifact**](docs/DefaultApi.md#artifact) | **GET** /artifactstore/api/v1/artifact/{artifact_uuid} | 
*DefaultApi* | [**artifact_raw**](docs/DefaultApi.md#artifact_raw) | **GET** /artifactstore/api/v1/artifact-raw/{shasum} | 
*DefaultApi* | [**comment**](docs/DefaultApi.md#comment) | **GET** /recon/api/v1/entity/{entity_id}/comment | 
*DefaultApi* | [**comment_0**](docs/DefaultApi.md#comment_0) | **POST** /recon/api/v1/entity/{entity_id}/comment | 
*DefaultApi* | [**delete_single_attack_user_action_descriptions**](docs/DefaultApi.md#delete_single_attack_user_action_descriptions) | **DELETE** /attack/api/v1/user/attack-action-descriptions/{id} | 
*DefaultApi* | [**delete_single_attack_user_runbook_descriptions**](docs/DefaultApi.md#delete_single_attack_user_runbook_descriptions) | **DELETE** /attack/api/v1/user/attack-runbook-descriptions/{id} | 
*DefaultApi* | [**delete_single_policy**](docs/DefaultApi.md#delete_single_policy) | **DELETE** /recon/api/v1/policy/{id} | 
*DefaultApi* | [**delete_single_saved_views**](docs/DefaultApi.md#delete_single_saved_views) | **DELETE** /recon/api/v1/saved-views/{id} | 
*DefaultApi* | [**get_action_metadata**](docs/DefaultApi.md#get_action_metadata) | **GET** /attack/api/v1/user/actions | 
*DefaultApi* | [**get_all_detections_for_target**](docs/DefaultApi.md#get_all_detections_for_target) | **GET** /recon/api/v1/all-detections-for-target | 
*DefaultApi* | [**get_attack_checkins_for_implant**](docs/DefaultApi.md#get_attack_checkins_for_implant) | **GET** /attack/api/v1/user/checkins-for-implant | 
*DefaultApi* | [**get_attack_implants**](docs/DefaultApi.md#get_attack_implants) | **GET** /attack/api/v1/user/implants | 
*DefaultApi* | [**get_attack_interfaces_for_implant**](docs/DefaultApi.md#get_attack_interfaces_for_implant) | **GET** /attack/api/v1/user/interfaces-for-implant | 
*DefaultApi* | [**get_attack_redirectors**](docs/DefaultApi.md#get_attack_redirectors) | **GET** /attack/api/v1/user/redirectors | 
*DefaultApi* | [**get_attack_runbook**](docs/DefaultApi.md#get_attack_runbook) | **GET** /attack/api/v1/user/runbooks | 
*DefaultApi* | [**get_attack_statistics**](docs/DefaultApi.md#get_attack_statistics) | **GET** /attack/api/v1/user/statistics | 
*DefaultApi* | [**get_attack_user_action_descriptions**](docs/DefaultApi.md#get_attack_user_action_descriptions) | **GET** /attack/api/v1/user/attack-action-descriptions | 
*DefaultApi* | [**get_attack_user_autoapprove**](docs/DefaultApi.md#get_attack_user_autoapprove) | **GET** /attack/api/v1/user/attack-autoapprove | 
*DefaultApi* | [**get_attack_user_runbook_descriptions**](docs/DefaultApi.md#get_attack_user_runbook_descriptions) | **GET** /attack/api/v1/user/attack-runbook-descriptions | 
*DefaultApi* | [**get_hostname**](docs/DefaultApi.md#get_hostname) | **GET** /recon/api/v1/hostname | 
*DefaultApi* | [**get_hostnames_for_ip**](docs/DefaultApi.md#get_hostnames_for_ip) | **GET** /recon/api/v1/hostnames-for-ip | 
*DefaultApi* | [**get_ip**](docs/DefaultApi.md#get_ip) | **GET** /recon/api/v1/ip | 
*DefaultApi* | [**get_ips_for_hostname**](docs/DefaultApi.md#get_ips_for_hostname) | **GET** /recon/api/v1/ips-for-hostname | 
*DefaultApi* | [**get_ips_for_network**](docs/DefaultApi.md#get_ips_for_network) | **GET** /recon/api/v1/ips-for-network | 
*DefaultApi* | [**get_ips_for_service**](docs/DefaultApi.md#get_ips_for_service) | **GET** /recon/api/v1/ips-for-service | 
*DefaultApi* | [**get_network**](docs/DefaultApi.md#get_network) | **GET** /recon/api/v1/network | 
*DefaultApi* | [**get_peer**](docs/DefaultApi.md#get_peer) | **GET** /recon/api/v1/peer | 
*DefaultApi* | [**get_peer_map**](docs/DefaultApi.md#get_peer_map) | **GET** /recon/api/v1/peer-map | 
*DefaultApi* | [**get_policy**](docs/DefaultApi.md#get_policy) | **GET** /recon/api/v1/policy | 
*DefaultApi* | [**get_ports_for_ip**](docs/DefaultApi.md#get_ports_for_ip) | **GET** /recon/api/v1/ports-for-ip | 
*DefaultApi* | [**get_prime**](docs/DefaultApi.md#get_prime) | **GET** /recon/api/v1/prime | 
*DefaultApi* | [**get_report**](docs/DefaultApi.md#get_report) | **GET** /recon/api/v1/report | 
*DefaultApi* | [**get_saved_views**](docs/DefaultApi.md#get_saved_views) | **GET** /recon/api/v1/saved-views | 
*DefaultApi* | [**get_service**](docs/DefaultApi.md#get_service) | **GET** /recon/api/v1/service | 
*DefaultApi* | [**get_single_action_metadata**](docs/DefaultApi.md#get_single_action_metadata) | **GET** /attack/api/v1/user/actions/{id} | 
*DefaultApi* | [**get_single_attack_implants**](docs/DefaultApi.md#get_single_attack_implants) | **GET** /attack/api/v1/user/implants/{id} | 
*DefaultApi* | [**get_single_attack_user_action_descriptions**](docs/DefaultApi.md#get_single_attack_user_action_descriptions) | **GET** /attack/api/v1/user/attack-action-descriptions/{id} | 
*DefaultApi* | [**get_single_attack_user_autoapprove**](docs/DefaultApi.md#get_single_attack_user_autoapprove) | **GET** /attack/api/v1/user/attack-autoapprove/{id} | 
*DefaultApi* | [**get_single_attack_user_runbook_descriptions**](docs/DefaultApi.md#get_single_attack_user_runbook_descriptions) | **GET** /attack/api/v1/user/attack-runbook-descriptions/{id} | 
*DefaultApi* | [**get_single_detection_for_target**](docs/DefaultApi.md#get_single_detection_for_target) | **GET** /recon/api/v1/single-detection-for-target | 
*DefaultApi* | [**get_single_hostname**](docs/DefaultApi.md#get_single_hostname) | **GET** /recon/api/v1/hostname/{id} | 
*DefaultApi* | [**get_single_hostnames_for_ip**](docs/DefaultApi.md#get_single_hostnames_for_ip) | **GET** /recon/api/v1/hostnames-for-ip/{id} | 
*DefaultApi* | [**get_single_ip**](docs/DefaultApi.md#get_single_ip) | **GET** /recon/api/v1/ip/{id} | 
*DefaultApi* | [**get_single_ips_for_hostname**](docs/DefaultApi.md#get_single_ips_for_hostname) | **GET** /recon/api/v1/ips-for-hostname/{id} | 
*DefaultApi* | [**get_single_ips_for_network**](docs/DefaultApi.md#get_single_ips_for_network) | **GET** /recon/api/v1/ips-for-network/{id} | 
*DefaultApi* | [**get_single_ips_for_service**](docs/DefaultApi.md#get_single_ips_for_service) | **GET** /recon/api/v1/ips-for-service/{id} | 
*DefaultApi* | [**get_single_network**](docs/DefaultApi.md#get_single_network) | **GET** /recon/api/v1/network/{id} | 
*DefaultApi* | [**get_single_peer**](docs/DefaultApi.md#get_single_peer) | **GET** /recon/api/v1/peer/{id} | 
*DefaultApi* | [**get_single_peer_map**](docs/DefaultApi.md#get_single_peer_map) | **GET** /recon/api/v1/peer-map/{id} | 
*DefaultApi* | [**get_single_ports_for_ip**](docs/DefaultApi.md#get_single_ports_for_ip) | **GET** /recon/api/v1/ports-for-ip/{id} | 
*DefaultApi* | [**get_single_report**](docs/DefaultApi.md#get_single_report) | **GET** /recon/api/v1/report/{id} | 
*DefaultApi* | [**get_single_saved_views**](docs/DefaultApi.md#get_single_saved_views) | **GET** /recon/api/v1/saved-views/{id} | 
*DefaultApi* | [**get_single_service**](docs/DefaultApi.md#get_single_service) | **GET** /recon/api/v1/service/{id} | 
*DefaultApi* | [**get_single_tagcounts**](docs/DefaultApi.md#get_single_tagcounts) | **GET** /recon/api/v1/tagcounts/{id} | 
*DefaultApi* | [**get_single_target**](docs/DefaultApi.md#get_single_target) | **GET** /recon/api/v1/target/{id} | 
*DefaultApi* | [**get_single_user_ap_action_instances**](docs/DefaultApi.md#get_single_user_ap_action_instances) | **GET** /attack/api/v1/user/ap-action-instance/{id} | 
*DefaultApi* | [**get_social_entity**](docs/DefaultApi.md#get_social_entity) | **GET** /recon/api/v1/social-entity | 
*DefaultApi* | [**get_statistics**](docs/DefaultApi.md#get_statistics) | **GET** /recon/api/v1/statistics | 
*DefaultApi* | [**get_tagcounts**](docs/DefaultApi.md#get_tagcounts) | **GET** /recon/api/v1/tagcounts | 
*DefaultApi* | [**get_target**](docs/DefaultApi.md#get_target) | **GET** /recon/api/v1/target | 
*DefaultApi* | [**get_user_ap_action_instances**](docs/DefaultApi.md#get_user_ap_action_instances) | **GET** /attack/api/v1/user/ap-action-instance | 
*DefaultApi* | [**hoc_submit**](docs/DefaultApi.md#hoc_submit) | **POST** /artifactstore/api/v1/hoc/submit | 
*DefaultApi* | [**hoc_submit_cpio**](docs/DefaultApi.md#hoc_submit_cpio) | **POST** /artifactstore/api/v1/hoc/submit-cpio | 
*DefaultApi* | [**impact_score_groups**](docs/DefaultApi.md#impact_score_groups) | **POST** /recon/api/v1/impact_score_groups | 
*DefaultApi* | [**patch_hostname**](docs/DefaultApi.md#patch_hostname) | **PATCH** /recon/api/v1/hostname | 
*DefaultApi* | [**patch_ip**](docs/DefaultApi.md#patch_ip) | **PATCH** /recon/api/v1/ip | 
*DefaultApi* | [**patch_network**](docs/DefaultApi.md#patch_network) | **PATCH** /recon/api/v1/network | 
*DefaultApi* | [**patch_single_attack_user_action_descriptions**](docs/DefaultApi.md#patch_single_attack_user_action_descriptions) | **PATCH** /attack/api/v1/user/attack-action-descriptions/{id} | 
*DefaultApi* | [**patch_single_attack_user_autoapprove**](docs/DefaultApi.md#patch_single_attack_user_autoapprove) | **PATCH** /attack/api/v1/user/attack-autoapprove/{id} | 
*DefaultApi* | [**patch_single_attack_user_runbook_descriptions**](docs/DefaultApi.md#patch_single_attack_user_runbook_descriptions) | **PATCH** /attack/api/v1/user/attack-runbook-descriptions/{id} | 
*DefaultApi* | [**patch_single_peer_map**](docs/DefaultApi.md#patch_single_peer_map) | **PATCH** /recon/api/v1/peer-map/{id} | 
*DefaultApi* | [**patch_single_policy**](docs/DefaultApi.md#patch_single_policy) | **PATCH** /recon/api/v1/policy/{id} | 
*DefaultApi* | [**patch_single_saved_views**](docs/DefaultApi.md#patch_single_saved_views) | **PATCH** /recon/api/v1/saved-views/{id} | 
*DefaultApi* | [**patch_single_user_ap_action_instances**](docs/DefaultApi.md#patch_single_user_ap_action_instances) | **PATCH** /attack/api/v1/user/ap-action-instance/{id} | 
*DefaultApi* | [**patch_social_entity**](docs/DefaultApi.md#patch_social_entity) | **PATCH** /recon/api/v1/social-entity | 
*DefaultApi* | [**patch_target**](docs/DefaultApi.md#patch_target) | **PATCH** /recon/api/v1/target | 
*DefaultApi* | [**paths**](docs/DefaultApi.md#paths) | **GET** /recon/api/v1/paths | 
*DefaultApi* | [**post_attack_user_action_descriptions**](docs/DefaultApi.md#post_attack_user_action_descriptions) | **POST** /attack/api/v1/user/attack-action-descriptions | 
*DefaultApi* | [**post_attack_user_autoapprove**](docs/DefaultApi.md#post_attack_user_autoapprove) | **POST** /attack/api/v1/user/attack-autoapprove | 
*DefaultApi* | [**post_attack_user_runbook_descriptions**](docs/DefaultApi.md#post_attack_user_runbook_descriptions) | **POST** /attack/api/v1/user/attack-runbook-descriptions | 
*DefaultApi* | [**post_comment_multi**](docs/DefaultApi.md#post_comment_multi) | **POST** /recon/api/v1/comment | 
*DefaultApi* | [**post_peer**](docs/DefaultApi.md#post_peer) | **POST** /recon/api/v1/peer | 
*DefaultApi* | [**post_peer_map**](docs/DefaultApi.md#post_peer_map) | **POST** /recon/api/v1/peer-map | 
*DefaultApi* | [**post_policy**](docs/DefaultApi.md#post_policy) | **POST** /recon/api/v1/policy | 
*DefaultApi* | [**post_saved_views**](docs/DefaultApi.md#post_saved_views) | **POST** /recon/api/v1/saved-views | 
*DefaultApi* | [**post_user_ap_action_instances**](docs/DefaultApi.md#post_user_ap_action_instances) | **POST** /attack/api/v1/user/ap-action-instance | 
*DefaultApi* | [**priority_groups**](docs/DefaultApi.md#priority_groups) | **POST** /recon/api/v1/priority_groups | 
*DefaultApi* | [**recon_worker_node_ips**](docs/DefaultApi.md#recon_worker_node_ips) | **GET** /recon/api/v1/recon-worker-node-ips | 
*DefaultApi* | [**status_groups**](docs/DefaultApi.md#status_groups) | **POST** /recon/api/v1/status_groups | 
*DefaultApi* | [**tag**](docs/DefaultApi.md#tag) | **GET** /recon/api/v1/tag | 
*DefaultApi* | [**target_temptation_groups**](docs/DefaultApi.md#target_temptation_groups) | **POST** /recon/api/v1/target_temptation_groups | 
*DefaultApi* | [**user_query**](docs/DefaultApi.md#user_query) | **GET** /artifactstore/api/v1/user/query | 
*DefaultApi* | [**user_retrieve**](docs/DefaultApi.md#user_retrieve) | **GET** /artifactstore/api/v1/user/retrieve/{shasum} | 
*DefaultApi* | [**uuid_comment_id**](docs/DefaultApi.md#uuid_comment_id) | **DELETE** /recon/api/v1/entity/{entity_id}/comment/{comment_id} | 
*DefaultApi* | [**uuid_comment_id_0**](docs/DefaultApi.md#uuid_comment_id_0) | **PATCH** /recon/api/v1/entity/{entity_id}/comment/{comment_id} | 


## Documentation For Models

 - [ActionMetadata](docs/ActionMetadata.md)
 - [ActionMetadataGetOutput](docs/ActionMetadataGetOutput.md)
 - [ActionMetadataSingleOutput](docs/ActionMetadataSingleOutput.md)
 - [ActionMetadataSingleOutputData](docs/ActionMetadataSingleOutputData.md)
 - [AllDetectionsForTarget](docs/AllDetectionsForTarget.md)
 - [AllDetectionsForTargetGetOutput](docs/AllDetectionsForTargetGetOutput.md)
 - [Artifactsrc](docs/Artifactsrc.md)
 - [ArtifactsrcMany](docs/ArtifactsrcMany.md)
 - [AttackCheckinsForImplant](docs/AttackCheckinsForImplant.md)
 - [AttackCheckinsForImplantGetOutput](docs/AttackCheckinsForImplantGetOutput.md)
 - [AttackImplants](docs/AttackImplants.md)
 - [AttackImplantsGetOutput](docs/AttackImplantsGetOutput.md)
 - [AttackImplantsSingleOutput](docs/AttackImplantsSingleOutput.md)
 - [AttackImplantsSingleOutputData](docs/AttackImplantsSingleOutputData.md)
 - [AttackInterfacesForImplant](docs/AttackInterfacesForImplant.md)
 - [AttackInterfacesForImplantGetOutput](docs/AttackInterfacesForImplantGetOutput.md)
 - [AttackRedirectors](docs/AttackRedirectors.md)
 - [AttackRedirectorsGetOutput](docs/AttackRedirectorsGetOutput.md)
 - [AttackRunbook](docs/AttackRunbook.md)
 - [AttackRunbookGetOutput](docs/AttackRunbookGetOutput.md)
 - [AttackStatistics](docs/AttackStatistics.md)
 - [AttackStatisticsGetOutput](docs/AttackStatisticsGetOutput.md)
 - [AttackUserActionDescriptions](docs/AttackUserActionDescriptions.md)
 - [AttackUserActionDescriptionsGetOutput](docs/AttackUserActionDescriptionsGetOutput.md)
 - [AttackUserActionDescriptionsModelIn](docs/AttackUserActionDescriptionsModelIn.md)
 - [AttackUserActionDescriptionsPatchIn](docs/AttackUserActionDescriptionsPatchIn.md)
 - [AttackUserActionDescriptionsPatchSingleInput](docs/AttackUserActionDescriptionsPatchSingleInput.md)
 - [AttackUserActionDescriptionsPatchSingleInputData](docs/AttackUserActionDescriptionsPatchSingleInputData.md)
 - [AttackUserActionDescriptionsPostInput](docs/AttackUserActionDescriptionsPostInput.md)
 - [AttackUserActionDescriptionsPostOutput](docs/AttackUserActionDescriptionsPostOutput.md)
 - [AttackUserActionDescriptionsSingleOutput](docs/AttackUserActionDescriptionsSingleOutput.md)
 - [AttackUserActionDescriptionsSingleOutputData](docs/AttackUserActionDescriptionsSingleOutputData.md)
 - [AttackUserAutoapprove](docs/AttackUserAutoapprove.md)
 - [AttackUserAutoapproveGetOutput](docs/AttackUserAutoapproveGetOutput.md)
 - [AttackUserAutoapproveModelIn](docs/AttackUserAutoapproveModelIn.md)
 - [AttackUserAutoapprovePatchIn](docs/AttackUserAutoapprovePatchIn.md)
 - [AttackUserAutoapprovePatchSingleInput](docs/AttackUserAutoapprovePatchSingleInput.md)
 - [AttackUserAutoapprovePatchSingleInputData](docs/AttackUserAutoapprovePatchSingleInputData.md)
 - [AttackUserAutoapprovePostInput](docs/AttackUserAutoapprovePostInput.md)
 - [AttackUserAutoapprovePostOutput](docs/AttackUserAutoapprovePostOutput.md)
 - [AttackUserAutoapproveSingleOutput](docs/AttackUserAutoapproveSingleOutput.md)
 - [AttackUserAutoapproveSingleOutputData](docs/AttackUserAutoapproveSingleOutputData.md)
 - [AttackUserRunbookDescriptions](docs/AttackUserRunbookDescriptions.md)
 - [AttackUserRunbookDescriptionsGetOutput](docs/AttackUserRunbookDescriptionsGetOutput.md)
 - [AttackUserRunbookDescriptionsModelIn](docs/AttackUserRunbookDescriptionsModelIn.md)
 - [AttackUserRunbookDescriptionsPatchIn](docs/AttackUserRunbookDescriptionsPatchIn.md)
 - [AttackUserRunbookDescriptionsPatchSingleInput](docs/AttackUserRunbookDescriptionsPatchSingleInput.md)
 - [AttackUserRunbookDescriptionsPatchSingleInputData](docs/AttackUserRunbookDescriptionsPatchSingleInputData.md)
 - [AttackUserRunbookDescriptionsPostInput](docs/AttackUserRunbookDescriptionsPostInput.md)
 - [AttackUserRunbookDescriptionsPostOutput](docs/AttackUserRunbookDescriptionsPostOutput.md)
 - [AttackUserRunbookDescriptionsSingleOutput](docs/AttackUserRunbookDescriptionsSingleOutput.md)
 - [AttackUserRunbookDescriptionsSingleOutputData](docs/AttackUserRunbookDescriptionsSingleOutputData.md)
 - [CommentCreationSchema](docs/CommentCreationSchema.md)
 - [CommentResponseCollectionSchema](docs/CommentResponseCollectionSchema.md)
 - [CommentResponseSchema](docs/CommentResponseSchema.md)
 - [ErrorSchema](docs/ErrorSchema.md)
 - [ExternalCommentCreationSchema](docs/ExternalCommentCreationSchema.md)
 - [Hostname](docs/Hostname.md)
 - [HostnameGetOutput](docs/HostnameGetOutput.md)
 - [HostnamePatchIn](docs/HostnamePatchIn.md)
 - [HostnamePatchInput](docs/HostnamePatchInput.md)
 - [HostnamePatchInputData](docs/HostnamePatchInputData.md)
 - [HostnamePatchInputOperationsInner](docs/HostnamePatchInputOperationsInner.md)
 - [HostnamePatchInputQ](docs/HostnamePatchInputQ.md)
 - [HostnamePatchOutput](docs/HostnamePatchOutput.md)
 - [HostnameSingleOutput](docs/HostnameSingleOutput.md)
 - [HostnameSingleOutputData](docs/HostnameSingleOutputData.md)
 - [HostnamesForIp](docs/HostnamesForIp.md)
 - [HostnamesForIpGetOutput](docs/HostnamesForIpGetOutput.md)
 - [HostnamesForIpSingleOutput](docs/HostnamesForIpSingleOutput.md)
 - [HostnamesForIpSingleOutputData](docs/HostnamesForIpSingleOutputData.md)
 - [ImpactScoreEntityReq](docs/ImpactScoreEntityReq.md)
 - [ImpactScoreGroupInnerResult](docs/ImpactScoreGroupInnerResult.md)
 - [ImpactScoreGroupOuterResult](docs/ImpactScoreGroupOuterResult.md)
 - [Ip](docs/Ip.md)
 - [IpGetOutput](docs/IpGetOutput.md)
 - [IpPatchIn](docs/IpPatchIn.md)
 - [IpPatchInput](docs/IpPatchInput.md)
 - [IpPatchInputData](docs/IpPatchInputData.md)
 - [IpPatchOutput](docs/IpPatchOutput.md)
 - [IpSingleOutput](docs/IpSingleOutput.md)
 - [IpSingleOutputData](docs/IpSingleOutputData.md)
 - [IpsForHostname](docs/IpsForHostname.md)
 - [IpsForHostnameGetOutput](docs/IpsForHostnameGetOutput.md)
 - [IpsForHostnameSingleOutput](docs/IpsForHostnameSingleOutput.md)
 - [IpsForHostnameSingleOutputData](docs/IpsForHostnameSingleOutputData.md)
 - [IpsForNetwork](docs/IpsForNetwork.md)
 - [IpsForNetworkGetOutput](docs/IpsForNetworkGetOutput.md)
 - [IpsForNetworkSingleOutput](docs/IpsForNetworkSingleOutput.md)
 - [IpsForNetworkSingleOutputData](docs/IpsForNetworkSingleOutputData.md)
 - [IpsForService](docs/IpsForService.md)
 - [IpsForServiceGetOutput](docs/IpsForServiceGetOutput.md)
 - [IpsForServiceSingleOutput](docs/IpsForServiceSingleOutput.md)
 - [IpsForServiceSingleOutputData](docs/IpsForServiceSingleOutputData.md)
 - [JsonPatchOperation](docs/JsonPatchOperation.md)
 - [Network](docs/Network.md)
 - [NetworkGetOutput](docs/NetworkGetOutput.md)
 - [NetworkPatchIn](docs/NetworkPatchIn.md)
 - [NetworkPatchInput](docs/NetworkPatchInput.md)
 - [NetworkPatchInputData](docs/NetworkPatchInputData.md)
 - [NetworkPatchOutput](docs/NetworkPatchOutput.md)
 - [NetworkSingleOutput](docs/NetworkSingleOutput.md)
 - [NetworkSingleOutputData](docs/NetworkSingleOutputData.md)
 - [PathDrSchema](docs/PathDrSchema.md)
 - [PathEntitySchema](docs/PathEntitySchema.md)
 - [PathsDataSchema](docs/PathsDataSchema.md)
 - [PathsOutputSchema](docs/PathsOutputSchema.md)
 - [Peer](docs/Peer.md)
 - [PeerGetOutput](docs/PeerGetOutput.md)
 - [PeerMap](docs/PeerMap.md)
 - [PeerMapGetOutput](docs/PeerMapGetOutput.md)
 - [PeerMapModelIn](docs/PeerMapModelIn.md)
 - [PeerMapPatchIn](docs/PeerMapPatchIn.md)
 - [PeerMapPatchSingleInput](docs/PeerMapPatchSingleInput.md)
 - [PeerMapPatchSingleInputData](docs/PeerMapPatchSingleInputData.md)
 - [PeerMapPostInput](docs/PeerMapPostInput.md)
 - [PeerMapPostOutput](docs/PeerMapPostOutput.md)
 - [PeerMapSingleOutput](docs/PeerMapSingleOutput.md)
 - [PeerMapSingleOutputData](docs/PeerMapSingleOutputData.md)
 - [PeerModelIn](docs/PeerModelIn.md)
 - [PeerPostInput](docs/PeerPostInput.md)
 - [PeerPostOutput](docs/PeerPostOutput.md)
 - [PeerSingleOutput](docs/PeerSingleOutput.md)
 - [PeerSingleOutputData](docs/PeerSingleOutputData.md)
 - [Policy](docs/Policy.md)
 - [PolicyGetOutput](docs/PolicyGetOutput.md)
 - [PolicyModelCustomIn](docs/PolicyModelCustomIn.md)
 - [PolicyPatchIn](docs/PolicyPatchIn.md)
 - [PolicyPatchSingleInput](docs/PolicyPatchSingleInput.md)
 - [PolicyPatchSingleInputData](docs/PolicyPatchSingleInputData.md)
 - [PolicyPostInput](docs/PolicyPostInput.md)
 - [PolicyPostOutput](docs/PolicyPostOutput.md)
 - [PolicySingleInput](docs/PolicySingleInput.md)
 - [PolicySingleOutput](docs/PolicySingleOutput.md)
 - [PolicySingleOutputData](docs/PolicySingleOutputData.md)
 - [PortsForIp](docs/PortsForIp.md)
 - [PortsForIpGetOutput](docs/PortsForIpGetOutput.md)
 - [PortsForIpSingleOutput](docs/PortsForIpSingleOutput.md)
 - [PortsForIpSingleOutputData](docs/PortsForIpSingleOutputData.md)
 - [Prime](docs/Prime.md)
 - [PrimeGetOutput](docs/PrimeGetOutput.md)
 - [PriorityEntityReq](docs/PriorityEntityReq.md)
 - [PriorityGroupInnerResult](docs/PriorityGroupInnerResult.md)
 - [PriorityGroupOuterResult](docs/PriorityGroupOuterResult.md)
 - [PriorityRange](docs/PriorityRange.md)
 - [QuerybuilderRuleGroupSchema](docs/QuerybuilderRuleGroupSchema.md)
 - [ReconWorkerNodeIps](docs/ReconWorkerNodeIps.md)
 - [Report](docs/Report.md)
 - [ReportGetOutput](docs/ReportGetOutput.md)
 - [ReportSingleOutput](docs/ReportSingleOutput.md)
 - [ReportSingleOutputData](docs/ReportSingleOutputData.md)
 - [SavedViews](docs/SavedViews.md)
 - [SavedViewsGetOutput](docs/SavedViewsGetOutput.md)
 - [SavedViewsModelCustomIn](docs/SavedViewsModelCustomIn.md)
 - [SavedViewsPatchIn](docs/SavedViewsPatchIn.md)
 - [SavedViewsPatchSingleInput](docs/SavedViewsPatchSingleInput.md)
 - [SavedViewsPatchSingleInputData](docs/SavedViewsPatchSingleInputData.md)
 - [SavedViewsPostInput](docs/SavedViewsPostInput.md)
 - [SavedViewsPostOutput](docs/SavedViewsPostOutput.md)
 - [SavedViewsSingleInput](docs/SavedViewsSingleInput.md)
 - [SavedViewsSingleOutput](docs/SavedViewsSingleOutput.md)
 - [SavedViewsSingleOutputData](docs/SavedViewsSingleOutputData.md)
 - [Service](docs/Service.md)
 - [ServiceGetOutput](docs/ServiceGetOutput.md)
 - [ServiceSingleOutput](docs/ServiceSingleOutput.md)
 - [ServiceSingleOutputData](docs/ServiceSingleOutputData.md)
 - [SingleDetectionForTarget](docs/SingleDetectionForTarget.md)
 - [SingleDetectionForTargetGetOutput](docs/SingleDetectionForTargetGetOutput.md)
 - [SocialEntity](docs/SocialEntity.md)
 - [SocialEntityGetOutput](docs/SocialEntityGetOutput.md)
 - [SocialEntityPatchIn](docs/SocialEntityPatchIn.md)
 - [SocialEntityPatchInput](docs/SocialEntityPatchInput.md)
 - [SocialEntityPatchInputData](docs/SocialEntityPatchInputData.md)
 - [SocialEntityPatchOutput](docs/SocialEntityPatchOutput.md)
 - [Statistics](docs/Statistics.md)
 - [StatisticsGetOutput](docs/StatisticsGetOutput.md)
 - [StatusEntityReq](docs/StatusEntityReq.md)
 - [StatusGroupInnerResult](docs/StatusGroupInnerResult.md)
 - [StatusGroupOuterResult](docs/StatusGroupOuterResult.md)
 - [Tagcounts](docs/Tagcounts.md)
 - [TagcountsGetOutput](docs/TagcountsGetOutput.md)
 - [TagcountsSingleOutput](docs/TagcountsSingleOutput.md)
 - [TagcountsSingleOutputData](docs/TagcountsSingleOutputData.md)
 - [Target](docs/Target.md)
 - [TargetGetOutput](docs/TargetGetOutput.md)
 - [TargetPatchIn](docs/TargetPatchIn.md)
 - [TargetPatchInput](docs/TargetPatchInput.md)
 - [TargetPatchInputData](docs/TargetPatchInputData.md)
 - [TargetPatchOutput](docs/TargetPatchOutput.md)
 - [TargetSingleOutput](docs/TargetSingleOutput.md)
 - [TargetSingleOutputData](docs/TargetSingleOutputData.md)
 - [TargetTemptationEntityReq](docs/TargetTemptationEntityReq.md)
 - [TargetTemptationGroupInnerResult](docs/TargetTemptationGroupInnerResult.md)
 - [TargetTemptationGroupOuterResult](docs/TargetTemptationGroupOuterResult.md)
 - [TargetTemptationRange](docs/TargetTemptationRange.md)
 - [UserApActionInstances](docs/UserApActionInstances.md)
 - [UserApActionInstancesGetOutput](docs/UserApActionInstancesGetOutput.md)
 - [UserApActionInstancesModelIn](docs/UserApActionInstancesModelIn.md)
 - [UserApActionInstancesPatchIn](docs/UserApActionInstancesPatchIn.md)
 - [UserApActionInstancesPatchSingleInput](docs/UserApActionInstancesPatchSingleInput.md)
 - [UserApActionInstancesPatchSingleInputData](docs/UserApActionInstancesPatchSingleInputData.md)
 - [UserApActionInstancesPostInput](docs/UserApActionInstancesPostInput.md)
 - [UserApActionInstancesPostOutput](docs/UserApActionInstancesPostOutput.md)
 - [UserApActionInstancesSingleOutput](docs/UserApActionInstancesSingleOutput.md)
 - [UserApActionInstancesSingleOutputData](docs/UserApActionInstancesSingleOutputData.md)
 - [UserArtifactQuery](docs/UserArtifactQuery.md)
 - [UserTagNameList](docs/UserTagNameList.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication (JWT)


## Author

support@randori.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in randori_api.apis and randori_api.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from randori_api.api.default_api import DefaultApi`
- `from randori_api.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import randori_api
from randori_api.apis import *
from randori_api.models import *
```

