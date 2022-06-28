# randori_api.DefaultApi

All URIs are relative to *https://app.randori.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_affiliation**](DefaultApi.md#add_affiliation) | **POST** /artifactstore/api/v1/add_affiliation | 
[**add_affiliation_file**](DefaultApi.md#add_affiliation_file) | **POST** /artifactstore/api/v1/add_affiliation_file | 
[**artifact**](DefaultApi.md#artifact) | **GET** /artifactstore/api/v1/artifact/{artifact_uuid} | 
[**artifact_raw**](DefaultApi.md#artifact_raw) | **GET** /artifactstore/api/v1/artifact-raw/{shasum} | 
[**comment**](DefaultApi.md#comment) | **GET** /recon/api/v1/entity/{entity_id}/comment | 
[**comment_0**](DefaultApi.md#comment_0) | **POST** /recon/api/v1/entity/{entity_id}/comment | 
[**delete_single_attack_user_action_descriptions**](DefaultApi.md#delete_single_attack_user_action_descriptions) | **DELETE** /attack/api/v1/user/attack-action-descriptions/{id} | 
[**delete_single_attack_user_runbook_descriptions**](DefaultApi.md#delete_single_attack_user_runbook_descriptions) | **DELETE** /attack/api/v1/user/attack-runbook-descriptions/{id} | 
[**delete_single_policy**](DefaultApi.md#delete_single_policy) | **DELETE** /recon/api/v1/policy/{id} | 
[**delete_single_saved_views**](DefaultApi.md#delete_single_saved_views) | **DELETE** /recon/api/v1/saved-views/{id} | 
[**get_action_metadata**](DefaultApi.md#get_action_metadata) | **GET** /attack/api/v1/user/actions | 
[**get_all_detections_for_target**](DefaultApi.md#get_all_detections_for_target) | **GET** /recon/api/v1/all-detections-for-target | 
[**get_attack_checkins_for_implant**](DefaultApi.md#get_attack_checkins_for_implant) | **GET** /attack/api/v1/user/checkins-for-implant | 
[**get_attack_implants**](DefaultApi.md#get_attack_implants) | **GET** /attack/api/v1/user/implants | 
[**get_attack_interfaces_for_implant**](DefaultApi.md#get_attack_interfaces_for_implant) | **GET** /attack/api/v1/user/interfaces-for-implant | 
[**get_attack_redirectors**](DefaultApi.md#get_attack_redirectors) | **GET** /attack/api/v1/user/redirectors | 
[**get_attack_runbook**](DefaultApi.md#get_attack_runbook) | **GET** /attack/api/v1/user/runbooks | 
[**get_attack_statistics**](DefaultApi.md#get_attack_statistics) | **GET** /attack/api/v1/user/statistics | 
[**get_attack_user_action_descriptions**](DefaultApi.md#get_attack_user_action_descriptions) | **GET** /attack/api/v1/user/attack-action-descriptions | 
[**get_attack_user_autoapprove**](DefaultApi.md#get_attack_user_autoapprove) | **GET** /attack/api/v1/user/attack-autoapprove | 
[**get_attack_user_runbook_descriptions**](DefaultApi.md#get_attack_user_runbook_descriptions) | **GET** /attack/api/v1/user/attack-runbook-descriptions | 
[**get_hostname**](DefaultApi.md#get_hostname) | **GET** /recon/api/v1/hostname | 
[**get_hostnames_for_ip**](DefaultApi.md#get_hostnames_for_ip) | **GET** /recon/api/v1/hostnames-for-ip | 
[**get_ip**](DefaultApi.md#get_ip) | **GET** /recon/api/v1/ip | 
[**get_ips_for_hostname**](DefaultApi.md#get_ips_for_hostname) | **GET** /recon/api/v1/ips-for-hostname | 
[**get_ips_for_network**](DefaultApi.md#get_ips_for_network) | **GET** /recon/api/v1/ips-for-network | 
[**get_ips_for_service**](DefaultApi.md#get_ips_for_service) | **GET** /recon/api/v1/ips-for-service | 
[**get_network**](DefaultApi.md#get_network) | **GET** /recon/api/v1/network | 
[**get_peer**](DefaultApi.md#get_peer) | **GET** /recon/api/v1/peer | 
[**get_peer_map**](DefaultApi.md#get_peer_map) | **GET** /recon/api/v1/peer-map | 
[**get_policy**](DefaultApi.md#get_policy) | **GET** /recon/api/v1/policy | 
[**get_ports_for_ip**](DefaultApi.md#get_ports_for_ip) | **GET** /recon/api/v1/ports-for-ip | 
[**get_prime**](DefaultApi.md#get_prime) | **GET** /recon/api/v1/prime | 
[**get_report**](DefaultApi.md#get_report) | **GET** /recon/api/v1/report | 
[**get_saved_views**](DefaultApi.md#get_saved_views) | **GET** /recon/api/v1/saved-views | 
[**get_service**](DefaultApi.md#get_service) | **GET** /recon/api/v1/service | 
[**get_single_action_metadata**](DefaultApi.md#get_single_action_metadata) | **GET** /attack/api/v1/user/actions/{id} | 
[**get_single_attack_implants**](DefaultApi.md#get_single_attack_implants) | **GET** /attack/api/v1/user/implants/{id} | 
[**get_single_attack_user_action_descriptions**](DefaultApi.md#get_single_attack_user_action_descriptions) | **GET** /attack/api/v1/user/attack-action-descriptions/{id} | 
[**get_single_attack_user_autoapprove**](DefaultApi.md#get_single_attack_user_autoapprove) | **GET** /attack/api/v1/user/attack-autoapprove/{id} | 
[**get_single_attack_user_runbook_descriptions**](DefaultApi.md#get_single_attack_user_runbook_descriptions) | **GET** /attack/api/v1/user/attack-runbook-descriptions/{id} | 
[**get_single_detection_for_target**](DefaultApi.md#get_single_detection_for_target) | **GET** /recon/api/v1/single-detection-for-target | 
[**get_single_hostname**](DefaultApi.md#get_single_hostname) | **GET** /recon/api/v1/hostname/{id} | 
[**get_single_hostnames_for_ip**](DefaultApi.md#get_single_hostnames_for_ip) | **GET** /recon/api/v1/hostnames-for-ip/{id} | 
[**get_single_ip**](DefaultApi.md#get_single_ip) | **GET** /recon/api/v1/ip/{id} | 
[**get_single_ips_for_hostname**](DefaultApi.md#get_single_ips_for_hostname) | **GET** /recon/api/v1/ips-for-hostname/{id} | 
[**get_single_ips_for_network**](DefaultApi.md#get_single_ips_for_network) | **GET** /recon/api/v1/ips-for-network/{id} | 
[**get_single_ips_for_service**](DefaultApi.md#get_single_ips_for_service) | **GET** /recon/api/v1/ips-for-service/{id} | 
[**get_single_network**](DefaultApi.md#get_single_network) | **GET** /recon/api/v1/network/{id} | 
[**get_single_peer**](DefaultApi.md#get_single_peer) | **GET** /recon/api/v1/peer/{id} | 
[**get_single_peer_map**](DefaultApi.md#get_single_peer_map) | **GET** /recon/api/v1/peer-map/{id} | 
[**get_single_ports_for_ip**](DefaultApi.md#get_single_ports_for_ip) | **GET** /recon/api/v1/ports-for-ip/{id} | 
[**get_single_report**](DefaultApi.md#get_single_report) | **GET** /recon/api/v1/report/{id} | 
[**get_single_saved_views**](DefaultApi.md#get_single_saved_views) | **GET** /recon/api/v1/saved-views/{id} | 
[**get_single_service**](DefaultApi.md#get_single_service) | **GET** /recon/api/v1/service/{id} | 
[**get_single_tagcounts**](DefaultApi.md#get_single_tagcounts) | **GET** /recon/api/v1/tagcounts/{id} | 
[**get_single_target**](DefaultApi.md#get_single_target) | **GET** /recon/api/v1/target/{id} | 
[**get_single_user_ap_action_instances**](DefaultApi.md#get_single_user_ap_action_instances) | **GET** /attack/api/v1/user/ap-action-instance/{id} | 
[**get_social_entity**](DefaultApi.md#get_social_entity) | **GET** /recon/api/v1/social-entity | 
[**get_statistics**](DefaultApi.md#get_statistics) | **GET** /recon/api/v1/statistics | 
[**get_tagcounts**](DefaultApi.md#get_tagcounts) | **GET** /recon/api/v1/tagcounts | 
[**get_target**](DefaultApi.md#get_target) | **GET** /recon/api/v1/target | 
[**get_user_ap_action_instances**](DefaultApi.md#get_user_ap_action_instances) | **GET** /attack/api/v1/user/ap-action-instance | 
[**hoc_submit**](DefaultApi.md#hoc_submit) | **POST** /artifactstore/api/v1/hoc/submit | 
[**hoc_submit_cpio**](DefaultApi.md#hoc_submit_cpio) | **POST** /artifactstore/api/v1/hoc/submit-cpio | 
[**impact_score_groups**](DefaultApi.md#impact_score_groups) | **POST** /recon/api/v1/impact_score_groups | 
[**patch_hostname**](DefaultApi.md#patch_hostname) | **PATCH** /recon/api/v1/hostname | 
[**patch_ip**](DefaultApi.md#patch_ip) | **PATCH** /recon/api/v1/ip | 
[**patch_network**](DefaultApi.md#patch_network) | **PATCH** /recon/api/v1/network | 
[**patch_single_attack_user_action_descriptions**](DefaultApi.md#patch_single_attack_user_action_descriptions) | **PATCH** /attack/api/v1/user/attack-action-descriptions/{id} | 
[**patch_single_attack_user_autoapprove**](DefaultApi.md#patch_single_attack_user_autoapprove) | **PATCH** /attack/api/v1/user/attack-autoapprove/{id} | 
[**patch_single_attack_user_runbook_descriptions**](DefaultApi.md#patch_single_attack_user_runbook_descriptions) | **PATCH** /attack/api/v1/user/attack-runbook-descriptions/{id} | 
[**patch_single_peer_map**](DefaultApi.md#patch_single_peer_map) | **PATCH** /recon/api/v1/peer-map/{id} | 
[**patch_single_policy**](DefaultApi.md#patch_single_policy) | **PATCH** /recon/api/v1/policy/{id} | 
[**patch_single_saved_views**](DefaultApi.md#patch_single_saved_views) | **PATCH** /recon/api/v1/saved-views/{id} | 
[**patch_single_user_ap_action_instances**](DefaultApi.md#patch_single_user_ap_action_instances) | **PATCH** /attack/api/v1/user/ap-action-instance/{id} | 
[**patch_social_entity**](DefaultApi.md#patch_social_entity) | **PATCH** /recon/api/v1/social-entity | 
[**patch_target**](DefaultApi.md#patch_target) | **PATCH** /recon/api/v1/target | 
[**paths**](DefaultApi.md#paths) | **GET** /recon/api/v1/paths | 
[**post_attack_user_action_descriptions**](DefaultApi.md#post_attack_user_action_descriptions) | **POST** /attack/api/v1/user/attack-action-descriptions | 
[**post_attack_user_autoapprove**](DefaultApi.md#post_attack_user_autoapprove) | **POST** /attack/api/v1/user/attack-autoapprove | 
[**post_attack_user_runbook_descriptions**](DefaultApi.md#post_attack_user_runbook_descriptions) | **POST** /attack/api/v1/user/attack-runbook-descriptions | 
[**post_comment_multi**](DefaultApi.md#post_comment_multi) | **POST** /recon/api/v1/comment | 
[**post_peer**](DefaultApi.md#post_peer) | **POST** /recon/api/v1/peer | 
[**post_peer_map**](DefaultApi.md#post_peer_map) | **POST** /recon/api/v1/peer-map | 
[**post_policy**](DefaultApi.md#post_policy) | **POST** /recon/api/v1/policy | 
[**post_saved_views**](DefaultApi.md#post_saved_views) | **POST** /recon/api/v1/saved-views | 
[**post_user_ap_action_instances**](DefaultApi.md#post_user_ap_action_instances) | **POST** /attack/api/v1/user/ap-action-instance | 
[**priority_groups**](DefaultApi.md#priority_groups) | **POST** /recon/api/v1/priority_groups | 
[**recon_worker_node_ips**](DefaultApi.md#recon_worker_node_ips) | **GET** /recon/api/v1/recon-worker-node-ips | 
[**status_groups**](DefaultApi.md#status_groups) | **POST** /recon/api/v1/status_groups | 
[**tag**](DefaultApi.md#tag) | **GET** /recon/api/v1/tag | 
[**target_temptation_groups**](DefaultApi.md#target_temptation_groups) | **POST** /recon/api/v1/target_temptation_groups | 
[**user_query**](DefaultApi.md#user_query) | **GET** /artifactstore/api/v1/user/query | 
[**user_retrieve**](DefaultApi.md#user_retrieve) | **GET** /artifactstore/api/v1/user/retrieve/{shasum} | 
[**uuid_comment_id**](DefaultApi.md#uuid_comment_id) | **DELETE** /recon/api/v1/entity/{entity_id}/comment/{comment_id} | 
[**uuid_comment_id_0**](DefaultApi.md#uuid_comment_id_0) | **PATCH** /recon/api/v1/entity/{entity_id}/comment/{comment_id} | 


# **add_affiliation**
> add_affiliation()



Add missing affiliations for an organization

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.add_affiliation()
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->add_affiliation: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_affiliation_file**
> add_affiliation_file()



Add a file of missing affiliations for an organization

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.add_affiliation_file()
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->add_affiliation_file: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifact**
> artifact(artifact_uuid2)



Get Artifact by UUID

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    artifact_uuid2 = "artifact_uuid_example" # str | 
    artifact_uuid = "artifact_uuid_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.artifact(artifact_uuid2)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->artifact: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.artifact(artifact_uuid2, artifact_uuid=artifact_uuid)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->artifact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_uuid2** | **str**|  |
 **artifact_uuid** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifact_raw**
> artifact_raw(shasum2)



Get raw Artifact by shasum

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    shasum2 = "shasum_example" # str | 
    shasum = "shasum_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.artifact_raw(shasum2)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->artifact_raw: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.artifact_raw(shasum2, shasum=shasum)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->artifact_raw: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shasum2** | **str**|  |
 **shasum** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comment**
> CommentResponseCollectionSchema comment(entity_id)



Retrieves a page of comments for a provided entity ID.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.comment_response_collection_schema import CommentResponseCollectionSchema
from pprint import pprint
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
    entity_id = "entity_id_example" # str | 
    offset = 1 # int |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.comment(entity_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->comment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.comment(entity_id, offset=offset, limit=limit)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  |
 **offset** | **int**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**CommentResponseCollectionSchema**](CommentResponseCollectionSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comment_0**
> CommentResponseSchema comment_0(entity_id)



Creates a single comment for a provided entity ID.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.comment_creation_schema import CommentCreationSchema
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.comment_response_schema import CommentResponseSchema
from pprint import pprint
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
    entity_id = "entity_id_example" # str | 
    comment_creation_schema = CommentCreationSchema(
        comment="comment_example",
    ) # CommentCreationSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.comment_0(entity_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->comment_0: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.comment_0(entity_id, comment_creation_schema=comment_creation_schema)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->comment_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  |
 **comment_creation_schema** | [**CommentCreationSchema**](CommentCreationSchema.md)|  | [optional]

### Return type

[**CommentResponseSchema**](CommentResponseSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_single_attack_user_action_descriptions**
> delete_single_attack_user_action_descriptions(id)



Remove the attack-user-action-descriptions object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_single_attack_user_action_descriptions(id)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->delete_single_attack_user_action_descriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_single_attack_user_runbook_descriptions**
> delete_single_attack_user_runbook_descriptions(id)



Remove the attack-user-runbook-descriptions object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_single_attack_user_runbook_descriptions(id)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->delete_single_attack_user_runbook_descriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_single_policy**
> delete_single_policy(id)



Remove the policy object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.policy_single_input import PolicySingleInput
from pprint import pprint
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
    id = "id_example" # str | 
    policy_single_input = PolicySingleInput(
        org_id="org_id_example",
    ) # PolicySingleInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_single_policy(id)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->delete_single_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.delete_single_policy(id, policy_single_input=policy_single_input)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->delete_single_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **policy_single_input** | [**PolicySingleInput**](PolicySingleInput.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_single_saved_views**
> delete_single_saved_views(id)



Remove the saved-views object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.saved_views_single_input import SavedViewsSingleInput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 
    saved_views_single_input = SavedViewsSingleInput(
        org_id="org_id_example",
    ) # SavedViewsSingleInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_single_saved_views(id)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->delete_single_saved_views: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.delete_single_saved_views(id, saved_views_single_input=saved_views_single_input)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->delete_single_saved_views: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **saved_views_single_input** | [**SavedViewsSingleInput**](SavedViewsSingleInput.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_metadata**
> ActionMetadataGetOutput get_action_metadata()



Search action-metadata objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.action_metadata_get_output import ActionMetadataGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-action_id",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_action_metadata(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_action_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**ActionMetadataGetOutput**](ActionMetadataGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_detections_for_target**
> AllDetectionsForTargetGetOutput get_all_detections_for_target()



Search all-detections-for-target objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.all_detections_for_target_get_output import AllDetectionsForTargetGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-affiliation_state",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_detections_for_target(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_all_detections_for_target: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**AllDetectionsForTargetGetOutput**](AllDetectionsForTargetGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attack_checkins_for_implant**
> AttackCheckinsForImplantGetOutput get_attack_checkins_for_implant()



Search attack-checkins-for-implant objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.attack_checkins_for_implant_get_output import AttackCheckinsForImplantGetOutput
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-bart_id",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_attack_checkins_for_implant(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_attack_checkins_for_implant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**AttackCheckinsForImplantGetOutput**](AttackCheckinsForImplantGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attack_implants**
> AttackImplantsGetOutput get_attack_implants()



Search attack-implants objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.attack_implants_get_output import AttackImplantsGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-arch",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_attack_implants(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_attack_implants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**AttackImplantsGetOutput**](AttackImplantsGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attack_interfaces_for_implant**
> AttackInterfacesForImplantGetOutput get_attack_interfaces_for_implant()



Search attack-interfaces-for-implant objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.attack_interfaces_for_implant_get_output import AttackInterfacesForImplantGetOutput
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-address",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_attack_interfaces_for_implant(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_attack_interfaces_for_implant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**AttackInterfacesForImplantGetOutput**](AttackInterfacesForImplantGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attack_redirectors**
> AttackRedirectorsGetOutput get_attack_redirectors()



Search attack-redirectors objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.attack_redirectors_get_output import AttackRedirectorsGetOutput
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-bart_id",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_attack_redirectors(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_attack_redirectors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**AttackRedirectorsGetOutput**](AttackRedirectorsGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attack_runbook**
> AttackRunbookGetOutput get_attack_runbook()



Search attack-runbook objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.attack_runbook_get_output import AttackRunbookGetOutput
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-comment",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_attack_runbook(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_attack_runbook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**AttackRunbookGetOutput**](AttackRunbookGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attack_statistics**
> AttackStatisticsGetOutput get_attack_statistics()



Search attack-statistics objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.attack_statistics_get_output import AttackStatisticsGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-current",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_attack_statistics(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_attack_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**AttackStatisticsGetOutput**](AttackStatisticsGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attack_user_action_descriptions**
> AttackUserActionDescriptionsGetOutput get_attack_user_action_descriptions()



Search attack-user-action-descriptions objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.attack_user_action_descriptions_get_output import AttackUserActionDescriptionsGetOutput
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-action_id",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_attack_user_action_descriptions(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_attack_user_action_descriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**AttackUserActionDescriptionsGetOutput**](AttackUserActionDescriptionsGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attack_user_autoapprove**
> AttackUserAutoapproveGetOutput get_attack_user_autoapprove()



Search attack-user-autoapprove objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.attack_user_autoapprove_get_output import AttackUserAutoapproveGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-approved",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_attack_user_autoapprove(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_attack_user_autoapprove: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**AttackUserAutoapproveGetOutput**](AttackUserAutoapproveGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attack_user_runbook_descriptions**
> AttackUserRunbookDescriptionsGetOutput get_attack_user_runbook_descriptions()



Search attack-user-runbook-descriptions objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.attack_user_runbook_descriptions_get_output import AttackUserRunbookDescriptionsGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-description",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_attack_user_runbook_descriptions(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_attack_user_runbook_descriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**AttackUserRunbookDescriptionsGetOutput**](AttackUserRunbookDescriptionsGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hostname**
> HostnameGetOutput get_hostname()



Search hostname objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.hostname_get_output import HostnameGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-affiliation_state",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_hostname(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_hostname: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**HostnameGetOutput**](HostnameGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hostnames_for_ip**
> HostnamesForIpGetOutput get_hostnames_for_ip()



Search hostnames-for-ip objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.hostnames_for_ip_get_output import HostnamesForIpGetOutput
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-affiliation_state",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_hostnames_for_ip(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_hostnames_for_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**HostnamesForIpGetOutput**](HostnamesForIpGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip**
> IpGetOutput get_ip()



Search ip objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.ip_get_output import IpGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-affiliation_state",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_ip(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**IpGetOutput**](IpGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ips_for_hostname**
> IpsForHostnameGetOutput get_ips_for_hostname()



Search ips-for-hostname objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.ips_for_hostname_get_output import IpsForHostnameGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-affiliation_state",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_ips_for_hostname(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_ips_for_hostname: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**IpsForHostnameGetOutput**](IpsForHostnameGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ips_for_network**
> IpsForNetworkGetOutput get_ips_for_network()



Search ips-for-network objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.ips_for_network_get_output import IpsForNetworkGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-affiliation_state",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_ips_for_network(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_ips_for_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**IpsForNetworkGetOutput**](IpsForNetworkGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ips_for_service**
> IpsForServiceGetOutput get_ips_for_service()



Search ips-for-service objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.ips_for_service_get_output import IpsForServiceGetOutput
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-affiliation_state",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_ips_for_service(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_ips_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**IpsForServiceGetOutput**](IpsForServiceGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network**
> NetworkGetOutput get_network()



Search network objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.network_get_output import NetworkGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-affiliation_state",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_network(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**NetworkGetOutput**](NetworkGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peer**
> PeerGetOutput get_peer()



Search peer objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.peer_get_output import PeerGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-id",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_peer(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_peer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**PeerGetOutput**](PeerGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peer_map**
> PeerMapGetOutput get_peer_map()



Search peer-map objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.peer_map_get_output import PeerMapGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-id",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_peer_map(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_peer_map: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**PeerMapGetOutput**](PeerMapGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> PolicyGetOutput get_policy()



Search policy objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.policy_get_output import PolicyGetOutput
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-actions",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_policy(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**PolicyGetOutput**](PolicyGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ports_for_ip**
> PortsForIpGetOutput get_ports_for_ip()



Search ports-for-ip objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.ports_for_ip_get_output import PortsForIpGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-confidence",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_ports_for_ip(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_ports_for_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**PortsForIpGetOutput**](PortsForIpGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prime**
> PrimeGetOutput get_prime()



Search prime objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.prime_get_output import PrimeGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-first_seen",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_prime(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_prime: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**PrimeGetOutput**](PrimeGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> ReportGetOutput get_report()



Search report objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.report_get_output import ReportGetOutput
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-created",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_report(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**ReportGetOutput**](ReportGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saved_views**
> SavedViewsGetOutput get_saved_views()



Search saved-views objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.saved_views_get_output import SavedViewsGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-created_at",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_saved_views(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_saved_views: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**SavedViewsGetOutput**](SavedViewsGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service**
> ServiceGetOutput get_service()



Search service objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.service_get_output import ServiceGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-applicability",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_service(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**ServiceGetOutput**](ServiceGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_action_metadata**
> ActionMetadataSingleOutput get_single_action_metadata(id)



Get one action-metadata object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.action_metadata_single_output import ActionMetadataSingleOutput
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_action_metadata(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_action_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_action_metadata(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_action_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**ActionMetadataSingleOutput**](ActionMetadataSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_attack_implants**
> AttackImplantsSingleOutput get_single_attack_implants(id)



Get one attack-implants object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.attack_implants_single_output import AttackImplantsSingleOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_attack_implants(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_attack_implants: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_attack_implants(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_attack_implants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**AttackImplantsSingleOutput**](AttackImplantsSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_attack_user_action_descriptions**
> AttackUserActionDescriptionsSingleOutput get_single_attack_user_action_descriptions(id)



Get one attack-user-action-descriptions object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.attack_user_action_descriptions_single_output import AttackUserActionDescriptionsSingleOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_attack_user_action_descriptions(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_attack_user_action_descriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**AttackUserActionDescriptionsSingleOutput**](AttackUserActionDescriptionsSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_attack_user_autoapprove**
> AttackUserAutoapproveSingleOutput get_single_attack_user_autoapprove(id)



Get one attack-user-autoapprove object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.attack_user_autoapprove_single_output import AttackUserAutoapproveSingleOutput
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_attack_user_autoapprove(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_attack_user_autoapprove: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_attack_user_autoapprove(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_attack_user_autoapprove: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**AttackUserAutoapproveSingleOutput**](AttackUserAutoapproveSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_attack_user_runbook_descriptions**
> AttackUserRunbookDescriptionsSingleOutput get_single_attack_user_runbook_descriptions(id)



Get one attack-user-runbook-descriptions object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.attack_user_runbook_descriptions_single_output import AttackUserRunbookDescriptionsSingleOutput
from pprint import pprint
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
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_attack_user_runbook_descriptions(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_attack_user_runbook_descriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**AttackUserRunbookDescriptionsSingleOutput**](AttackUserRunbookDescriptionsSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_detection_for_target**
> SingleDetectionForTargetGetOutput get_single_detection_for_target()



Search single-detection-for-target objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.single_detection_for_target_get_output import SingleDetectionForTargetGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-affiliation_state",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_detection_for_target(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_detection_for_target: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**SingleDetectionForTargetGetOutput**](SingleDetectionForTargetGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_hostname**
> HostnameSingleOutput get_single_hostname(id)



Get one hostname object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.hostname_single_output import HostnameSingleOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_hostname(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_hostname: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_hostname(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_hostname: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**HostnameSingleOutput**](HostnameSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_hostnames_for_ip**
> HostnamesForIpSingleOutput get_single_hostnames_for_ip(id)



Get one hostnames-for-ip object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.hostnames_for_ip_single_output import HostnamesForIpSingleOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_hostnames_for_ip(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_hostnames_for_ip: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_hostnames_for_ip(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_hostnames_for_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**HostnamesForIpSingleOutput**](HostnamesForIpSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_ip**
> IpSingleOutput get_single_ip(id)



Get one ip object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.ip_single_output import IpSingleOutput
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_ip(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_ip: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_ip(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**IpSingleOutput**](IpSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_ips_for_hostname**
> IpsForHostnameSingleOutput get_single_ips_for_hostname(id)



Get one ips-for-hostname object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.ips_for_hostname_single_output import IpsForHostnameSingleOutput
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_ips_for_hostname(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_ips_for_hostname: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_ips_for_hostname(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_ips_for_hostname: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**IpsForHostnameSingleOutput**](IpsForHostnameSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_ips_for_network**
> IpsForNetworkSingleOutput get_single_ips_for_network(id)



Get one ips-for-network object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.ips_for_network_single_output import IpsForNetworkSingleOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_ips_for_network(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_ips_for_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_ips_for_network(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_ips_for_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**IpsForNetworkSingleOutput**](IpsForNetworkSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_ips_for_service**
> IpsForServiceSingleOutput get_single_ips_for_service(id)



Get one ips-for-service object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.ips_for_service_single_output import IpsForServiceSingleOutput
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_ips_for_service(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_ips_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_ips_for_service(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_ips_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**IpsForServiceSingleOutput**](IpsForServiceSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_network**
> NetworkSingleOutput get_single_network(id)



Get one network object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.network_single_output import NetworkSingleOutput
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_network(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_network(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**NetworkSingleOutput**](NetworkSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_peer**
> PeerSingleOutput get_single_peer(id)



Get one peer object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.peer_single_output import PeerSingleOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_peer(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_peer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**PeerSingleOutput**](PeerSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_peer_map**
> PeerMapSingleOutput get_single_peer_map(id)



Get one peer-map object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.peer_map_single_output import PeerMapSingleOutput
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_peer_map(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_peer_map: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_peer_map(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_peer_map: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**PeerMapSingleOutput**](PeerMapSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_ports_for_ip**
> PortsForIpSingleOutput get_single_ports_for_ip(id)



Get one ports-for-ip object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.ports_for_ip_single_output import PortsForIpSingleOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_ports_for_ip(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_ports_for_ip: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_ports_for_ip(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_ports_for_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**PortsForIpSingleOutput**](PortsForIpSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_report**
> ReportSingleOutput get_single_report(id)



Get one report object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.report_single_output import ReportSingleOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_report(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_report(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**ReportSingleOutput**](ReportSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_saved_views**
> SavedViewsSingleOutput get_single_saved_views(id)



Get one saved-views object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.saved_views_single_output import SavedViewsSingleOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_saved_views(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_saved_views: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_saved_views(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_saved_views: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**SavedViewsSingleOutput**](SavedViewsSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_service**
> ServiceSingleOutput get_single_service(id)



Get one service object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.service_single_output import ServiceSingleOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_service(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_service(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**ServiceSingleOutput**](ServiceSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_tagcounts**
> TagcountsSingleOutput get_single_tagcounts(id)



Get one tagcounts object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.tagcounts_single_output import TagcountsSingleOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_tagcounts(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_tagcounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_tagcounts(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_tagcounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**TagcountsSingleOutput**](TagcountsSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_target**
> TargetSingleOutput get_single_target(id)



Get one target object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.target_single_output import TargetSingleOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_target(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_target: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_target(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_target: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**TargetSingleOutput**](TargetSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_user_ap_action_instances**
> UserApActionInstancesSingleOutput get_single_user_ap_action_instances(id)



Get one user-ap-action-instances object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.user_ap_action_instances_single_output import UserApActionInstancesSingleOutput
from pprint import pprint
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
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_user_ap_action_instances(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_user_ap_action_instances: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_user_ap_action_instances(id, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_single_user_ap_action_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**UserApActionInstancesSingleOutput**](UserApActionInstancesSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_social_entity**
> SocialEntityGetOutput get_social_entity()



Search social-entity objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.social_entity_get_output import SocialEntityGetOutput
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-address",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_social_entity(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_social_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**SocialEntityGetOutput**](SocialEntityGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics**
> StatisticsGetOutput get_statistics()



Search statistics objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.statistics_get_output import StatisticsGetOutput
from pprint import pprint
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
    interval = 1 # int, none_type | number of records to skip between responses (optional)
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-id",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_statistics(interval=interval, offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interval** | **int, none_type**| number of records to skip between responses | [optional]
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**StatisticsGetOutput**](StatisticsGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tagcounts**
> TagcountsGetOutput get_tagcounts()



Search tagcounts objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.tagcounts_get_output import TagcountsGetOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-all_count",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_tagcounts(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_tagcounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**TagcountsGetOutput**](TagcountsGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target**
> TargetGetOutput get_target()



Search target objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.target_get_output import TargetGetOutput
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-affiliation_state",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_target(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_target: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**TargetGetOutput**](TargetGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_ap_action_instances**
> UserApActionInstancesGetOutput get_user_ap_action_instances()



Search user-ap-action-instances objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.user_ap_action_instances_get_output import UserApActionInstancesGetOutput
from pprint import pprint
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
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-_dst_ip",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_user_ap_action_instances(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->get_user_ap_action_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**UserApActionInstancesGetOutput**](UserApActionInstancesGetOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hoc_submit**
> Artifactsrc hoc_submit()



Manually upload an artifact

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.artifactsrc import Artifactsrc
from pprint import pprint
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
    filename = "filename_example" # str |  (optional)
    source = "source_example" # str |  (optional)
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.hoc_submit(filename=filename, source=source, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->hoc_submit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  | [optional]
 **source** | **str**|  | [optional]
 **org_id** | **str**|  | [optional]

### Return type

[**Artifactsrc**](Artifactsrc.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hoc_submit_cpio**
> ArtifactsrcMany hoc_submit_cpio()



Manually upload multiple artifacts via cpio archive

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.artifactsrc_many import ArtifactsrcMany
from pprint import pprint
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
    source = "source_example" # str |  (optional)
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.hoc_submit_cpio(source=source, org_id=org_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->hoc_submit_cpio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**|  | [optional]
 **org_id** | **str**|  | [optional]

### Return type

[**ArtifactsrcMany**](ArtifactsrcMany.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **impact_score_groups**
> ImpactScoreGroupOuterResult impact_score_groups()



Return counts of a given entity type grouped by impact score. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.impact_score_group_outer_result import ImpactScoreGroupOuterResult
from randori_api.model.impact_score_entity_req import ImpactScoreEntityReq
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    impact_score_entity_req = ImpactScoreEntityReq(
        entity_type="ip",
        min_first_seen=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # ImpactScoreEntityReq |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.impact_score_groups(impact_score_entity_req=impact_score_entity_req)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->impact_score_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **impact_score_entity_req** | [**ImpactScoreEntityReq**](ImpactScoreEntityReq.md)|  | [optional]

### Return type

[**ImpactScoreGroupOuterResult**](ImpactScoreGroupOuterResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_hostname**
> HostnamePatchOutput patch_hostname()



bulk-patch hostname records

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.hostname_patch_output import HostnamePatchOutput
from randori_api.model.hostname_patch_input import HostnamePatchInput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    hostname_patch_input = HostnamePatchInput(
        data=HostnamePatchInputData(None),
        operations=[
            HostnamePatchInputOperationsInner(None),
        ],
        q=HostnamePatchInputQ(None),
    ) # HostnamePatchInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_hostname(hostname_patch_input=hostname_patch_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_hostname: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname_patch_input** | [**HostnamePatchInput**](HostnamePatchInput.md)|  | [optional]

### Return type

[**HostnamePatchOutput**](HostnamePatchOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_ip**
> IpPatchOutput patch_ip()



bulk-patch ip records

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.ip_patch_output import IpPatchOutput
from randori_api.model.ip_patch_input import IpPatchInput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    ip_patch_input = IpPatchInput(
        data=IpPatchInputData(None),
        operations=[
            HostnamePatchInputOperationsInner(None),
        ],
        q=HostnamePatchInputQ(None),
    ) # IpPatchInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_ip(ip_patch_input=ip_patch_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_patch_input** | [**IpPatchInput**](IpPatchInput.md)|  | [optional]

### Return type

[**IpPatchOutput**](IpPatchOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_network**
> NetworkPatchOutput patch_network()



bulk-patch network records

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.network_patch_input import NetworkPatchInput
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.network_patch_output import NetworkPatchOutput
from pprint import pprint
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
    network_patch_input = NetworkPatchInput(
        data=NetworkPatchInputData(None),
        operations=[
            HostnamePatchInputOperationsInner(None),
        ],
        q=HostnamePatchInputQ(None),
    ) # NetworkPatchInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_network(network_patch_input=network_patch_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_patch_input** | [**NetworkPatchInput**](NetworkPatchInput.md)|  | [optional]

### Return type

[**NetworkPatchOutput**](NetworkPatchOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_single_attack_user_action_descriptions**
> AttackUserActionDescriptionsSingleOutput patch_single_attack_user_action_descriptions(id)



Update fields for the attack-user-action-descriptions object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.attack_user_action_descriptions_single_output import AttackUserActionDescriptionsSingleOutput
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.attack_user_action_descriptions_patch_single_input import AttackUserActionDescriptionsPatchSingleInput
from pprint import pprint
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
    id = "id_example" # str | 
    attack_user_action_descriptions_patch_single_input = AttackUserActionDescriptionsPatchSingleInput(
        data=AttackUserActionDescriptionsPatchSingleInputData(None),
    ) # AttackUserActionDescriptionsPatchSingleInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_single_attack_user_action_descriptions(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_attack_user_action_descriptions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_single_attack_user_action_descriptions(id, attack_user_action_descriptions_patch_single_input=attack_user_action_descriptions_patch_single_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_attack_user_action_descriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **attack_user_action_descriptions_patch_single_input** | [**AttackUserActionDescriptionsPatchSingleInput**](AttackUserActionDescriptionsPatchSingleInput.md)|  | [optional]

### Return type

[**AttackUserActionDescriptionsSingleOutput**](AttackUserActionDescriptionsSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_single_attack_user_autoapprove**
> AttackUserAutoapproveSingleOutput patch_single_attack_user_autoapprove(id)



Update fields for the attack-user-autoapprove object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.attack_user_autoapprove_patch_single_input import AttackUserAutoapprovePatchSingleInput
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.attack_user_autoapprove_single_output import AttackUserAutoapproveSingleOutput
from pprint import pprint
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
    id = "id_example" # str | 
    attack_user_autoapprove_patch_single_input = AttackUserAutoapprovePatchSingleInput(
        data=AttackUserAutoapprovePatchSingleInputData(None),
        org_id="org_id_example",
    ) # AttackUserAutoapprovePatchSingleInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_single_attack_user_autoapprove(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_attack_user_autoapprove: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_single_attack_user_autoapprove(id, attack_user_autoapprove_patch_single_input=attack_user_autoapprove_patch_single_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_attack_user_autoapprove: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **attack_user_autoapprove_patch_single_input** | [**AttackUserAutoapprovePatchSingleInput**](AttackUserAutoapprovePatchSingleInput.md)|  | [optional]

### Return type

[**AttackUserAutoapproveSingleOutput**](AttackUserAutoapproveSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_single_attack_user_runbook_descriptions**
> AttackUserRunbookDescriptionsSingleOutput patch_single_attack_user_runbook_descriptions(id)



Update fields for the attack-user-runbook-descriptions object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.attack_user_runbook_descriptions_patch_single_input import AttackUserRunbookDescriptionsPatchSingleInput
from randori_api.model.attack_user_runbook_descriptions_single_output import AttackUserRunbookDescriptionsSingleOutput
from pprint import pprint
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
    id = "id_example" # str | 
    attack_user_runbook_descriptions_patch_single_input = AttackUserRunbookDescriptionsPatchSingleInput(
        data=AttackUserRunbookDescriptionsPatchSingleInputData(None),
    ) # AttackUserRunbookDescriptionsPatchSingleInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_single_attack_user_runbook_descriptions(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_attack_user_runbook_descriptions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_single_attack_user_runbook_descriptions(id, attack_user_runbook_descriptions_patch_single_input=attack_user_runbook_descriptions_patch_single_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_attack_user_runbook_descriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **attack_user_runbook_descriptions_patch_single_input** | [**AttackUserRunbookDescriptionsPatchSingleInput**](AttackUserRunbookDescriptionsPatchSingleInput.md)|  | [optional]

### Return type

[**AttackUserRunbookDescriptionsSingleOutput**](AttackUserRunbookDescriptionsSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_single_peer_map**
> PeerMapSingleOutput patch_single_peer_map(id)



Update fields for the peer-map object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.peer_map_patch_single_input import PeerMapPatchSingleInput
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.peer_map_single_output import PeerMapSingleOutput
from pprint import pprint
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
    id = "id_example" # str | 
    peer_map_patch_single_input = PeerMapPatchSingleInput(
        data=PeerMapPatchSingleInputData(None),
        org_id="org_id_example",
    ) # PeerMapPatchSingleInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_single_peer_map(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_peer_map: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_single_peer_map(id, peer_map_patch_single_input=peer_map_patch_single_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_peer_map: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **peer_map_patch_single_input** | [**PeerMapPatchSingleInput**](PeerMapPatchSingleInput.md)|  | [optional]

### Return type

[**PeerMapSingleOutput**](PeerMapSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_single_policy**
> PolicySingleOutput patch_single_policy(id)



Update fields for the policy object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.policy_patch_single_input import PolicyPatchSingleInput
from randori_api.model.policy_single_output import PolicySingleOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    id = "id_example" # str | 
    policy_patch_single_input = PolicyPatchSingleInput(
        data=PolicyPatchSingleInputData(None),
        org_id="org_id_example",
    ) # PolicyPatchSingleInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_single_policy(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_single_policy(id, policy_patch_single_input=policy_patch_single_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **policy_patch_single_input** | [**PolicyPatchSingleInput**](PolicyPatchSingleInput.md)|  | [optional]

### Return type

[**PolicySingleOutput**](PolicySingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_single_saved_views**
> SavedViewsSingleOutput patch_single_saved_views(id)



Update fields for the saved-views object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.saved_views_single_output import SavedViewsSingleOutput
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.saved_views_patch_single_input import SavedViewsPatchSingleInput
from pprint import pprint
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
    id = "id_example" # str | 
    saved_views_patch_single_input = SavedViewsPatchSingleInput(
        data=SavedViewsPatchSingleInputData(None),
        org_id="org_id_example",
    ) # SavedViewsPatchSingleInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_single_saved_views(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_saved_views: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_single_saved_views(id, saved_views_patch_single_input=saved_views_patch_single_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_saved_views: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **saved_views_patch_single_input** | [**SavedViewsPatchSingleInput**](SavedViewsPatchSingleInput.md)|  | [optional]

### Return type

[**SavedViewsSingleOutput**](SavedViewsSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_single_user_ap_action_instances**
> UserApActionInstancesSingleOutput patch_single_user_ap_action_instances(id)



Update fields for the user-ap-action-instances object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.user_ap_action_instances_patch_single_input import UserApActionInstancesPatchSingleInput
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.user_ap_action_instances_single_output import UserApActionInstancesSingleOutput
from pprint import pprint
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
    id = "id_example" # str | 
    user_ap_action_instances_patch_single_input = UserApActionInstancesPatchSingleInput(
        data=UserApActionInstancesPatchSingleInputData(None),
        org_id="org_id_example",
    ) # UserApActionInstancesPatchSingleInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_single_user_ap_action_instances(id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_user_ap_action_instances: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_single_user_ap_action_instances(id, user_ap_action_instances_patch_single_input=user_ap_action_instances_patch_single_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_user_ap_action_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **user_ap_action_instances_patch_single_input** | [**UserApActionInstancesPatchSingleInput**](UserApActionInstancesPatchSingleInput.md)|  | [optional]

### Return type

[**UserApActionInstancesSingleOutput**](UserApActionInstancesSingleOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_social_entity**
> SocialEntityPatchOutput patch_social_entity()



bulk-patch social-entity records

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.social_entity_patch_output import SocialEntityPatchOutput
from randori_api.model.social_entity_patch_input import SocialEntityPatchInput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    social_entity_patch_input = SocialEntityPatchInput(
        data=SocialEntityPatchInputData(None),
        operations=[
            HostnamePatchInputOperationsInner(None),
        ],
        q=HostnamePatchInputQ(None),
    ) # SocialEntityPatchInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_social_entity(social_entity_patch_input=social_entity_patch_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_social_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_entity_patch_input** | [**SocialEntityPatchInput**](SocialEntityPatchInput.md)|  | [optional]

### Return type

[**SocialEntityPatchOutput**](SocialEntityPatchOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_target**
> TargetPatchOutput patch_target()



bulk-patch target records

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.target_patch_output import TargetPatchOutput
from randori_api.model.target_patch_input import TargetPatchInput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    target_patch_input = TargetPatchInput(
        data=TargetPatchInputData(None),
        operations=[
            HostnamePatchInputOperationsInner(None),
        ],
        q=HostnamePatchInputQ(None),
    ) # TargetPatchInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_target(target_patch_input=target_patch_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->patch_target: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_patch_input** | [**TargetPatchInput**](TargetPatchInput.md)|  | [optional]

### Return type

[**TargetPatchOutput**](TargetPatchOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paths**
> PathsOutputSchema paths()



Returns paths from query param to nearest prime entity(s)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.paths_output_schema import PathsOutputSchema
from pprint import pprint
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
    terminal = "terminal_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.paths(terminal=terminal)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->paths: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal** | **str**|  | [optional]

### Return type

[**PathsOutputSchema**](PathsOutputSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_attack_user_action_descriptions**
> AttackUserActionDescriptionsPostOutput post_attack_user_action_descriptions()



Add new attack-user-action-descriptions objects

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.attack_user_action_descriptions_post_input import AttackUserActionDescriptionsPostInput
from randori_api.model.attack_user_action_descriptions_post_output import AttackUserActionDescriptionsPostOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    attack_user_action_descriptions_post_input = AttackUserActionDescriptionsPostInput(
        data=[
            AttackUserActionDescriptionsModelIn(
                action_id="action_id_example",
                description="description_example",
                id="id_example",
                name="name_example",
                template="template_example",
            ),
        ],
    ) # AttackUserActionDescriptionsPostInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_attack_user_action_descriptions(attack_user_action_descriptions_post_input=attack_user_action_descriptions_post_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->post_attack_user_action_descriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attack_user_action_descriptions_post_input** | [**AttackUserActionDescriptionsPostInput**](AttackUserActionDescriptionsPostInput.md)|  | [optional]

### Return type

[**AttackUserActionDescriptionsPostOutput**](AttackUserActionDescriptionsPostOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_attack_user_autoapprove**
> AttackUserAutoapprovePostOutput post_attack_user_autoapprove()



Add new attack-user-autoapprove objects

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.attack_user_autoapprove_post_output import AttackUserAutoapprovePostOutput
from randori_api.model.attack_user_autoapprove_post_input import AttackUserAutoapprovePostInput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    attack_user_autoapprove_post_input = AttackUserAutoapprovePostInput(
        data=[
            AttackUserAutoapproveModelIn(
                approved=True,
                approver="approver_example",
                id="id_example",
                org_id="org_id_example",
                process_definition_id="process_definition_id_example",
                time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
    ) # AttackUserAutoapprovePostInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_attack_user_autoapprove(attack_user_autoapprove_post_input=attack_user_autoapprove_post_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->post_attack_user_autoapprove: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attack_user_autoapprove_post_input** | [**AttackUserAutoapprovePostInput**](AttackUserAutoapprovePostInput.md)|  | [optional]

### Return type

[**AttackUserAutoapprovePostOutput**](AttackUserAutoapprovePostOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_attack_user_runbook_descriptions**
> AttackUserRunbookDescriptionsPostOutput post_attack_user_runbook_descriptions()



Add new attack-user-runbook-descriptions objects

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.attack_user_runbook_descriptions_post_output import AttackUserRunbookDescriptionsPostOutput
from randori_api.model.attack_user_runbook_descriptions_post_input import AttackUserRunbookDescriptionsPostInput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    attack_user_runbook_descriptions_post_input = AttackUserRunbookDescriptionsPostInput(
        data=[
            AttackUserRunbookDescriptionsModelIn(
                description="description_example",
                guidance="guidance_example",
                id="id_example",
                name="name_example",
                objective="objective_example",
                runbook_id="runbook_id_example",
            ),
        ],
    ) # AttackUserRunbookDescriptionsPostInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_attack_user_runbook_descriptions(attack_user_runbook_descriptions_post_input=attack_user_runbook_descriptions_post_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->post_attack_user_runbook_descriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attack_user_runbook_descriptions_post_input** | [**AttackUserRunbookDescriptionsPostInput**](AttackUserRunbookDescriptionsPostInput.md)|  | [optional]

### Return type

[**AttackUserRunbookDescriptionsPostOutput**](AttackUserRunbookDescriptionsPostOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_comment_multi**
> post_comment_multi()



Creates a single comment for multiple entity IDs

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.external_comment_creation_schema import ExternalCommentCreationSchema
from pprint import pprint
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
    external_comment_creation_schema = ExternalCommentCreationSchema(
        action={},
        comment="comment_example",
        entity_ids=[
            "entity_ids_example",
        ],
    ) # ExternalCommentCreationSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.post_comment_multi(external_comment_creation_schema=external_comment_creation_schema)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->post_comment_multi: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_comment_creation_schema** | [**ExternalCommentCreationSchema**](ExternalCommentCreationSchema.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_peer**
> PeerPostOutput post_peer()



Add new peer objects

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.peer_post_input import PeerPostInput
from randori_api.model.peer_post_output import PeerPostOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    peer_post_input = PeerPostInput(
        data=[
            PeerModelIn(
                type="SIZE",
                value="value_example",
            ),
        ],
    ) # PeerPostInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_peer(peer_post_input=peer_post_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->post_peer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peer_post_input** | [**PeerPostInput**](PeerPostInput.md)|  | [optional]

### Return type

[**PeerPostOutput**](PeerPostOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_peer_map**
> PeerMapPostOutput post_peer_map()



Add new peer-map objects

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.peer_map_post_input import PeerMapPostInput
from randori_api.model.peer_map_post_output import PeerMapPostOutput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    peer_map_post_input = PeerMapPostInput(
        data=[
            PeerMapModelIn(
                org_id="org_id_example",
                org_peer_industry="org_peer_industry_example",
                org_peer_size="org_peer_size_example",
            ),
        ],
    ) # PeerMapPostInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_peer_map(peer_map_post_input=peer_map_post_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->post_peer_map: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peer_map_post_input** | [**PeerMapPostInput**](PeerMapPostInput.md)|  | [optional]

### Return type

[**PeerMapPostOutput**](PeerMapPostOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_policy**
> PolicyPostOutput post_policy()



Add new policy objects

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.policy_post_output import PolicyPostOutput
from randori_api.model.policy_post_input import PolicyPostInput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    policy_post_input = PolicyPostInput(
        data=[
            PolicyModelCustomIn(
                actions=[
                    {},
                ],
                entity_types=[
                    "entity_types_example",
                ],
                expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                filter_data={},
                is_active=True,
                name="name_example",
                notes="notes_example",
                sys_period="sys_period_example",
            ),
        ],
    ) # PolicyPostInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_policy(policy_post_input=policy_post_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->post_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_post_input** | [**PolicyPostInput**](PolicyPostInput.md)|  | [optional]

### Return type

[**PolicyPostOutput**](PolicyPostOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_saved_views**
> SavedViewsPostOutput post_saved_views()



Add new saved-views objects

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.saved_views_post_output import SavedViewsPostOutput
from randori_api.model.saved_views_post_input import SavedViewsPostInput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    saved_views_post_input = SavedViewsPostInput(
        data=[
            SavedViewsModelCustomIn(
                description="description_example",
                entity_type="target",
                filter_data={},
                is_favorite=True,
                is_global=True,
                name="name_example",
                sort_data={},
            ),
        ],
    ) # SavedViewsPostInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_saved_views(saved_views_post_input=saved_views_post_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->post_saved_views: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saved_views_post_input** | [**SavedViewsPostInput**](SavedViewsPostInput.md)|  | [optional]

### Return type

[**SavedViewsPostOutput**](SavedViewsPostOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_ap_action_instances**
> UserApActionInstancesPostOutput post_user_ap_action_instances()



Add new user-ap-action-instances objects

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.user_ap_action_instances_post_output import UserApActionInstancesPostOutput
from randori_api.model.user_ap_action_instances_post_input import UserApActionInstancesPostInput
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    user_ap_action_instances_post_input = UserApActionInstancesPostInput(
        data=[
            UserApActionInstancesModelIn(
                dst_ip=[
                    "dst_ip_example",
                ],
                dst_network=[
                    "dst_network_example",
                ],
                src_ip=[
                    "src_ip_example",
                ],
                action_id="action_id_example",
                artifacts_status="artifacts_status_example",
                bart_id="bart_id_example",
                completed=dateutil_parser('1970-01-01T00:00:00.00Z'),
                config={},
                config_hash="config_hash_example",
                deleted=True,
                dst_email=[
                    "dst_email_example",
                ],
                dst_host=[
                    "dst_host_example",
                ],
                dst_mac=[
                    "dst_mac_example",
                ],
                dst_misc=[
                    "dst_misc_example",
                ],
                dst_path=[
                    "dst_path_example",
                ],
                dst_port=[
                    1,
                ],
                id="id_example",
                implant_id="implant_id_example",
                implant_uid="implant_uid_example",
                org_id="org_id_example",
                perspective_metadata={},
                platform_state=1,
                randori_notes="randori_notes_example",
                result="result_example",
                result_hash="result_hash_example",
                runbook_instance_id="runbook_instance_id_example",
                src_email=[
                    "src_email_example",
                ],
                src_host=[
                    "src_host_example",
                ],
                src_mac=[
                    "src_mac_example",
                ],
                src_misc=[
                    "src_misc_example",
                ],
                started=dateutil_parser('1970-01-01T00:00:00.00Z'),
                summary_sha="summary_sha_example",
                trigger={},
                updated=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
    ) # UserApActionInstancesPostInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_user_ap_action_instances(user_ap_action_instances_post_input=user_ap_action_instances_post_input)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->post_user_ap_action_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_ap_action_instances_post_input** | [**UserApActionInstancesPostInput**](UserApActionInstancesPostInput.md)|  | [optional]

### Return type

[**UserApActionInstancesPostOutput**](UserApActionInstancesPostOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **priority_groups**
> PriorityGroupOuterResult priority_groups()



Return counts of a given entity type grouped by priority score ranges. This depends on the requestor to provide sane ranges; ranges are evaluated in order so overlaps wont yield duplicate results.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.priority_group_outer_result import PriorityGroupOuterResult
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.priority_entity_req import PriorityEntityReq
from pprint import pprint
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
    priority_entity_req = PriorityEntityReq(
        entity_type="ip",
        min_first_seen=dateutil_parser('1970-01-01T00:00:00.00Z'),
        prio_ranges=[
            PriorityRange(
                prio_max=0,
                prio_min=0,
                prio_range_name="high",
            ),
        ],
    ) # PriorityEntityReq |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.priority_groups(priority_entity_req=priority_entity_req)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->priority_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **priority_entity_req** | [**PriorityEntityReq**](PriorityEntityReq.md)|  | [optional]

### Return type

[**PriorityGroupOuterResult**](PriorityGroupOuterResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recon_worker_node_ips**
> ReconWorkerNodeIps recon_worker_node_ips(ips)



Return IP addresses supplied, with a boolean value key indicating whether the IP was used by Randori in reconnaissance in (up to) the last 30 days. Note: the IP addresses must be a list of strings that is base64 encoded.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.recon_worker_node_ips import ReconWorkerNodeIps
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    ips = "ips_example" # str | 
    lookbackdays = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.recon_worker_node_ips(ips)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->recon_worker_node_ips: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.recon_worker_node_ips(ips, lookbackdays=lookbackdays)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->recon_worker_node_ips: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ips** | **str**|  |
 **lookbackdays** | **int**|  | [optional]

### Return type

[**ReconWorkerNodeIps**](ReconWorkerNodeIps.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_groups**
> StatusGroupOuterResult status_groups()



Return counts of a given entity type grouped by status.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.status_group_outer_result import StatusGroupOuterResult
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.status_entity_req import StatusEntityReq
from pprint import pprint
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
    status_entity_req = StatusEntityReq(
        entity_type="ip",
        min_first_seen=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # StatusEntityReq |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.status_groups(status_entity_req=status_entity_req)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->status_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_entity_req** | [**StatusEntityReq**](StatusEntityReq.md)|  | [optional]

### Return type

[**StatusGroupOuterResult**](StatusGroupOuterResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag**
> UserTagNameList tag()



Return list of all tags present on system that belong belong to an entity alive in the last day

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.user_tag_name_list import UserTagNameList
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.tag()
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->tag: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UserTagNameList**](UserTagNameList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **target_temptation_groups**
> TargetTemptationGroupOuterResult target_temptation_groups()



Return counts of a given entity type grouped by target temptation score ranges. This depends on the requestor to provide sane ranges; ranges are evaluated in order so overlaps wont yield duplicate results.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.target_temptation_group_outer_result import TargetTemptationGroupOuterResult
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.target_temptation_entity_req import TargetTemptationEntityReq
from pprint import pprint
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
    target_temptation_entity_req = TargetTemptationEntityReq(
        entity_type="ip",
        min_first_seen=dateutil_parser('1970-01-01T00:00:00.00Z'),
        tt_ranges=[
            TargetTemptationRange(
                tt_max=0,
                tt_min=0,
                tt_range_name="high",
            ),
        ],
    ) # TargetTemptationEntityReq |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.target_temptation_groups(target_temptation_entity_req=target_temptation_entity_req)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->target_temptation_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_temptation_entity_req** | [**TargetTemptationEntityReq**](TargetTemptationEntityReq.md)|  | [optional]

### Return type

[**TargetTemptationGroupOuterResult**](TargetTemptationGroupOuterResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_query**
> UserArtifactQuery user_query()



UserQuery

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.user_artifact_query import UserArtifactQuery
from pprint import pprint
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
    id = "id_example" # str |  (optional)
    created = "created_example" # str |  (optional)
    updated = "updated_example" # str |  (optional)
    org_id = "org_id_example" # str |  (optional)
    source = "source_example" # str |  (optional)
    filename = "filename_example" # str |  (optional)
    shasum = "shasum_example" # str |  (optional)
    ingests = 1 # int |  (optional)
    size = 1 # int |  (optional)
    created_start = 1 # int |  (optional)
    created_end = 1 # int |  (optional)
    updated_start = 1 # int |  (optional)
    updated_end = 1 # int |  (optional)
    max_count = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.user_query(id=id, created=created, updated=updated, org_id=org_id, source=source, filename=filename, shasum=shasum, ingests=ingests, size=size, created_start=created_start, created_end=created_end, updated_start=updated_start, updated_end=updated_end, max_count=max_count)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->user_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional]
 **created** | **str**|  | [optional]
 **updated** | **str**|  | [optional]
 **org_id** | **str**|  | [optional]
 **source** | **str**|  | [optional]
 **filename** | **str**|  | [optional]
 **shasum** | **str**|  | [optional]
 **ingests** | **int**|  | [optional]
 **size** | **int**|  | [optional]
 **created_start** | **int**|  | [optional]
 **created_end** | **int**|  | [optional]
 **updated_start** | **int**|  | [optional]
 **updated_end** | **int**|  | [optional]
 **max_count** | **int**|  | [optional]

### Return type

[**UserArtifactQuery**](UserArtifactQuery.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_retrieve**
> user_retrieve(shasum2)



Retrieve

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from pprint import pprint
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
    shasum2 = "shasum_example" # str | 
    shasum = "shasum_example" # str |  (optional)
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.user_retrieve(shasum2)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->user_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.user_retrieve(shasum2, shasum=shasum, org_id=org_id)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->user_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shasum2** | **str**|  |
 **shasum** | **str**|  | [optional]
 **org_id** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uuid_comment_id**
> CommentResponseSchema uuid_comment_id(entity_id, comment_id)



Deletes an existing comment

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.comment_response_schema import CommentResponseSchema
from pprint import pprint
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
    entity_id = "entity_id_example" # str | 
    comment_id = "comment_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.uuid_comment_id(entity_id, comment_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->uuid_comment_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  |
 **comment_id** | **str**|  |

### Return type

[**CommentResponseSchema**](CommentResponseSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uuid_comment_id_0**
> CommentResponseSchema uuid_comment_id_0(entity_id, comment_id)



Updates an existing comment

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api
from randori_api.api import default_api
from randori_api.model.error_schema import ErrorSchema
from randori_api.model.comment_response_schema import CommentResponseSchema
from pprint import pprint
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
    entity_id = "entity_id_example" # str | 
    comment_id = "comment_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.uuid_comment_id_0(entity_id, comment_id)
        pprint(api_response)
    except randori_api.ApiException as e:
        print("Exception when calling DefaultApi->uuid_comment_id_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  |
 **comment_id** | **str**|  |

### Return type

[**CommentResponseSchema**](CommentResponseSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

