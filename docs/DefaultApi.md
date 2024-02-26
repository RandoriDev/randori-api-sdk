# randori_api_sdk.DefaultApi

All URIs are relative to *https://app3.randori.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_affiliation_file**](DefaultApi.md#add_affiliation_file) | **POST** /artifactstore/api/v1/add_affiliation_file | 
[**artifacts**](DefaultApi.md#artifacts) | **GET** /artifactstore/api/v1/activity-log/{activity_instance_id}/artifacts | 
[**change_password**](DefaultApi.md#change_password) | **POST** /auth/api/v1/change-password | 
[**delete_single_saved_views**](DefaultApi.md#delete_single_saved_views) | **DELETE** /recon/api/v1/saved-views/{id} | 
[**features**](DefaultApi.md#features) | **GET** /auth/api/v1/features | 
[**features_org**](DefaultApi.md#features_org) | **GET** /auth/api/v1/features-org | 
[**get_action_metadata**](DefaultApi.md#get_action_metadata) | **GET** /attack/api/v1/user/actions | 
[**get_activity_log**](DefaultApi.md#get_activity_log) | **GET** /recon/api/v1/activity-log | 
[**get_all_detections_for_target**](DefaultApi.md#get_all_detections_for_target) | **GET** /recon/api/v1/all-detections-for-target | 
[**get_attack_checkins_for_implant**](DefaultApi.md#get_attack_checkins_for_implant) | **GET** /attack/api/v1/user/checkins-for-implant | 
[**get_attack_implants**](DefaultApi.md#get_attack_implants) | **GET** /attack/api/v1/user/implants | 
[**get_attack_interfaces_for_implant**](DefaultApi.md#get_attack_interfaces_for_implant) | **GET** /attack/api/v1/user/interfaces-for-implant | 
[**get_attack_redirectors**](DefaultApi.md#get_attack_redirectors) | **GET** /attack/api/v1/user/redirectors | 
[**get_attack_runbook**](DefaultApi.md#get_attack_runbook) | **GET** /attack/api/v1/user/runbooks | 
[**get_attack_statistics**](DefaultApi.md#get_attack_statistics) | **GET** /attack/api/v1/user/statistics | 
[**get_authorization_policy**](DefaultApi.md#get_authorization_policy) | **GET** /recon/api/v1/authorization-policy | 
[**get_entityid_comment**](DefaultApi.md#get_entityid_comment) | **GET** /recon/api/v1/entity/{entity_id}/comment | 
[**get_guidance_file**](DefaultApi.md#get_guidance_file) | **GET** /guidance-articles/api/v1/{tag}.md | 
[**get_hostname**](DefaultApi.md#get_hostname) | **GET** /recon/api/v1/hostname | 
[**get_hostnames_for_ip**](DefaultApi.md#get_hostnames_for_ip) | **GET** /recon/api/v1/hostnames-for-ip | 
[**get_ip**](DefaultApi.md#get_ip) | **GET** /recon/api/v1/ip | 
[**get_ips_for_hostname**](DefaultApi.md#get_ips_for_hostname) | **GET** /recon/api/v1/ips-for-hostname | 
[**get_ips_for_network**](DefaultApi.md#get_ips_for_network) | **GET** /recon/api/v1/ips-for-network | 
[**get_ips_for_service**](DefaultApi.md#get_ips_for_service) | **GET** /recon/api/v1/ips-for-service | 
[**get_network**](DefaultApi.md#get_network) | **GET** /recon/api/v1/network | 
[**get_organization**](DefaultApi.md#get_organization) | **GET** /auth/api/v1/organization | 
[**get_policy**](DefaultApi.md#get_policy) | **GET** /recon/api/v1/policy | 
[**get_ports_for_ip**](DefaultApi.md#get_ports_for_ip) | **GET** /recon/api/v1/ports-for-ip | 
[**get_preferences**](DefaultApi.md#get_preferences) | **GET** /auth/api/v1/preferences | 
[**get_saved_views**](DefaultApi.md#get_saved_views) | **GET** /recon/api/v1/saved-views | 
[**get_service**](DefaultApi.md#get_service) | **GET** /recon/api/v1/service | 
[**get_single_action_metadata**](DefaultApi.md#get_single_action_metadata) | **GET** /attack/api/v1/user/actions/{id} | 
[**get_single_activity_log**](DefaultApi.md#get_single_activity_log) | **GET** /recon/api/v1/activity-log/{id} | 
[**get_single_attack_implants**](DefaultApi.md#get_single_attack_implants) | **GET** /attack/api/v1/user/implants/{id} | 
[**get_single_detection_for_target**](DefaultApi.md#get_single_detection_for_target) | **GET** /recon/api/v1/single-detection-for-target | 
[**get_single_hostname**](DefaultApi.md#get_single_hostname) | **GET** /recon/api/v1/hostname/{id} | 
[**get_single_hostnames_for_ip**](DefaultApi.md#get_single_hostnames_for_ip) | **GET** /recon/api/v1/hostnames-for-ip/{id} | 
[**get_single_ip**](DefaultApi.md#get_single_ip) | **GET** /recon/api/v1/ip/{id} | 
[**get_single_ips_for_hostname**](DefaultApi.md#get_single_ips_for_hostname) | **GET** /recon/api/v1/ips-for-hostname/{id} | 
[**get_single_ips_for_network**](DefaultApi.md#get_single_ips_for_network) | **GET** /recon/api/v1/ips-for-network/{id} | 
[**get_single_ips_for_service**](DefaultApi.md#get_single_ips_for_service) | **GET** /recon/api/v1/ips-for-service/{id} | 
[**get_single_network**](DefaultApi.md#get_single_network) | **GET** /recon/api/v1/network/{id} | 
[**get_single_organization**](DefaultApi.md#get_single_organization) | **GET** /auth/api/v1/organization/{id} | 
[**get_single_ports_for_ip**](DefaultApi.md#get_single_ports_for_ip) | **GET** /recon/api/v1/ports-for-ip/{id} | 
[**get_single_saved_views**](DefaultApi.md#get_single_saved_views) | **GET** /recon/api/v1/saved-views/{id} | 
[**get_single_service**](DefaultApi.md#get_single_service) | **GET** /recon/api/v1/service/{id} | 
[**get_single_tagcounts**](DefaultApi.md#get_single_tagcounts) | **GET** /recon/api/v1/tagcounts/{id} | 
[**get_single_target**](DefaultApi.md#get_single_target) | **GET** /recon/api/v1/target/{id} | 
[**get_single_user**](DefaultApi.md#get_single_user) | **GET** /auth/api/v1/user/{id} | 
[**get_social_entity**](DefaultApi.md#get_social_entity) | **GET** /recon/api/v1/social-entity | 
[**get_statistics**](DefaultApi.md#get_statistics) | **GET** /recon/api/v1/statistics | 
[**get_tagcounts**](DefaultApi.md#get_tagcounts) | **GET** /recon/api/v1/tagcounts | 
[**get_target**](DefaultApi.md#get_target) | **GET** /recon/api/v1/target | 
[**get_user**](DefaultApi.md#get_user) | **GET** /auth/api/v1/user | 
[**login**](DefaultApi.md#login) | **POST** /auth/api/v1/login | 
[**login_otp**](DefaultApi.md#login_otp) | **POST** /auth/api/v1/login-otp | 
[**logout**](DefaultApi.md#logout) | **POST** /auth/api/v1/logout | 
[**manual_authorization**](DefaultApi.md#manual_authorization) | **POST** /recon/api/v1/manual-authorization | 
[**mitre_mitigation**](DefaultApi.md#mitre_mitigation) | **GET** /recon/api/v1/mitre/mitigation/{mitre_code} | 
[**mitre_tactic**](DefaultApi.md#mitre_tactic) | **GET** /recon/api/v1/mitre/tactic/{mitre_code} | 
[**mitre_technique**](DefaultApi.md#mitre_technique) | **GET** /recon/api/v1/mitre/technique/{mitre_code} | 
[**org_with_feature**](DefaultApi.md#org_with_feature) | **GET** /auth/api/v1/org_with_feature | 
[**patch_entiityid_commentid**](DefaultApi.md#patch_entiityid_commentid) | **PATCH** /recon/api/v1/entity/{entity_id}/comment/{comment_id} | 
[**patch_hostname**](DefaultApi.md#patch_hostname) | **PATCH** /recon/api/v1/hostname | 
[**patch_ip**](DefaultApi.md#patch_ip) | **PATCH** /recon/api/v1/ip | 
[**patch_network**](DefaultApi.md#patch_network) | **PATCH** /recon/api/v1/network | 
[**patch_single_saved_views**](DefaultApi.md#patch_single_saved_views) | **PATCH** /recon/api/v1/saved-views/{id} | 
[**patch_single_user**](DefaultApi.md#patch_single_user) | **PATCH** /auth/api/v1/user/{id} | 
[**patch_social_entity**](DefaultApi.md#patch_social_entity) | **PATCH** /recon/api/v1/social-entity | 
[**patch_target**](DefaultApi.md#patch_target) | **PATCH** /recon/api/v1/target | 
[**paths**](DefaultApi.md#paths) | **GET** /recon/api/v1/paths | 
[**permission_group_types**](DefaultApi.md#permission_group_types) | **GET** /auth/api/v1/permission-group-types | 
[**permission_groups_read**](DefaultApi.md#permission_groups_read) | **GET** /auth/api/v1/permission-groups | 
[**post_comment_multi**](DefaultApi.md#post_comment_multi) | **POST** /recon/api/v1/comment | 
[**post_entity_comment**](DefaultApi.md#post_entity_comment) | **POST** /recon/api/v1/entity/{entity_id}/comment | 
[**post_saved_views**](DefaultApi.md#post_saved_views) | **POST** /recon/api/v1/saved-views | 
[**recon_worker_node_ips**](DefaultApi.md#recon_worker_node_ips) | **GET** /recon/api/v1/recon-worker-node-ips | 
[**renew**](DefaultApi.md#renew) | **POST** /auth/api/v1/renew | 
[**renew_api_token**](DefaultApi.md#renew_api_token) | **POST** /auth/api/v1/renew-api-token | 
[**tag**](DefaultApi.md#tag) | **GET** /recon/api/v1/tag | 
[**uuid_artifactsource_uuid**](DefaultApi.md#uuid_artifactsource_uuid) | **GET** /artifactstore/api/v1/retrieve-artifact/{artifactsource_uuid} | 
[**uuid_comment_id**](DefaultApi.md#uuid_comment_id) | **DELETE** /recon/api/v1/entity/{entity_id}/comment/{comment_id} | 
[**validate**](DefaultApi.md#validate) | **POST** /auth/api/v1/validate | 
[**validate_user_jwt**](DefaultApi.md#validate_user_jwt) | **GET** /auth/api/v1/validate | 


# **add_affiliation_file**
> add_affiliation_file()



Add a file of missing affiliations for an organization

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.add_affiliation_file()
    except randori_api_sdk.ApiException as e:
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

# **artifacts**
> ArtifactForActivityResponseCollectionSchema artifacts(activity_instance_id)



This returns all renderable artifacts for an activity instance

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.artifact_for_activity_response_collection_schema import ArtifactForActivityResponseCollectionSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    activity_instance_id = "activity_instance_id_example" # str | 
    offset = 1 # int |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.artifacts(activity_instance_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->artifacts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.artifacts(activity_instance_id, offset=offset, limit=limit)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->artifacts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_instance_id** | **str**|  |
 **offset** | **int**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**ArtifactForActivityResponseCollectionSchema**](ArtifactForActivityResponseCollectionSchema.md)

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

# **change_password**
> DefaultOutputSchema change_password()



Change the password for the jwt user.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.default_output_schema import DefaultOutputSchema
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.password_change_schema import PasswordChangeSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    password_change_schema = PasswordChangeSchema(
        new_password="new_password_example",
        old_password="old_password_example",
    ) # PasswordChangeSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.change_password(password_change_schema=password_change_schema)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->change_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_change_schema** | [**PasswordChangeSchema**](PasswordChangeSchema.md)|  | [optional]

### Return type

[**DefaultOutputSchema**](DefaultOutputSchema.md)

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

# **delete_single_saved_views**
> delete_single_saved_views(id)



Remove the saved-views object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.saved_views_single_input import SavedViewsSingleInput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    saved_views_single_input = SavedViewsSingleInput(
        org_id="org_id_example",
    ) # SavedViewsSingleInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_single_saved_views(id)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->delete_single_saved_views: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.delete_single_saved_views(id, saved_views_single_input=saved_views_single_input)
    except randori_api_sdk.ApiException as e:
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

# **features**
> FeatureResponseCollection features()



Retrieve defined features.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.feature_response_collection import FeatureResponseCollection
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    feature_names = [
        "feature_names_example",
    ] # [str] |  (optional)
    feature_types = [
        "feature_types_example",
    ] # [str] |  (optional)
    active_only = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.features(feature_names=feature_names, feature_types=feature_types, active_only=active_only)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->features: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_names** | **[str]**|  | [optional]
 **feature_types** | **[str]**|  | [optional]
 **active_only** | **bool**|  | [optional]

### Return type

[**FeatureResponseCollection**](FeatureResponseCollection.md)

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

# **features_org**
> OrgFeatureResponseCollection features_org()



Retrieve an organization's features.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.org_feature_response_collection import OrgFeatureResponseCollection
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    names = [
        "names_example",
    ] # [str] |  (optional)
    org_uuid = "org_uuid_example" # str |  (optional)
    active_only = True # bool |  (optional)
    return_all = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.features_org(names=names, org_uuid=org_uuid, active_only=active_only, return_all=return_all)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->features_org: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **[str]**|  | [optional]
 **org_uuid** | **str**|  | [optional]
 **active_only** | **bool**|  | [optional]
 **return_all** | **bool**|  | [optional]

### Return type

[**OrgFeatureResponseCollection**](OrgFeatureResponseCollection.md)

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

# **get_action_metadata**
> ActionMetadataGetOutput get_action_metadata()



Search action-metadata objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.action_metadata_get_output import ActionMetadataGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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

# **get_activity_log**
> ActivityLogGetOutput get_activity_log()



Search activity-log objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.activity_log_get_output import ActivityLogGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-configuration__description",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_activity_log(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_activity_log: %s\n" % e)
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

[**ActivityLogGetOutput**](ActivityLogGetOutput.md)

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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.all_detections_for_target_get_output import AllDetectionsForTargetGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.attack_checkins_for_implant_get_output import AttackCheckinsForImplantGetOutput
from randori_api_sdk.model.error_schema import ErrorSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.attack_implants_get_output import AttackImplantsGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.attack_interfaces_for_implant_get_output import AttackInterfacesForImplantGetOutput
from randori_api_sdk.model.error_schema import ErrorSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.attack_redirectors_get_output import AttackRedirectorsGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.attack_runbook_get_output import AttackRunbookGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.attack_statistics_get_output import AttackStatisticsGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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

# **get_authorization_policy**
> AuthorizationPolicyGetOutput get_authorization_policy()



Search authorization-policy objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.authorization_policy_get_output import AuthorizationPolicyGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
        api_response = api_instance.get_authorization_policy(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_authorization_policy: %s\n" % e)
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

[**AuthorizationPolicyGetOutput**](AuthorizationPolicyGetOutput.md)

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

# **get_entityid_comment**
> CommentResponseCollectionSchema get_entityid_comment(entity_id)



Retrieves a page of comments for a provided entity ID.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.comment_response_collection_schema import CommentResponseCollectionSchema
from randori_api_sdk.model.error_schema import ErrorSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    entity_id = "entity_id_example" # str | 
    offset = 1 # int |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_entityid_comment(entity_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_entityid_comment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_entityid_comment(entity_id, offset=offset, limit=limit)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_entityid_comment: %s\n" % e)
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

# **get_guidance_file**
> get_guidance_file(tag)



Retrieve Randori guidance as markdown by tag

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    tag = "tag_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_guidance_file(tag)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_guidance_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**|  |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hostname**
> HostnameGetOutput get_hostname()



Search hostname objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.hostname_get_output import HostnameGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.hostnames_for_ip_get_output import HostnamesForIpGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.ip_get_output import IpGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.ips_for_hostname_get_output import IpsForHostnameGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.ips_for_network_get_output import IpsForNetworkGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.ips_for_service_get_output import IpsForServiceGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.network_get_output import NetworkGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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

# **get_organization**
> OrganizationGetOutput get_organization()



Search organization objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.organization_get_output import OrganizationGetOutput
from randori_api_sdk.model.error_schema import ErrorSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
        api_response = api_instance.get_organization(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_organization: %s\n" % e)
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

[**OrganizationGetOutput**](OrganizationGetOutput.md)

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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.policy_get_output import PolicyGetOutput
from randori_api_sdk.model.error_schema import ErrorSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.ports_for_ip_get_output import PortsForIpGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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

# **get_preferences**
> PreferenceOutCollection get_preferences()



Retrieve preferences for a user.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.preference_out_collection import PreferenceOutCollection
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    names = [
        "names_example",
    ] # [str] |  (optional)
    group_names = [
        "group_names_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_preferences(names=names, group_names=group_names)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_preferences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **[str]**|  | [optional]
 **group_names** | **[str]**|  | [optional]

### Return type

[**PreferenceOutCollection**](PreferenceOutCollection.md)

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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.saved_views_get_output import SavedViewsGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.service_get_output import ServiceGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.action_metadata_single_output import ActionMetadataSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_action_metadata(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_action_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_action_metadata(id, org_id=org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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

# **get_single_activity_log**
> ActivityLogSingleOutput get_single_activity_log(id)



Get one activity-log object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.activity_log_single_output import ActivityLogSingleOutput
from randori_api_sdk.model.error_schema import ErrorSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_activity_log(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_activity_log: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_activity_log(id, org_id=org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_activity_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **org_id** | **str**|  | [optional]

### Return type

[**ActivityLogSingleOutput**](ActivityLogSingleOutput.md)

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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.attack_implants_single_output import AttackImplantsSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_attack_implants(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_attack_implants: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_attack_implants(id, org_id=org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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

# **get_single_detection_for_target**
> SingleDetectionForTargetGetOutput get_single_detection_for_target()



Search single-detection-for-target objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.single_detection_for_target_get_output import SingleDetectionForTargetGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.hostname_single_output import HostnameSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_hostname(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_hostname: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_hostname(id, org_id=org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.hostnames_for_ip_single_output import HostnamesForIpSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_hostnames_for_ip(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_hostnames_for_ip: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_hostnames_for_ip(id, org_id=org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.ip_single_output import IpSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_ip(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_ip: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_ip(id, org_id=org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.ips_for_hostname_single_output import IpsForHostnameSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_ips_for_hostname(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_ips_for_hostname: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_ips_for_hostname(id, org_id=org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.ips_for_network_single_output import IpsForNetworkSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_ips_for_network(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_ips_for_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_ips_for_network(id, org_id=org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.ips_for_service_single_output import IpsForServiceSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_ips_for_service(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_ips_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_ips_for_service(id, org_id=org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.network_single_output import NetworkSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_network(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_network(id, org_id=org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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

# **get_single_organization**
> OrganizationSingleOutput get_single_organization(id)



Get one organization object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.organization_single_output import OrganizationSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_organization(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_organization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**OrganizationSingleOutput**](OrganizationSingleOutput.md)

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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.ports_for_ip_single_output import PortsForIpSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_ports_for_ip(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_ports_for_ip: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_ports_for_ip(id, org_id=org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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

# **get_single_saved_views**
> SavedViewsSingleOutput get_single_saved_views(id)



Get one saved-views object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.saved_views_single_output import SavedViewsSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_saved_views(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_saved_views: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_saved_views(id, org_id=org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.service_single_output import ServiceSingleOutput
from randori_api_sdk.model.error_schema import ErrorSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_service(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_service(id, org_id=org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.tagcounts_single_output import TagcountsSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_tagcounts(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_tagcounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_tagcounts(id, org_id=org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.target_single_output import TargetSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    org_id = "org_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_target(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_target: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_single_target(id, org_id=org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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

# **get_single_user**
> UserSingleOutput get_single_user(id)



Get one user object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.user_single_output import UserSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_single_user(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_single_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**UserSingleOutput**](UserSingleOutput.md)

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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.social_entity_get_output import SocialEntityGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.statistics_get_output import StatisticsGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.tagcounts_get_output import TagcountsGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.target_get_output import TargetGetOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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

# **get_user**
> UserGetOutput get_user()



Search user objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.user_get_output import UserGetOutput
from randori_api_sdk.model.error_schema import ErrorSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    current_org_only = False # bool |  (optional) if omitted the server will use the default value of False
    offset = 1 # int | offset into avilable records after filtering (optional)
    limit = 1 # int | maximum number of records to return (optional)
    sort = [
        "-created_on",
    ] # [str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
    q = "q_example" # str | base64 encoded jquery querybuilder complex search field (optional)
    reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_user(current_org_only=current_org_only, offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **current_org_only** | **bool**|  | [optional] if omitted the server will use the default value of False
 **offset** | **int**| offset into avilable records after filtering | [optional]
 **limit** | **int**| maximum number of records to return | [optional]
 **sort** | **[str]**| fields in the object to sort by, in order of precedence, minus indicates descending | [optional]
 **q** | **str**| base64 encoded jquery querybuilder complex search field | [optional]
 **reversed_nulls** | **bool**| if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger | [optional]

### Return type

[**UserGetOutput**](UserGetOutput.md)

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

# **login**
> DefaultOutputSchema login()



Login with credentials.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.default_output_schema import DefaultOutputSchema
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.username_password_input_schema import UsernamePasswordInputSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username_password_input_schema = UsernamePasswordInputSchema(
        password="password_example",
        username="username_example",
    ) # UsernamePasswordInputSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.login(username_password_input_schema=username_password_input_schema)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username_password_input_schema** | [**UsernamePasswordInputSchema**](UsernamePasswordInputSchema.md)|  | [optional]

### Return type

[**DefaultOutputSchema**](DefaultOutputSchema.md)

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

# **login_otp**
> DefaultOutputSchema login_otp()



Complete login with the current OTP.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.default_output_schema import DefaultOutputSchema
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.otp_token_input_schema import OtpTokenInputSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    otp_token_input_schema = OtpTokenInputSchema(
        otp="otp_example",
    ) # OtpTokenInputSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.login_otp(otp_token_input_schema=otp_token_input_schema)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->login_otp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otp_token_input_schema** | [**OtpTokenInputSchema**](OtpTokenInputSchema.md)|  | [optional]

### Return type

[**DefaultOutputSchema**](DefaultOutputSchema.md)

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

# **logout**
> DefaultOutputSchema logout()



Logout the current JWT or another JWT owned by the user.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.logout_input_schema import LogoutInputSchema
from randori_api_sdk.model.default_output_schema import DefaultOutputSchema
from randori_api_sdk.model.error_schema import ErrorSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    logout_input_schema = LogoutInputSchema(
        jti="jti_example",
    ) # LogoutInputSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.logout(logout_input_schema=logout_input_schema)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->logout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logout_input_schema** | [**LogoutInputSchema**](LogoutInputSchema.md)|  | [optional]

### Return type

[**DefaultOutputSchema**](DefaultOutputSchema.md)

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

# **manual_authorization**
> manual_authorization()



Given a list of detection uuids and an action, will apply that action to those dections

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.manual_authorization_request import ManualAuthorizationRequest
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    manual_authorization_request = ManualAuthorizationRequest(
        action="action_example",
        detection_ids=[
            "detection_ids_example",
        ],
    ) # ManualAuthorizationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.manual_authorization(manual_authorization_request=manual_authorization_request)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->manual_authorization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_authorization_request** | [**ManualAuthorizationRequest**](ManualAuthorizationRequest.md)|  | [optional]

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

# **mitre_mitigation**
> MitreMitigation mitre_mitigation(mitre_code)



Given a valid mitre mitigation code, will return details about that mitigation

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.mitre_mitigation import MitreMitigation
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    mitre_code = "mitre_code_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.mitre_mitigation(mitre_code)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->mitre_mitigation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mitre_code** | **str**|  |

### Return type

[**MitreMitigation**](MitreMitigation.md)

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

# **mitre_tactic**
> MitreTactic mitre_tactic(mitre_code)



Given a valid mitre tactic code, will return details about that tactic

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.mitre_tactic import MitreTactic
from randori_api_sdk.model.error_schema import ErrorSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    mitre_code = "mitre_code_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.mitre_tactic(mitre_code)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->mitre_tactic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mitre_code** | **str**|  |

### Return type

[**MitreTactic**](MitreTactic.md)

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

# **mitre_technique**
> MitreTechnique mitre_technique(mitre_code)



Given a valid mitre technique code, will return details about that technique

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.mitre_technique import MitreTechnique
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    mitre_code = "mitre_code_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.mitre_technique(mitre_code)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->mitre_technique: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mitre_code** | **str**|  |

### Return type

[**MitreTechnique**](MitreTechnique.md)

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

# **org_with_feature**
> OrgWithFeatureResponseCollection org_with_feature(feature_name)



Retrieve organization with active features.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.org_with_feature_response_collection import OrgWithFeatureResponseCollection
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    feature_name = "feature_name_example" # str | 
    org_list = [
        "org_list_example",
    ] # [str], none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.org_with_feature(feature_name)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->org_with_feature: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.org_with_feature(feature_name, org_list=org_list)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->org_with_feature: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_name** | **str**|  |
 **org_list** | **[str], none_type**|  | [optional]

### Return type

[**OrgWithFeatureResponseCollection**](OrgWithFeatureResponseCollection.md)

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

# **patch_entiityid_commentid**
> CommentResponseSchema patch_entiityid_commentid(comment_id, entity_id)



Updates an existing comment

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.comment_response_schema import CommentResponseSchema
from randori_api_sdk.model.comment_creation_schema import CommentCreationSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    comment_id = "comment_id_example" # str | 
    entity_id = "entity_id_example" # str | 
    comment_creation_schema = CommentCreationSchema(
        comment="comment_example",
    ) # CommentCreationSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_entiityid_commentid(comment_id, entity_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->patch_entiityid_commentid: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_entiityid_commentid(comment_id, entity_id, comment_creation_schema=comment_creation_schema)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->patch_entiityid_commentid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  |
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

# **patch_hostname**
> HostnamePatchOutput patch_hostname()



bulk-patch hostname records

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.hostname_patch_input import HostnamePatchInput
from randori_api_sdk.model.hostname_patch_output import HostnamePatchOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    hostname_patch_input = HostnamePatchInput(
        data=None,
        operations=[
            None,
        ],
        q=None,
    ) # HostnamePatchInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_hostname(hostname_patch_input=hostname_patch_input)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.ip_patch_output import IpPatchOutput
from randori_api_sdk.model.ip_patch_input import IpPatchInput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    ip_patch_input = IpPatchInput(
        data=None,
        operations=[
            None,
        ],
        q=None,
    ) # IpPatchInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_ip(ip_patch_input=ip_patch_input)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.network_patch_input import NetworkPatchInput
from randori_api_sdk.model.network_patch_output import NetworkPatchOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    network_patch_input = NetworkPatchInput(
        data=None,
        operations=[
            None,
        ],
        q=None,
    ) # NetworkPatchInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_network(network_patch_input=network_patch_input)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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

# **patch_single_saved_views**
> SavedViewsSingleOutput patch_single_saved_views(id)



Update fields for the saved-views object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.saved_views_single_output import SavedViewsSingleOutput
from randori_api_sdk.model.saved_views_patch_single_input import SavedViewsPatchSingleInput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    saved_views_patch_single_input = SavedViewsPatchSingleInput(
        data=None,
        org_id="org_id_example",
    ) # SavedViewsPatchSingleInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_single_saved_views(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_saved_views: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_single_saved_views(id, saved_views_patch_single_input=saved_views_patch_single_input)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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

# **patch_single_user**
> UserSingleOutput patch_single_user(id)



Update fields for the user object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.user_patch_single_input import UserPatchSingleInput
from randori_api_sdk.model.user_single_output import UserSingleOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 
    user_patch_single_input = UserPatchSingleInput(
        confirmed_password="confirmed_password_example",
        data=None,
    ) # UserPatchSingleInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_single_user(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_single_user(id, user_patch_single_input=user_patch_single_input)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->patch_single_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **user_patch_single_input** | [**UserPatchSingleInput**](UserPatchSingleInput.md)|  | [optional]

### Return type

[**UserSingleOutput**](UserSingleOutput.md)

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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.social_entity_patch_input import SocialEntityPatchInput
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.social_entity_patch_output import SocialEntityPatchOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    social_entity_patch_input = SocialEntityPatchInput(
        data=None,
        operations=[
            None,
        ],
        q=None,
    ) # SocialEntityPatchInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_social_entity(social_entity_patch_input=social_entity_patch_input)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.target_patch_input import TargetPatchInput
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.target_patch_output import TargetPatchOutput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    target_patch_input = TargetPatchInput(
        data=None,
        operations=[
            None,
        ],
        q=None,
    ) # TargetPatchInput |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_target(target_patch_input=target_patch_input)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.paths_output_schema import PathsOutputSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    terminal = "terminal_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.paths(terminal=terminal)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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

# **permission_group_types**
> PermissionGroupsInfo permission_group_types()



Retrieve valid permission group types.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.permission_groups_info import PermissionGroupsInfo
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.permission_group_types()
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->permission_group_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PermissionGroupsInfo**](PermissionGroupsInfo.md)

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

# **permission_groups_read**
> PermissionGroup permission_groups_read(target_user_id)



Retrieve permission groups for a user in the currently viewed organization.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.permission_group import PermissionGroup
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    target_user_id = "target_user_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.permission_groups_read(target_user_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->permission_groups_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_user_id** | **str**|  |

### Return type

[**PermissionGroup**](PermissionGroup.md)

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

# **post_comment_multi**
> post_comment_multi()



Creates a single comment for multiple entity IDs

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.external_comment_creation_schema import ExternalCommentCreationSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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

# **post_entity_comment**
> CommentResponseSchema post_entity_comment(entity_id)



Creates a single comment for a provided entity ID.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.comment_response_schema import CommentResponseSchema
from randori_api_sdk.model.comment_creation_schema import CommentCreationSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    entity_id = "entity_id_example" # str | 
    comment_creation_schema = CommentCreationSchema(
        comment="comment_example",
    ) # CommentCreationSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_entity_comment(entity_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->post_entity_comment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_entity_comment(entity_id, comment_creation_schema=comment_creation_schema)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->post_entity_comment: %s\n" % e)
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

# **post_saved_views**
> SavedViewsPostOutput post_saved_views()



Add new saved-views objects

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.saved_views_post_output import SavedViewsPostOutput
from randori_api_sdk.model.saved_views_post_input import SavedViewsPostInput
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
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
    except randori_api_sdk.ApiException as e:
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

# **recon_worker_node_ips**
> ReconWorkerNodeIps recon_worker_node_ips(ips)



Return IP addresses supplied, with a boolean value key indicating whether the IP was used by Randori in reconnaissance in (up to) the last 30 days. Note: the IP addresses must be a list of strings that is base64 encoded.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.recon_worker_node_ips import ReconWorkerNodeIps
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    ips = "ips_example" # str | 
    lookbackdays = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.recon_worker_node_ips(ips)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->recon_worker_node_ips: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.recon_worker_node_ips(ips, lookbackdays=lookbackdays)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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

# **renew**
> DefaultOutputSchema renew()



Renew the user token if it is valid

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.logout_input_schema import LogoutInputSchema
from randori_api_sdk.model.default_output_schema import DefaultOutputSchema
from randori_api_sdk.model.error_schema import ErrorSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    logout_input_schema = LogoutInputSchema(
        jti="jti_example",
    ) # LogoutInputSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.renew(logout_input_schema=logout_input_schema)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->renew: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logout_input_schema** | [**LogoutInputSchema**](LogoutInputSchema.md)|  | [optional]

### Return type

[**DefaultOutputSchema**](DefaultOutputSchema.md)

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

# **renew_api_token**
> renew_api_token()



Invalidates current session of an API token, and clones it into a new token/session. A way to rotate an API token value without changing anything else about it

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.renew_api_token()
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->renew_api_token: %s\n" % e)
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

# **tag**
> UserTagNameList tag()



Return list of all tags present on system that belong belong to an entity alive in the last day

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.user_tag_name_list import UserTagNameList
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.tag()
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
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

# **uuid_artifactsource_uuid**
> uuid_artifactsource_uuid(artifactsource_uuid)



Returns the raw artifact for the given artifact instance id provided

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    artifactsource_uuid = "artifactsource_uuid_example" # str | 
    activity_instance_id = "activity_instance_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.uuid_artifactsource_uuid(artifactsource_uuid)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->uuid_artifactsource_uuid: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.uuid_artifactsource_uuid(artifactsource_uuid, activity_instance_id=activity_instance_id)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->uuid_artifactsource_uuid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactsource_uuid** | **str**|  |
 **activity_instance_id** | **str**|  | [optional]

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
> CommentResponseSchema uuid_comment_id(comment_id, entity_id)



Deletes an existing comment

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.comment_response_schema import CommentResponseSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    comment_id = "comment_id_example" # str | 
    entity_id = "entity_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.uuid_comment_id(comment_id, entity_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->uuid_comment_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  |
 **entity_id** | **str**|  |

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

# **validate**
> TokenOutputSchema validate()



Validate provided tokens

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.token_output_schema import TokenOutputSchema
from randori_api_sdk.model.error_schema import ErrorSchema
from randori_api_sdk.model.token_input_schema import TokenInputSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    token_input_schema = TokenInputSchema(
        token="token_example",
    ) # TokenInputSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.validate(token_input_schema=token_input_schema)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->validate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_input_schema** | [**TokenInputSchema**](TokenInputSchema.md)|  | [optional]

### Return type

[**TokenOutputSchema**](TokenOutputSchema.md)

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

# **validate_user_jwt**
> TokenOutputSchema validate_user_jwt()



Validate user token from auth

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import default_api
from randori_api_sdk.model.token_output_schema import TokenOutputSchema
from randori_api_sdk.model.error_schema import ErrorSchema
from pprint import pprint
# Defining the host is optional and defaults to https://app3.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app3.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.validate_user_jwt()
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling DefaultApi->validate_user_jwt: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenOutputSchema**](TokenOutputSchema.md)

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

