# randori_api.DefaultApi

All URIs are relative to *https://alpha.randori.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_detections_for_target**](DefaultApi.md#get_all_detections_for_target) | **GET** /recon/api/v1/all-detections-for-target | 
[**get_hostname**](DefaultApi.md#get_hostname) | **GET** /recon/api/v1/hostname | 
[**get_hostnames_for_ip**](DefaultApi.md#get_hostnames_for_ip) | **GET** /recon/api/v1/hostnames-for-ip | 
[**get_ip**](DefaultApi.md#get_ip) | **GET** /recon/api/v1/ip | 
[**get_ips_for_hostname**](DefaultApi.md#get_ips_for_hostname) | **GET** /recon/api/v1/ips-for-hostname | 
[**get_ips_for_network**](DefaultApi.md#get_ips_for_network) | **GET** /recon/api/v1/ips-for-network | 
[**get_ips_for_service**](DefaultApi.md#get_ips_for_service) | **GET** /recon/api/v1/ips-for-service | 
[**get_network**](DefaultApi.md#get_network) | **GET** /recon/api/v1/network | 
[**get_ports_for_ip**](DefaultApi.md#get_ports_for_ip) | **GET** /recon/api/v1/ports-for-ip | 
[**get_service**](DefaultApi.md#get_service) | **GET** /recon/api/v1/service | 
[**get_single_detection_for_target**](DefaultApi.md#get_single_detection_for_target) | **GET** /recon/api/v1/single-detection-for-target | 
[**get_single_hostname**](DefaultApi.md#get_single_hostname) | **GET** /recon/api/v1/hostname/{id} | 
[**get_single_hostnames_for_ip**](DefaultApi.md#get_single_hostnames_for_ip) | **GET** /recon/api/v1/hostnames-for-ip/{id} | 
[**get_single_ip**](DefaultApi.md#get_single_ip) | **GET** /recon/api/v1/ip/{id} | 
[**get_single_ips_for_hostname**](DefaultApi.md#get_single_ips_for_hostname) | **GET** /recon/api/v1/ips-for-hostname/{id} | 
[**get_single_ips_for_network**](DefaultApi.md#get_single_ips_for_network) | **GET** /recon/api/v1/ips-for-network/{id} | 
[**get_single_ips_for_service**](DefaultApi.md#get_single_ips_for_service) | **GET** /recon/api/v1/ips-for-service/{id} | 
[**get_single_network**](DefaultApi.md#get_single_network) | **GET** /recon/api/v1/network/{id} | 
[**get_single_ports_for_ip**](DefaultApi.md#get_single_ports_for_ip) | **GET** /recon/api/v1/ports-for-ip/{id} | 
[**get_single_service**](DefaultApi.md#get_single_service) | **GET** /recon/api/v1/service/{id} | 
[**get_single_tagcounts**](DefaultApi.md#get_single_tagcounts) | **GET** /recon/api/v1/tagcounts/{id} | 
[**get_single_target**](DefaultApi.md#get_single_target) | **GET** /recon/api/v1/target/{id} | 
[**get_social_entity**](DefaultApi.md#get_social_entity) | **GET** /recon/api/v1/social-entity | 
[**get_statistics**](DefaultApi.md#get_statistics) | **GET** /recon/api/v1/statistics | 
[**get_tagcounts**](DefaultApi.md#get_tagcounts) | **GET** /recon/api/v1/tagcounts | 
[**get_target**](DefaultApi.md#get_target) | **GET** /recon/api/v1/target | 
[**impact_score_groups**](DefaultApi.md#impact_score_groups) | **POST** /recon/api/v1/impact_score_groups | 
[**patch_hostname**](DefaultApi.md#patch_hostname) | **PATCH** /recon/api/v1/hostname | 
[**patch_ip**](DefaultApi.md#patch_ip) | **PATCH** /recon/api/v1/ip | 
[**patch_network**](DefaultApi.md#patch_network) | **PATCH** /recon/api/v1/network | 
[**patch_social_entity**](DefaultApi.md#patch_social_entity) | **PATCH** /recon/api/v1/social-entity | 
[**patch_target**](DefaultApi.md#patch_target) | **PATCH** /recon/api/v1/target | 
[**paths**](DefaultApi.md#paths) | **GET** /recon/api/v1/paths | 
[**priority_groups**](DefaultApi.md#priority_groups) | **POST** /recon/api/v1/priority_groups | 
[**status_groups**](DefaultApi.md#status_groups) | **POST** /recon/api/v1/status_groups | 
[**tag**](DefaultApi.md#tag) | **GET** /recon/api/v1/tag | 
[**target_temptation_groups**](DefaultApi.md#target_temptation_groups) | **POST** /recon/api/v1/target_temptation_groups | 


# **get_all_detections_for_target**
> AllDetectionsForTargetGetOutput get_all_detections_for_target(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)



Search all-detections-for-target objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    try:
        api_response = api_instance.get_all_detections_for_target(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all_detections_for_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 
 **sort** | [**list[str]**](str.md)| fields in the object to sort by, in order of precedence, minus indicates descending | [optional] 
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

# **get_hostname**
> HostnameGetOutput get_hostname(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)



Search hostname objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    try:
        api_response = api_instance.get_hostname(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_hostname: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 
 **sort** | [**list[str]**](str.md)| fields in the object to sort by, in order of precedence, minus indicates descending | [optional] 
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
> HostnamesForIpGetOutput get_hostnames_for_ip(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)



Search hostnames-for-ip objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    try:
        api_response = api_instance.get_hostnames_for_ip(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_hostnames_for_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 
 **sort** | [**list[str]**](str.md)| fields in the object to sort by, in order of precedence, minus indicates descending | [optional] 
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
> IpGetOutput get_ip(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)



Search ip objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    try:
        api_response = api_instance.get_ip(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 
 **sort** | [**list[str]**](str.md)| fields in the object to sort by, in order of precedence, minus indicates descending | [optional] 
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
> IpsForHostnameGetOutput get_ips_for_hostname(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)



Search ips-for-hostname objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    try:
        api_response = api_instance.get_ips_for_hostname(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_ips_for_hostname: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 
 **sort** | [**list[str]**](str.md)| fields in the object to sort by, in order of precedence, minus indicates descending | [optional] 
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
> IpsForNetworkGetOutput get_ips_for_network(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)



Search ips-for-network objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    try:
        api_response = api_instance.get_ips_for_network(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_ips_for_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 
 **sort** | [**list[str]**](str.md)| fields in the object to sort by, in order of precedence, minus indicates descending | [optional] 
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
> IpsForServiceGetOutput get_ips_for_service(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)



Search ips-for-service objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    try:
        api_response = api_instance.get_ips_for_service(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_ips_for_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 
 **sort** | [**list[str]**](str.md)| fields in the object to sort by, in order of precedence, minus indicates descending | [optional] 
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
> NetworkGetOutput get_network(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)



Search network objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    try:
        api_response = api_instance.get_network(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 
 **sort** | [**list[str]**](str.md)| fields in the object to sort by, in order of precedence, minus indicates descending | [optional] 
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

# **get_ports_for_ip**
> PortsForIpGetOutput get_ports_for_ip(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)



Search ports-for-ip objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    try:
        api_response = api_instance.get_ports_for_ip(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_ports_for_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 
 **sort** | [**list[str]**](str.md)| fields in the object to sort by, in order of precedence, minus indicates descending | [optional] 
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

# **get_service**
> ServiceGetOutput get_service(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)



Search service objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    try:
        api_response = api_instance.get_service(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 
 **sort** | [**list[str]**](str.md)| fields in the object to sort by, in order of precedence, minus indicates descending | [optional] 
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

# **get_single_detection_for_target**
> SingleDetectionForTargetGetOutput get_single_detection_for_target(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)



Search single-detection-for-target objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    try:
        api_response = api_instance.get_single_detection_for_target(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_single_detection_for_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 
 **sort** | [**list[str]**](str.md)| fields in the object to sort by, in order of precedence, minus indicates descending | [optional] 
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
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_single_hostname(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_single_hostname: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_single_hostnames_for_ip(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_single_hostnames_for_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_single_ip(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_single_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_single_ips_for_hostname(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_single_ips_for_hostname: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_single_ips_for_network(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_single_ips_for_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_single_ips_for_service(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_single_ips_for_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_single_network(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_single_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **get_single_ports_for_ip**
> PortsForIpSingleOutput get_single_ports_for_ip(id)



Get one ports-for-ip object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_single_ports_for_ip(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_single_ports_for_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **get_single_service**
> ServiceSingleOutput get_single_service(id)



Get one service object by id

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_single_service(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_single_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_single_tagcounts(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_single_tagcounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_single_target(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_single_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **get_social_entity**
> SocialEntityGetOutput get_social_entity(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)



Search social-entity objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    try:
        api_response = api_instance.get_social_entity(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_social_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 
 **sort** | [**list[str]**](str.md)| fields in the object to sort by, in order of precedence, minus indicates descending | [optional] 
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
> StatisticsGetOutput get_statistics(interval=interval, offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)



Search statistics objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    interval = 56 # int | number of records to skip between responses (optional)
offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    try:
        api_response = api_instance.get_statistics(interval=interval, offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interval** | **int**| number of records to skip between responses | [optional] 
 **offset** | **int**| offset into avilable records after filtering | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 
 **sort** | [**list[str]**](str.md)| fields in the object to sort by, in order of precedence, minus indicates descending | [optional] 
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
> TagcountsGetOutput get_tagcounts(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)



Search tagcounts objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    try:
        api_response = api_instance.get_tagcounts(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_tagcounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 
 **sort** | [**list[str]**](str.md)| fields in the object to sort by, in order of precedence, minus indicates descending | [optional] 
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
> TargetGetOutput get_target(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)



Search target objects with an optional filter

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

    try:
        api_response = api_instance.get_target(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset into avilable records after filtering | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 
 **sort** | [**list[str]**](str.md)| fields in the object to sort by, in order of precedence, minus indicates descending | [optional] 
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

# **impact_score_groups**
> ImpactScoreGroupOuterResult impact_score_groups(impact_score_entity_req=impact_score_entity_req)



Return counts of a given entity type grouped by impact score. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    impact_score_entity_req = randori_api.ImpactScoreEntityReq() # ImpactScoreEntityReq |  (optional)

    try:
        api_response = api_instance.impact_score_groups(impact_score_entity_req=impact_score_entity_req)
        pprint(api_response)
    except ApiException as e:
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
> HostnamePatchOutput patch_hostname(hostname_patch_input=hostname_patch_input)



bulk-patch hostname records

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
  
import json
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint

configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_API_TOKEN_HERE'

data_dict = json.loads('''{
    "impact_score": "Medium",
    "status": "Needs Investigation"
}''')

query = json.loads('''{
    "condition": "OR",
    "rules": [
        {
            "id": "table.id",
            "field": "table.id",
            "type": "object",
            "input": "text",
            "operator": "equal",
            "value": "REPLACE_ME"
        }
    ]
}''')

assert configuration.access_token != 'YOUR_API_TOKEN_HERE', 'API Token is not set.'

assert query['rules'][0]['value'] != 'REPLACE_ME', 'Value of hostname id is not set.'


with randori_api.ApiClient(configuration) as api_client:

    api_instance = randori_api.DefaultApi(api_client)

    hostname_patch_input = randori_api.HostnamePatchInput(data = data_dict, q = query)

    try:
        api_response = api_instance.patch_hostname(hostname_patch_input=hostname_patch_input)
        pprint(api_response)
    except ApiException as e:
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
> IpPatchOutput patch_ip(ip_patch_input=ip_patch_input)



bulk-patch ip records

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    ip_patch_input = randori_api.IpPatchInput() # IpPatchInput |  (optional)

    try:
        api_response = api_instance.patch_ip(ip_patch_input=ip_patch_input)
        pprint(api_response)
    except ApiException as e:
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
> NetworkPatchOutput patch_network(network_patch_input=network_patch_input)



bulk-patch network records

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    network_patch_input = randori_api.NetworkPatchInput() # NetworkPatchInput |  (optional)

    try:
        api_response = api_instance.patch_network(network_patch_input=network_patch_input)
        pprint(api_response)
    except ApiException as e:
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

# **patch_social_entity**
> SocialEntityPatchOutput patch_social_entity(social_entity_patch_input=social_entity_patch_input)



bulk-patch social-entity records

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    social_entity_patch_input = randori_api.SocialEntityPatchInput() # SocialEntityPatchInput |  (optional)

    try:
        api_response = api_instance.patch_social_entity(social_entity_patch_input=social_entity_patch_input)
        pprint(api_response)
    except ApiException as e:
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
> TargetPatchOutput patch_target(target_patch_input=target_patch_input)



bulk-patch target records

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    target_patch_input = randori_api.TargetPatchInput() # TargetPatchInput |  (optional)

    try:
        api_response = api_instance.patch_target(target_patch_input=target_patch_input)
        pprint(api_response)
    except ApiException as e:
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
> PathsOutputSchema paths(terminal=terminal)



Returns paths from query param to nearest prime entity(s)

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    terminal = 'terminal_example' # str |  (optional)

    try:
        api_response = api_instance.paths(terminal=terminal)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal** | [**str**](.md)|  | [optional] 

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

# **priority_groups**
> PriorityGroupOuterResult priority_groups(priority_entity_req=priority_entity_req)



Return counts of a given entity type grouped by priority score ranges. This depends on the requestor to provide sane ranges; ranges are evaluated in order so overlaps wont yield duplicate results.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    priority_entity_req = randori_api.PriorityEntityReq() # PriorityEntityReq |  (optional)

    try:
        api_response = api_instance.priority_groups(priority_entity_req=priority_entity_req)
        pprint(api_response)
    except ApiException as e:
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

# **status_groups**
> StatusGroupOuterResult status_groups(status_entity_req=status_entity_req)



Return counts of a given entity type grouped by status. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    status_entity_req = randori_api.StatusEntityReq() # StatusEntityReq |  (optional)

    try:
        api_response = api_instance.status_groups(status_entity_req=status_entity_req)
        pprint(api_response)
    except ApiException as e:
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
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    
    try:
        api_response = api_instance.tag()
        pprint(api_response)
    except ApiException as e:
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
> TargetTemptationGroupOuterResult target_temptation_groups(target_temptation_entity_req=target_temptation_entity_req)



Return counts of a given entity type grouped by target temptation score ranges. This depends on the requestor to provide sane ranges; ranges are evaluated in order so overlaps wont yield duplicate results.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://alpha.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api.Configuration(
    host = "https://alpha.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with randori_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = randori_api.DefaultApi(api_client)
    target_temptation_entity_req = randori_api.TargetTemptationEntityReq() # TargetTemptationEntityReq |  (optional)

    try:
        api_response = api_instance.target_temptation_groups(target_temptation_entity_req=target_temptation_entity_req)
        pprint(api_response)
    except ApiException as e:
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

