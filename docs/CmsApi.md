# randori_api_sdk.CmsApi

All URIs are relative to *https://app3.randori.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**frontend_edit_activity_configuration**](CmsApi.md#frontend_edit_activity_configuration) | **PATCH** /cms/api/v1/frontend/activity-configurations/{id} | Edit activity configurations
[**frontend_edit_activity_configuration_criteria**](CmsApi.md#frontend_edit_activity_configuration_criteria) | **POST** /cms/api/v1/frontend/activity-configurations/{id}/trigger_criteria/{name} | Edit activity configuration criteria
[**frontend_edit_activity_configuration_parameter**](CmsApi.md#frontend_edit_activity_configuration_parameter) | **POST** /cms/api/v1/frontend/activity-configurations/{id}/parameters/{name}/{kind} | Edit activity configuration parameter
[**frontend_get_activity_configuration**](CmsApi.md#frontend_get_activity_configuration) | **GET** /cms/api/v1/frontend/activity-configurations/{id} | Get activity configurations
[**frontend_get_configuration_criteria**](CmsApi.md#frontend_get_configuration_criteria) | **GET** /cms/api/v1/frontend/activity-configurations/{id}/trigger_criteria/{name} | Get activity configuration criteria
[**frontend_get_configuration_parameter**](CmsApi.md#frontend_get_configuration_parameter) | **GET** /cms/api/v1/frontend/activity-configurations/{id}/parameters/{name}/{kind} | Get activity configuration parameter
[**frontend_list_activity_configuration**](CmsApi.md#frontend_list_activity_configuration) | **GET** /cms/api/v1/frontend/activity-configurations | List activity configurations
[**frontend_list_activity_configuration_criteria**](CmsApi.md#frontend_list_activity_configuration_criteria) | **GET** /cms/api/v1/frontend/activity-configurations/{id}/trigger_criteria | List activity configuration criteria
[**frontend_list_activity_configuration_parameters**](CmsApi.md#frontend_list_activity_configuration_parameters) | **GET** /cms/api/v1/frontend/activity-configurations/{id}/parameters | List activity configuration parameters
[**frontend_list_applicable_activities**](CmsApi.md#frontend_list_applicable_activities) | **GET** /cms/api/v1/frontend/applicable-activities/{entity_type}/{entity_id} | List applicable activity configurations
[**frontend_list_applicable_entities_parameters**](CmsApi.md#frontend_list_applicable_entities_parameters) | **GET** /cms/api/v1/frontend/activity-configurations/:id/applicable-entities/:entity_type | List applicable entities for a configuration
[**frontend_validate_now**](CmsApi.md#frontend_validate_now) | **POST** /cms/api/v1/frontend/validate | Start validate now job


# **frontend_edit_activity_configuration**
> CmspbFrontendSingleConfigurationResponse frontend_edit_activity_configuration(id, cmspb_edit_configuration_request)

Edit activity configurations

Edit activity configurations

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_edit_configuration_request import CmspbEditConfigurationRequest
from randori_api_sdk.model.cmspb_frontend_single_configuration_response import CmspbFrontendSingleConfigurationResponse
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
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Activity Configuration ID
    cmspb_edit_configuration_request = CmspbEditConfigurationRequest(
        changed_fields=[
            CmspbEditConfigurationRequestFields(0),
        ],
        description="description_example",
        enabled=True,
        name="name_example",
        pinned=True,
        settings=CmspbSettings(
            execution_parameters=[
                CmspbSettingsParameter(
                    is_unset=True,
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=StructpbValue(
                        kind=None,
                    ),
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
            matching_criteria=[
                CmspbSettingsCriteria(
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=StructpbValue(
                        kind=None,
                    ),
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
            parameters=[
                CmspbSettingsParameter(
                    is_unset=True,
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=StructpbValue(
                        kind=None,
                    ),
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
            trigger_criteria=[
                CmspbSettingsCriteria(
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=StructpbValue(
                        kind=None,
                    ),
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
        ),
        template_version_id="template_version_id_example",
    ) # CmspbEditConfigurationRequest | Activity Configuration edit request

    # example passing only required values which don't have defaults set
    try:
        # Edit activity configurations
        api_response = api_instance.frontend_edit_activity_configuration(id, cmspb_edit_configuration_request)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_edit_activity_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Activity Configuration ID |
 **cmspb_edit_configuration_request** | [**CmspbEditConfigurationRequest**](CmspbEditConfigurationRequest.md)| Activity Configuration edit request |

### Return type

[**CmspbFrontendSingleConfigurationResponse**](CmspbFrontendSingleConfigurationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **frontend_edit_activity_configuration_criteria**
> CmspbFrontendSingleConfigurationResponse frontend_edit_activity_configuration_criteria(id, name, cms_update_trigger_request)

Edit activity configuration criteria

Edit activity configuration criteria

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cms_update_trigger_request import CmsUpdateTriggerRequest
from randori_api_sdk.model.cmspb_frontend_single_configuration_response import CmspbFrontendSingleConfigurationResponse
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
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Activity Configuration ID
    name = "name_example" # str | Criteria name
    cms_update_trigger_request = CmsUpdateTriggerRequest(
        value=None,
    ) # CmsUpdateTriggerRequest | Criteria edit request

    # example passing only required values which don't have defaults set
    try:
        # Edit activity configuration criteria
        api_response = api_instance.frontend_edit_activity_configuration_criteria(id, name, cms_update_trigger_request)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_edit_activity_configuration_criteria: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Activity Configuration ID |
 **name** | **str**| Criteria name |
 **cms_update_trigger_request** | [**CmsUpdateTriggerRequest**](CmsUpdateTriggerRequest.md)| Criteria edit request |

### Return type

[**CmspbFrontendSingleConfigurationResponse**](CmspbFrontendSingleConfigurationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **frontend_edit_activity_configuration_parameter**
> CmspbFrontendSingleConfigurationResponse frontend_edit_activity_configuration_parameter(id, name, kind, cms_update_parameter_request)

Edit activity configuration parameter

Edit activity configuration parameter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cms_update_parameter_request import CmsUpdateParameterRequest
from randori_api_sdk.model.cmspb_frontend_single_configuration_response import CmspbFrontendSingleConfigurationResponse
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
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Activity Configuration ID
    name = "name_example" # str | Criteria name
    kind = "kind_example" # str | Parameter kind (configuration or execution)
    cms_update_parameter_request = CmsUpdateParameterRequest(
        value=None,
    ) # CmsUpdateParameterRequest | Parameter edit request

    # example passing only required values which don't have defaults set
    try:
        # Edit activity configuration parameter
        api_response = api_instance.frontend_edit_activity_configuration_parameter(id, name, kind, cms_update_parameter_request)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_edit_activity_configuration_parameter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Activity Configuration ID |
 **name** | **str**| Criteria name |
 **kind** | **str**| Parameter kind (configuration or execution) |
 **cms_update_parameter_request** | [**CmsUpdateParameterRequest**](CmsUpdateParameterRequest.md)| Parameter edit request |

### Return type

[**CmspbFrontendSingleConfigurationResponse**](CmspbFrontendSingleConfigurationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **frontend_get_activity_configuration**
> CmspbFrontendSingleConfigurationResponse frontend_get_activity_configuration(id)

Get activity configurations

Get activity configurations

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_frontend_single_configuration_response import CmspbFrontendSingleConfigurationResponse
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
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Activity Configuration ID

    # example passing only required values which don't have defaults set
    try:
        # Get activity configurations
        api_response = api_instance.frontend_get_activity_configuration(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_get_activity_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Activity Configuration ID |

### Return type

[**CmspbFrontendSingleConfigurationResponse**](CmspbFrontendSingleConfigurationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **frontend_get_configuration_criteria**
> CmspbFrontendSingleTriggerResponse frontend_get_configuration_criteria(id, name)

Get activity configuration criteria

Get activity configuration criteria

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_frontend_single_trigger_response import CmspbFrontendSingleTriggerResponse
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
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Activity Configuration ID
    name = "name_example" # str | Criteria name

    # example passing only required values which don't have defaults set
    try:
        # Get activity configuration criteria
        api_response = api_instance.frontend_get_configuration_criteria(id, name)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_get_configuration_criteria: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Activity Configuration ID |
 **name** | **str**| Criteria name |

### Return type

[**CmspbFrontendSingleTriggerResponse**](CmspbFrontendSingleTriggerResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **frontend_get_configuration_parameter**
> CmspbFrontendSingleParameterResponse frontend_get_configuration_parameter(id, name, kind)

Get activity configuration parameter

Get activity configuration parameter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_frontend_single_parameter_response import CmspbFrontendSingleParameterResponse
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
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Activity Configuration ID
    name = "name_example" # str | Criteria name
    kind = "kind_example" # str | Parameter kind (configuration or execution)

    # example passing only required values which don't have defaults set
    try:
        # Get activity configuration parameter
        api_response = api_instance.frontend_get_configuration_parameter(id, name, kind)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_get_configuration_parameter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Activity Configuration ID |
 **name** | **str**| Criteria name |
 **kind** | **str**| Parameter kind (configuration or execution) |

### Return type

[**CmspbFrontendSingleParameterResponse**](CmspbFrontendSingleParameterResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **frontend_list_activity_configuration**
> CmspbFrontendListConfigurationsResponse frontend_list_activity_configuration()

List activity configurations

List activity configurations

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_frontend_list_configurations_response import CmspbFrontendListConfigurationsResponse
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
    api_instance = cms_api.CmsApi(api_client)
    q = "q_example" # str | QueryBuilder query (optional)
    sort = "sort_example" # str | Sort order (optional)
    limit = 1 # int | Limit (optional)
    offset = 1 # int | Offset (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List activity configurations
        api_response = api_instance.frontend_list_activity_configuration(q=q, sort=sort, limit=limit, offset=offset)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_list_activity_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| QueryBuilder query | [optional]
 **sort** | **str**| Sort order | [optional]
 **limit** | **int**| Limit | [optional]
 **offset** | **int**| Offset | [optional]

### Return type

[**CmspbFrontendListConfigurationsResponse**](CmspbFrontendListConfigurationsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **frontend_list_activity_configuration_criteria**
> CmspbFrontendTriggersResponse frontend_list_activity_configuration_criteria(id)

List activity configuration criteria

List activity configuration criteria

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_frontend_triggers_response import CmspbFrontendTriggersResponse
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
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Activity Configuration ID
    limit = 1 # int | Limit (optional)
    offset = 1 # int | Offset (optional)

    # example passing only required values which don't have defaults set
    try:
        # List activity configuration criteria
        api_response = api_instance.frontend_list_activity_configuration_criteria(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_list_activity_configuration_criteria: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List activity configuration criteria
        api_response = api_instance.frontend_list_activity_configuration_criteria(id, limit=limit, offset=offset)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_list_activity_configuration_criteria: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Activity Configuration ID |
 **limit** | **int**| Limit | [optional]
 **offset** | **int**| Offset | [optional]

### Return type

[**CmspbFrontendTriggersResponse**](CmspbFrontendTriggersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **frontend_list_activity_configuration_parameters**
> CmspbFrontendParametersResponse frontend_list_activity_configuration_parameters(id)

List activity configuration parameters

List activity configuration parameters

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_frontend_parameters_response import CmspbFrontendParametersResponse
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
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Activity Configuration ID
    limit = 1 # int | Limit (optional)
    offset = 1 # int | Offset (optional)

    # example passing only required values which don't have defaults set
    try:
        # List activity configuration parameters
        api_response = api_instance.frontend_list_activity_configuration_parameters(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_list_activity_configuration_parameters: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List activity configuration parameters
        api_response = api_instance.frontend_list_activity_configuration_parameters(id, limit=limit, offset=offset)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_list_activity_configuration_parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Activity Configuration ID |
 **limit** | **int**| Limit | [optional]
 **offset** | **int**| Offset | [optional]

### Return type

[**CmspbFrontendParametersResponse**](CmspbFrontendParametersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **frontend_list_applicable_activities**
> CmspbFrontendListApplicableConfigurationsResponse frontend_list_applicable_activities(entity_type, entity_id)

List applicable activity configurations

List applicable activity configurations

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_frontend_list_applicable_configurations_response import CmspbFrontendListApplicableConfigurationsResponse
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
    api_instance = cms_api.CmsApi(api_client)
    entity_type = "entity_type_example" # str | Entity type
    entity_id = "entity_id_example" # str | Entity ID
    sort = "sort_example" # str | Sort order (optional)
    limit = 1 # int | Limit (optional)
    offset = 1 # int | Offset (optional)

    # example passing only required values which don't have defaults set
    try:
        # List applicable activity configurations
        api_response = api_instance.frontend_list_applicable_activities(entity_type, entity_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_list_applicable_activities: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List applicable activity configurations
        api_response = api_instance.frontend_list_applicable_activities(entity_type, entity_id, sort=sort, limit=limit, offset=offset)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_list_applicable_activities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| Entity type |
 **entity_id** | **str**| Entity ID |
 **sort** | **str**| Sort order | [optional]
 **limit** | **int**| Limit | [optional]
 **offset** | **int**| Offset | [optional]

### Return type

[**CmspbFrontendListApplicableConfigurationsResponse**](CmspbFrontendListApplicableConfigurationsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **frontend_list_applicable_entities_parameters**
> CmspbFrontendListApplicableEntitiesResponse frontend_list_applicable_entities_parameters(id, entity_type)

List applicable entities for a configuration

List applicable entities for a configuration

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_frontend_list_applicable_entities_response import CmspbFrontendListApplicableEntitiesResponse
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
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Activity Configuration ID
    entity_type = "entity_type_example" # str | Entity type
    limit = 1 # int | Limit (optional)
    offset = 1 # int | Offset (optional)

    # example passing only required values which don't have defaults set
    try:
        # List applicable entities for a configuration
        api_response = api_instance.frontend_list_applicable_entities_parameters(id, entity_type)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_list_applicable_entities_parameters: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List applicable entities for a configuration
        api_response = api_instance.frontend_list_applicable_entities_parameters(id, entity_type, limit=limit, offset=offset)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_list_applicable_entities_parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Activity Configuration ID |
 **entity_type** | **str**| Entity type |
 **limit** | **int**| Limit | [optional]
 **offset** | **int**| Offset | [optional]

### Return type

[**CmspbFrontendListApplicableEntitiesResponse**](CmspbFrontendListApplicableEntitiesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **frontend_validate_now**
> CmspbFrontendRunNowJobResponse frontend_validate_now(cms_validate_now_request)

Start validate now job

Start validate now job

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_frontend_run_now_job_response import CmspbFrontendRunNowJobResponse
from randori_api_sdk.model.cms_validate_now_request import CmsValidateNowRequest
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
    api_instance = cms_api.CmsApi(api_client)
    cms_validate_now_request = CmsValidateNowRequest(
        configuration_id="configuration_id_example",
        entity_id="entity_id_example",
        entity_type="entity_type_example",
    ) # CmsValidateNowRequest | Validate now request

    # example passing only required values which don't have defaults set
    try:
        # Start validate now job
        api_response = api_instance.frontend_validate_now(cms_validate_now_request)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_validate_now: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cms_validate_now_request** | [**CmsValidateNowRequest**](CmsValidateNowRequest.md)| Validate now request |

### Return type

[**CmspbFrontendRunNowJobResponse**](CmspbFrontendRunNowJobResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

