# randori_api_sdk.CmsApi

All URIs are relative to *https://app.randori.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_exception_policy_assignment**](CmsApi.md#change_exception_policy_assignment) | **PUT** /cms/api/v1/exception-policies/{id} | Change exception policy assignment.
[**change_organization_settings**](CmsApi.md#change_organization_settings) | **PATCH** /cms/api/v1/admin/organizations/{id} | Change organization settings
[**create_activity_configuration**](CmsApi.md#create_activity_configuration) | **POST** /cms/api/v1/activity-configurations | Create an activity configuration
[**delete_exception_policy**](CmsApi.md#delete_exception_policy) | **DELETE** /cms/api/v1/exception-policies/{id} | Delete exception policy.
[**edit_activity_configuration_version**](CmsApi.md#edit_activity_configuration_version) | **PATCH** /cms/api/v1/activity-configuration-versions/{id} | Edit activity configuration version.
[**edit_exception_policy**](CmsApi.md#edit_exception_policy) | **PATCH** /cms/api/v1/exception-policies/{id} | Edit exception policy.
[**find_planning_results**](CmsApi.md#find_planning_results) | **POST** /cms/api/v1/planning-results | List planning results for org
[**frontend_create_exception_policy**](CmsApi.md#frontend_create_exception_policy) | **POST** /cms/api/v1/frontend/exception-policies | Create exception policy
[**frontend_edit_activity_configuration**](CmsApi.md#frontend_edit_activity_configuration) | **PATCH** /cms/api/v1/frontend/activity-configurations/{id} | Edit activity configurations
[**frontend_edit_activity_configuration_criteria**](CmsApi.md#frontend_edit_activity_configuration_criteria) | **POST** /cms/api/v1/frontend/activity-configurations/{id}/trigger_criteria/{name} | Edit activity configuration criteria
[**frontend_edit_activity_configuration_parameter**](CmsApi.md#frontend_edit_activity_configuration_parameter) | **POST** /cms/api/v1/frontend/activity-configurations/{id}/parameters/{name}/{kind} | Edit activity configuration parameter
[**frontend_edit_exception_policy**](CmsApi.md#frontend_edit_exception_policy) | **PATCH** /cms/api/v1/frontend/exception-policies/{id} | Edit exception policy
[**frontend_get_activity_configuration**](CmsApi.md#frontend_get_activity_configuration) | **GET** /cms/api/v1/frontend/activity-configurations/{id} | Get activity configurations
[**frontend_get_configuration_criteria**](CmsApi.md#frontend_get_configuration_criteria) | **GET** /cms/api/v1/frontend/activity-configurations/{id}/trigger_criteria/{name} | Get activity configuration criteria
[**frontend_get_configuration_parameter**](CmsApi.md#frontend_get_configuration_parameter) | **GET** /cms/api/v1/frontend/activity-configurations/{id}/parameters/{name}/{kind} | Get activity configuration parameter
[**frontend_get_exception_policy**](CmsApi.md#frontend_get_exception_policy) | **GET** /cms/api/v1/frontend/exception-policies/{id} | Get exception policy
[**frontend_list_activity_configuration**](CmsApi.md#frontend_list_activity_configuration) | **GET** /cms/api/v1/frontend/activity-configurations | List activity configurations
[**frontend_list_activity_configuration_criteria**](CmsApi.md#frontend_list_activity_configuration_criteria) | **GET** /cms/api/v1/frontend/activity-configurations/{id}/trigger_criteria | List activity configuration criteria
[**frontend_list_activity_configuration_parameters**](CmsApi.md#frontend_list_activity_configuration_parameters) | **GET** /cms/api/v1/frontend/activity-configurations/{id}/parameters | List activity configuration parameters
[**frontend_list_applicable_activities**](CmsApi.md#frontend_list_applicable_activities) | **GET** /cms/api/v1/frontend/applicable-activities/{entity_type}/{entity_id} | List applicable activity configurations
[**frontend_list_applicable_entities_parameters**](CmsApi.md#frontend_list_applicable_entities_parameters) | **GET** /cms/api/v1/frontend/activity-configurations/{id}/applicable-entities/{entity_type} | List applicable entities for a configuration
[**frontend_list_configurations_for_policy**](CmsApi.md#frontend_list_configurations_for_policy) | **GET** /cms/api/v1/frontend/exception-policies/{id}/configurations | List configurations for exception policy
[**frontend_list_exception_policies**](CmsApi.md#frontend_list_exception_policies) | **GET** /cms/api/v1/frontend/exception-policies | List exception policy
[**frontend_validate_now**](CmsApi.md#frontend_validate_now) | **POST** /cms/api/v1/frontend/validate | Start validate now job
[**get_activity_configuration_version**](CmsApi.md#get_activity_configuration_version) | **GET** /cms/api/v1/activity-configuration-versions/{id} | Retrieve activity configuration version.
[**get_activity_configuration_versions**](CmsApi.md#get_activity_configuration_versions) | **GET** /cms/api/v1/activity-configuration-versions | List activity configuration versions for org
[**get_exception_policies**](CmsApi.md#get_exception_policies) | **GET** /cms/api/v1/exception-policies | List exception policies for org
[**get_exception_policy**](CmsApi.md#get_exception_policy) | **GET** /cms/api/v1/exception-policies/{id} | Retrieve exception policy.
[**get_organization_settings**](CmsApi.md#get_organization_settings) | **GET** /cms/api/v1/admin/organizations/{id} | Get organization settings
[**list_organizations_settings**](CmsApi.md#list_organizations_settings) | **GET** /cms/api/v1/admin/organizations | List organizations with settings
[**publish_activity_configuration**](CmsApi.md#publish_activity_configuration) | **POST** /cms/api/v1/activity-configuration-versions/{id}/publish | Publish activity configuration.
[**upload_exception_policy**](CmsApi.md#upload_exception_policy) | **POST** /cms/api/v1/exception-policies | Upload an exception policy
[**validate_activity_configuration_version**](CmsApi.md#validate_activity_configuration_version) | **POST** /cms/api/v1/activity-configuration-versions/{id}/validate | Validate activity configuration-version


# **change_exception_policy_assignment**
> CmspbActivityTypeFlowResponse change_exception_policy_assignment(id, cmspb_assign_configuration_to_policy_request)

Change exception policy assignment.

Change exception policy assignment.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_assign_configuration_to_policy_request import CmspbAssignConfigurationToPolicyRequest
from randori_api_sdk.model.cmspb_activity_type_flow_response import CmspbActivityTypeFlowResponse
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Exception Policy ID
    cmspb_assign_configuration_to_policy_request = CmspbAssignConfigurationToPolicyRequest(
        configuration_id=[
            "configuration_id_example",
        ],
        revoke=True,
    ) # CmspbAssignConfigurationToPolicyRequest | Assign configuration to policy request

    # example passing only required values which don't have defaults set
    try:
        # Change exception policy assignment.
        api_response = api_instance.change_exception_policy_assignment(id, cmspb_assign_configuration_to_policy_request)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->change_exception_policy_assignment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Exception Policy ID |
 **cmspb_assign_configuration_to_policy_request** | [**CmspbAssignConfigurationToPolicyRequest**](CmspbAssignConfigurationToPolicyRequest.md)| Assign configuration to policy request |

### Return type

[**CmspbActivityTypeFlowResponse**](CmspbActivityTypeFlowResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_organization_settings**
> CmspbActivityTypeFlowResponse change_organization_settings(id, cmspb_change_organization_settings_request)

Change organization settings

Change organization settings

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_activity_type_flow_response import CmspbActivityTypeFlowResponse
from randori_api_sdk.model.cmspb_change_organization_settings_request import CmspbChangeOrganizationSettingsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Organization id
    cmspb_change_organization_settings_request = CmspbChangeOrganizationSettingsRequest(
        auto_enable=True,
        changed_fields=[
            CmspbChangeOrganizationSettingsRequestFields(0),
        ],
        use_latest=True,
    ) # CmspbChangeOrganizationSettingsRequest | Change organization settings

    # example passing only required values which don't have defaults set
    try:
        # Change organization settings
        api_response = api_instance.change_organization_settings(id, cmspb_change_organization_settings_request)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->change_organization_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization id |
 **cmspb_change_organization_settings_request** | [**CmspbChangeOrganizationSettingsRequest**](CmspbChangeOrganizationSettingsRequest.md)| Change organization settings |

### Return type

[**CmspbActivityTypeFlowResponse**](CmspbActivityTypeFlowResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_activity_configuration**
> CmspbConfigurationsResponse create_activity_configuration(cmspb_create_configuration_request)

Create an activity configuration

Create an activity configuration

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_create_configuration_request import CmspbCreateConfigurationRequest
from randori_api_sdk.model.cmspb_configurations_response import CmspbConfigurationsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    cmspb_create_configuration_request = CmspbCreateConfigurationRequest(
        description="description_example",
        enabled=True,
        fork=True,
        from_configuration_id="from_configuration_id_example",
        name="name_example",
        pinned=True,
        settings=CmspbSettings(
            execution_parameters=[
                CmspbSettingsParameter(
                    is_unset=True,
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=None,
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
            matching_criteria=[
                CmspbSettingsCriteria(
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=None,
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
            parameters=[
                CmspbSettingsParameter(
                    is_unset=True,
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=None,
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
            trigger_criteria=[
                CmspbSettingsCriteria(
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=None,
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
        ),
    ) # CmspbCreateConfigurationRequest | Activity Configuration creation request

    # example passing only required values which don't have defaults set
    try:
        # Create an activity configuration
        api_response = api_instance.create_activity_configuration(cmspb_create_configuration_request)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->create_activity_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cmspb_create_configuration_request** | [**CmspbCreateConfigurationRequest**](CmspbCreateConfigurationRequest.md)| Activity Configuration creation request |

### Return type

[**CmspbConfigurationsResponse**](CmspbConfigurationsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_exception_policy**
> CmspbPolicyResponse delete_exception_policy(id)

Delete exception policy.

Delete exception policy.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_policy_response import CmspbPolicyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Exception Policy ID

    # example passing only required values which don't have defaults set
    try:
        # Delete exception policy.
        api_response = api_instance.delete_exception_policy(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->delete_exception_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Exception Policy ID |

### Return type

[**CmspbPolicyResponse**](CmspbPolicyResponse.md)

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

# **edit_activity_configuration_version**
> CmspbConfigurationsResponse edit_activity_configuration_version(id, cmspb_edit_configuration_request)

Edit activity configuration version.

Edit activity configuration version.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_edit_configuration_request import CmspbEditConfigurationRequest
from randori_api_sdk.model.cmspb_configurations_response import CmspbConfigurationsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Activity Configuration Version ID
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
                    value=None,
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
            matching_criteria=[
                CmspbSettingsCriteria(
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=None,
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
            parameters=[
                CmspbSettingsParameter(
                    is_unset=True,
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=None,
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
            trigger_criteria=[
                CmspbSettingsCriteria(
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=None,
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
        ),
        template_version_id="template_version_id_example",
    ) # CmspbEditConfigurationRequest | Activity Configuration edit request

    # example passing only required values which don't have defaults set
    try:
        # Edit activity configuration version.
        api_response = api_instance.edit_activity_configuration_version(id, cmspb_edit_configuration_request)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->edit_activity_configuration_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Activity Configuration Version ID |
 **cmspb_edit_configuration_request** | [**CmspbEditConfigurationRequest**](CmspbEditConfigurationRequest.md)| Activity Configuration edit request |

### Return type

[**CmspbConfigurationsResponse**](CmspbConfigurationsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_exception_policy**
> CmspbPolicyResponse edit_exception_policy(id, cmspb_edit_configuration_request)

Edit exception policy.

Edit exception policy.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_policy_response import CmspbPolicyResponse
from randori_api_sdk.model.cmspb_edit_configuration_request import CmspbEditConfigurationRequest
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Exception Policy ID
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
                    value=None,
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
            matching_criteria=[
                CmspbSettingsCriteria(
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=None,
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
            parameters=[
                CmspbSettingsParameter(
                    is_unset=True,
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=None,
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
            trigger_criteria=[
                CmspbSettingsCriteria(
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=None,
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
        ),
        template_version_id="template_version_id_example",
    ) # CmspbEditConfigurationRequest | Exception Policy edit request

    # example passing only required values which don't have defaults set
    try:
        # Edit exception policy.
        api_response = api_instance.edit_exception_policy(id, cmspb_edit_configuration_request)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->edit_exception_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Exception Policy ID |
 **cmspb_edit_configuration_request** | [**CmspbEditConfigurationRequest**](CmspbEditConfigurationRequest.md)| Exception Policy edit request |

### Return type

[**CmspbPolicyResponse**](CmspbPolicyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_planning_results**
> CmspbListPlanningResultsResponse find_planning_results(cms_list_statistics_request)

List planning results for org

List planning results for org

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_list_planning_results_response import CmspbListPlanningResultsResponse
from randori_api_sdk.model.cms_list_statistics_request import CmsListStatisticsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    cms_list_statistics_request = CmsListStatisticsRequest(
        activity_configuration_id="activity_configuration_id_example",
        activity_configuration_version_id="activity_configuration_version_id_example",
        entity_id="entity_id_example",
        _from="_from_example",
        limit=1,
        offset=1,
        planned=True,
        planning_result_id="planning_result_id_example",
        to="to_example",
        triggered=True,
    ) # CmsListStatisticsRequest | List planning results request

    # example passing only required values which don't have defaults set
    try:
        # List planning results for org
        api_response = api_instance.find_planning_results(cms_list_statistics_request)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->find_planning_results: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cms_list_statistics_request** | [**CmsListStatisticsRequest**](CmsListStatisticsRequest.md)| List planning results request |

### Return type

[**CmspbListPlanningResultsResponse**](CmspbListPlanningResultsResponse.md)

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

# **frontend_create_exception_policy**
> CmspbFrontendSingleExceptionPolicyResponse frontend_create_exception_policy(cmspb_frontend_create_policy_request)

Create exception policy

Create exception policy

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_frontend_single_exception_policy_response import CmspbFrontendSingleExceptionPolicyResponse
from randori_api_sdk.model.cmspb_frontend_create_policy_request import CmspbFrontendCreatePolicyRequest
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    cmspb_frontend_create_policy_request = CmspbFrontendCreatePolicyRequest(
        config=CmspbFrontendPolicyConfiguration(
            activity_classes=[
                "activity_classes_example",
            ],
            perspectives=[
                "perspectives_example",
            ],
            time_spans=[
                CmspbFrontendExceptionPolicyTimeSpan(
                    end=CmspbFrontendExceptionPolicyDatetime(
                        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        time="time_example",
                    ),
                    start=CmspbFrontendExceptionPolicyDatetime(
                        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        time="time_example",
                    ),
                ),
            ],
            timezone="timezone_example",
            week_spans=[
                CmspbFrontendExceptionPolicyWeekSpan(
                    end=CmspbFrontendExceptionPolicyWeekdayAndTime(
                        day=CmspbFrontendExceptionPolicyWeekday(0),
                        time="time_example",
                    ),
                    start=CmspbFrontendExceptionPolicyWeekdayAndTime(
                        day=CmspbFrontendExceptionPolicyWeekday(0),
                        time="time_example",
                    ),
                ),
            ],
        ),
        description="description_example",
        enabled=True,
        name="name_example",
    ) # CmspbFrontendCreatePolicyRequest | Exception policy create request

    # example passing only required values which don't have defaults set
    try:
        # Create exception policy
        api_response = api_instance.frontend_create_exception_policy(cmspb_frontend_create_policy_request)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_create_exception_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cmspb_frontend_create_policy_request** | [**CmspbFrontendCreatePolicyRequest**](CmspbFrontendCreatePolicyRequest.md)| Exception policy create request |

### Return type

[**CmspbFrontendSingleExceptionPolicyResponse**](CmspbFrontendSingleExceptionPolicyResponse.md)

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
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
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
                    value=None,
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
            matching_criteria=[
                CmspbSettingsCriteria(
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=None,
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
            parameters=[
                CmspbSettingsParameter(
                    is_unset=True,
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=None,
                    value_format=ContentstorepbConfigurationValueFormat(0),
                ),
            ],
            trigger_criteria=[
                CmspbSettingsCriteria(
                    name="name_example",
                    obsolete_value="obsolete_value_example",
                    value=None,
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
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
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
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
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

# **frontend_edit_exception_policy**
> CmspbFrontendSingleExceptionPolicyResponse frontend_edit_exception_policy(id, cmspb_frontend_edit_policy_request)

Edit exception policy

Edit exception policy

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_frontend_edit_policy_request import CmspbFrontendEditPolicyRequest
from randori_api_sdk.model.cmspb_frontend_single_exception_policy_response import CmspbFrontendSingleExceptionPolicyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Exception Policy ID
    cmspb_frontend_edit_policy_request = CmspbFrontendEditPolicyRequest(
        changed_fields=[
            CmspbFrontendEditPolicyRequestFields(0),
        ],
        config=CmspbFrontendPolicyConfiguration(
            activity_classes=[
                "activity_classes_example",
            ],
            perspectives=[
                "perspectives_example",
            ],
            time_spans=[
                CmspbFrontendExceptionPolicyTimeSpan(
                    end=CmspbFrontendExceptionPolicyDatetime(
                        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        time="time_example",
                    ),
                    start=CmspbFrontendExceptionPolicyDatetime(
                        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        time="time_example",
                    ),
                ),
            ],
            timezone="timezone_example",
            week_spans=[
                CmspbFrontendExceptionPolicyWeekSpan(
                    end=CmspbFrontendExceptionPolicyWeekdayAndTime(
                        day=CmspbFrontendExceptionPolicyWeekday(0),
                        time="time_example",
                    ),
                    start=CmspbFrontendExceptionPolicyWeekdayAndTime(
                        day=CmspbFrontendExceptionPolicyWeekday(0),
                        time="time_example",
                    ),
                ),
            ],
        ),
        description="description_example",
        enabled=True,
        name="name_example",
    ) # CmspbFrontendEditPolicyRequest | Exception policy edit request

    # example passing only required values which don't have defaults set
    try:
        # Edit exception policy
        api_response = api_instance.frontend_edit_exception_policy(id, cmspb_frontend_edit_policy_request)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_edit_exception_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Exception Policy ID |
 **cmspb_frontend_edit_policy_request** | [**CmspbFrontendEditPolicyRequest**](CmspbFrontendEditPolicyRequest.md)| Exception policy edit request |

### Return type

[**CmspbFrontendSingleExceptionPolicyResponse**](CmspbFrontendSingleExceptionPolicyResponse.md)

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
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
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
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
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
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
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

# **frontend_get_exception_policy**
> CmspbFrontendSingleExceptionPolicyResponse frontend_get_exception_policy(id)

Get exception policy

Get exception policy

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_frontend_single_exception_policy_response import CmspbFrontendSingleExceptionPolicyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Exception Policy ID

    # example passing only required values which don't have defaults set
    try:
        # Get exception policy
        api_response = api_instance.frontend_get_exception_policy(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_get_exception_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Exception Policy ID |

### Return type

[**CmspbFrontendSingleExceptionPolicyResponse**](CmspbFrontendSingleExceptionPolicyResponse.md)

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
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
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
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
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
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
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
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
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
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
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

# **frontend_list_configurations_for_policy**
> CmspbFrontendListConfigurationsResponse frontend_list_configurations_for_policy(id)

List configurations for exception policy

List configurations for exception policy

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_frontend_list_configurations_response import CmspbFrontendListConfigurationsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Exception Policy ID
    limit = 1 # int | Limit (optional)
    offset = 1 # int | Offset (optional)

    # example passing only required values which don't have defaults set
    try:
        # List configurations for exception policy
        api_response = api_instance.frontend_list_configurations_for_policy(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_list_configurations_for_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List configurations for exception policy
        api_response = api_instance.frontend_list_configurations_for_policy(id, limit=limit, offset=offset)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_list_configurations_for_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Exception Policy ID |
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

# **frontend_list_exception_policies**
> CmspbFrontendListExceptionPoliciesResponse frontend_list_exception_policies()

List exception policy

List exception policy

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_frontend_list_exception_policies_response import CmspbFrontendListExceptionPoliciesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
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
        # List exception policy
        api_response = api_instance.frontend_list_exception_policies(q=q, sort=sort, limit=limit, offset=offset)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->frontend_list_exception_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| QueryBuilder query | [optional]
 **sort** | **str**| Sort order | [optional]
 **limit** | **int**| Limit | [optional]
 **offset** | **int**| Offset | [optional]

### Return type

[**CmspbFrontendListExceptionPoliciesResponse**](CmspbFrontendListExceptionPoliciesResponse.md)

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
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
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

# **get_activity_configuration_version**
> CmspbGetConfigurationsResponse get_activity_configuration_version(id)

Retrieve activity configuration version.

Retrieve activity configuration version.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_get_configurations_response import CmspbGetConfigurationsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Activity Configuration ID

    # example passing only required values which don't have defaults set
    try:
        # Retrieve activity configuration version.
        api_response = api_instance.get_activity_configuration_version(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->get_activity_configuration_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Activity Configuration ID |

### Return type

[**CmspbGetConfigurationsResponse**](CmspbGetConfigurationsResponse.md)

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

# **get_activity_configuration_versions**
> CmspbListConfigurationsResponse get_activity_configuration_versions(org_id)

List activity configuration versions for org

List activity configurations versions for org

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_list_configurations_response import CmspbListConfigurationsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    org_id = "org_id_example" # str | Organization ID
    configuration_id = "configuration_id_example" # str | Configuration ID (optional)
    policy_id = "policy_id_example" # str | Policy ID (optional)
    limit = 1 # int | Limit (optional)
    offset = 1 # int | Offset (optional)

    # example passing only required values which don't have defaults set
    try:
        # List activity configuration versions for org
        api_response = api_instance.get_activity_configuration_versions(org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->get_activity_configuration_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List activity configuration versions for org
        api_response = api_instance.get_activity_configuration_versions(org_id, configuration_id=configuration_id, policy_id=policy_id, limit=limit, offset=offset)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->get_activity_configuration_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID |
 **configuration_id** | **str**| Configuration ID | [optional]
 **policy_id** | **str**| Policy ID | [optional]
 **limit** | **int**| Limit | [optional]
 **offset** | **int**| Offset | [optional]

### Return type

[**CmspbListConfigurationsResponse**](CmspbListConfigurationsResponse.md)

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

# **get_exception_policies**
> CmspbListPoliciesResponse get_exception_policies(org_id)

List exception policies for org

List exception policies for org

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_list_policies_response import CmspbListPoliciesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    org_id = "org_id_example" # str | Organization ID
    limit = 1 # int | Limit (optional)
    offset = 1 # int | Offset (optional)

    # example passing only required values which don't have defaults set
    try:
        # List exception policies for org
        api_response = api_instance.get_exception_policies(org_id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->get_exception_policies: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List exception policies for org
        api_response = api_instance.get_exception_policies(org_id, limit=limit, offset=offset)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->get_exception_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID |
 **limit** | **int**| Limit | [optional]
 **offset** | **int**| Offset | [optional]

### Return type

[**CmspbListPoliciesResponse**](CmspbListPoliciesResponse.md)

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

# **get_exception_policy**
> CmspbPolicyResponse get_exception_policy(id)

Retrieve exception policy.

Retrieve exception policy.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_policy_response import CmspbPolicyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Exception Policy ID

    # example passing only required values which don't have defaults set
    try:
        # Retrieve exception policy.
        api_response = api_instance.get_exception_policy(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->get_exception_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Exception Policy ID |

### Return type

[**CmspbPolicyResponse**](CmspbPolicyResponse.md)

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

# **get_organization_settings**
> CmspbGetOrganizationResponse get_organization_settings(id)

Get organization settings

Get organization settings

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_get_organization_response import CmspbGetOrganizationResponse
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Activity type ID

    # example passing only required values which don't have defaults set
    try:
        # Get organization settings
        api_response = api_instance.get_organization_settings(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->get_organization_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Activity type ID |

### Return type

[**CmspbGetOrganizationResponse**](CmspbGetOrganizationResponse.md)

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

# **list_organizations_settings**
> CmspbListOrganizationSettingsResponse list_organizations_settings()

List organizations with settings

List organizations with settings

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_list_organization_settings_response import CmspbListOrganizationSettingsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    limit = 1 # int | Limit (optional)
    offset = 1 # int | Offset (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List organizations with settings
        api_response = api_instance.list_organizations_settings(limit=limit, offset=offset)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->list_organizations_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit | [optional]
 **offset** | **int**| Offset | [optional]

### Return type

[**CmspbListOrganizationSettingsResponse**](CmspbListOrganizationSettingsResponse.md)

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

# **publish_activity_configuration**
> CmspbConfigurationsResponse publish_activity_configuration(id)

Publish activity configuration.

Publish activity configuration.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_configurations_response import CmspbConfigurationsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Activity Configuration Version ID

    # example passing only required values which don't have defaults set
    try:
        # Publish activity configuration.
        api_response = api_instance.publish_activity_configuration(id)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->publish_activity_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Activity Configuration Version ID |

### Return type

[**CmspbConfigurationsResponse**](CmspbConfigurationsResponse.md)

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

# **upload_exception_policy**
> CmspbPolicyResponse upload_exception_policy(cms_upload_policy_request)

Upload an exception policy

Upload an exception policy

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_policy_response import CmspbPolicyResponse
from randori_api_sdk.model.cms_upload_policy_request import CmsUploadPolicyRequest
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    cms_upload_policy_request = CmsUploadPolicyRequest(
        enabled="enabled_example",
        yaml_config=MultipartFileHeader(
            filename="filename_example",
            header=TextprotoMIMEHeader(
                key=[
                    "key_example",
                ],
            ),
            size=1,
        ),
    ) # CmsUploadPolicyRequest | Exception Policy upload request

    # example passing only required values which don't have defaults set
    try:
        # Upload an exception policy
        api_response = api_instance.upload_exception_policy(cms_upload_policy_request)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->upload_exception_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cms_upload_policy_request** | [**CmsUploadPolicyRequest**](CmsUploadPolicyRequest.md)| Exception Policy upload request |

### Return type

[**CmspbPolicyResponse**](CmspbPolicyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_activity_configuration_version**
> CmspbStartValidationSeriesResponse validate_activity_configuration_version(id, cmspb_start_validation_series_request)

Validate activity configuration-version

Validate activity configuration version

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import cms_api
from randori_api_sdk.model.cmspb_start_validation_series_response import CmspbStartValidationSeriesResponse
from randori_api_sdk.model.cmspb_start_validation_series_request import CmspbStartValidationSeriesRequest
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cms_api.CmsApi(api_client)
    id = "id_example" # str | Activity Configuration Version ID
    cmspb_start_validation_series_request = CmspbStartValidationSeriesRequest(
        message=[
            ValidationpbValidationEvent(
                detections=[
                    PlatformpbDetection(
                        affiliation=1,
                        affiliation_display=1,
                        affiliation_override=True,
                        authority_display=True,
                        authority_distance=1,
                        authority_override=True,
                        authority_path=[
                            "authority_path_example",
                        ],
                        authority_source="authority_source_example",
                        authorization_state=PlatformpbAuthorizationState(0),
                        confidence=1,
                        confidence_display=1,
                        confidence_override=True,
                        detection_criteria=StructpbStruct(
                            fields={
                                "key": StructpbValue(
                                    kind=None,
                                ),
                            },
                        ),
                        discovery_distance=1,
                        discovery_path=[
                            "discovery_path_example",
                        ],
                        discovery_source="discovery_source_example",
                        first_time=TimestamppbTimestamp(
                            nanos=1,
                            seconds=1,
                        ),
                        hostname_id="hostname_id_example",
                        id="id_example",
                        lens_view="lens_view_example",
                        network_id="network_id_example",
                        perspective="perspective_example",
                        perspective_id="perspective_id_example",
                        poc_id="poc_id_example",
                        port_id="port_id_example",
                        service=PlatformpbService(
                            applicability=1,
                            attack_note="attack_note_example",
                            cpe=StructpbStruct(
                                fields={
                                    "key": StructpbValue(
                                        kind=None,
                                    ),
                                },
                            ),
                            creator_type="creator_type_example",
                            creator_uuid="creator_uuid_example",
                            criticality=1,
                            deleted=True,
                            description="description_example",
                            description_source="description_source_example",
                            enumerability=1,
                            first_time=TimestamppbTimestamp(
                                nanos=1,
                                seconds=1,
                            ),
                            id="id_example",
                            name="name_example",
                            post_exploit=1,
                            private_weakness=1,
                            promoted=True,
                            promoter="promoter_example",
                            promotion_time=TimestamppbTimestamp(
                                nanos=1,
                                seconds=1,
                            ),
                            public_weakness=1,
                            randori_notes="randori_notes_example",
                            reference="reference_example",
                            research=1,
                            svc_type="svc_type_example",
                            sys_period="sys_period_example",
                            target_temptation=1,
                            tech_category=[
                                "tech_category_example",
                            ],
                            temptation_last_modified=TimestamppbTimestamp(
                                nanos=1,
                                seconds=1,
                            ),
                            time=TimestamppbTimestamp(
                                nanos=1,
                                seconds=1,
                            ),
                            type="type_example",
                            vendor="vendor_example",
                            version="version_example",
                        ),
                        service_id="service_id_example",
                        time=TimestamppbTimestamp(
                            nanos=1,
                            seconds=1,
                        ),
                        type="type_example",
                        validated_vulnerabilities=[
                            "validated_vulnerabilities_example",
                        ],
                    ),
                ],
                entity=PlatformpbEntity(
                    authority_display=True,
                    authority_distance=1,
                    authority_override=True,
                    authorization_state=PlatformpbAuthorizationState(0),
                    deleted=True,
                    detection_criteria=StructpbStruct(
                        fields={
                            "key": StructpbValue(
                                kind=None,
                            ),
                        },
                    ),
                    first_time=TimestamppbTimestamp(
                        nanos=1,
                        seconds=1,
                    ),
                    hostname_type="hostname_type_example",
                    id="id_example",
                    lens_view="lens_view_example",
                    network_size=1,
                    orig_lens_view="orig_lens_view_example",
                    perspective=PlatformpbEntityPerspective(
                        capabilities=StructpbStruct(
                            fields={
                                "key": StructpbValue(
                                    kind=None,
                                ),
                            },
                        ),
                        tags=[
                            "tags_example",
                        ],
                        type="type_example",
                    ),
                    perspective_id="perspective_id_example",
                    time=TimestamppbTimestamp(
                        nanos=1,
                        seconds=1,
                    ),
                    type="type_example",
                    value="value_example",
                ),
                open_ports=[
                    1,
                ],
                service=PlatformpbService(
                    applicability=1,
                    attack_note="attack_note_example",
                    cpe=StructpbStruct(
                        fields={
                            "key": StructpbValue(
                                kind=None,
                            ),
                        },
                    ),
                    creator_type="creator_type_example",
                    creator_uuid="creator_uuid_example",
                    criticality=1,
                    deleted=True,
                    description="description_example",
                    description_source="description_source_example",
                    enumerability=1,
                    first_time=TimestamppbTimestamp(
                        nanos=1,
                        seconds=1,
                    ),
                    id="id_example",
                    name="name_example",
                    post_exploit=1,
                    private_weakness=1,
                    promoted=True,
                    promoter="promoter_example",
                    promotion_time=TimestamppbTimestamp(
                        nanos=1,
                        seconds=1,
                    ),
                    public_weakness=1,
                    randori_notes="randori_notes_example",
                    reference="reference_example",
                    research=1,
                    svc_type="svc_type_example",
                    sys_period="sys_period_example",
                    target_temptation=1,
                    tech_category=[
                        "tech_category_example",
                    ],
                    temptation_last_modified=TimestamppbTimestamp(
                        nanos=1,
                        seconds=1,
                    ),
                    time=TimestamppbTimestamp(
                        nanos=1,
                        seconds=1,
                    ),
                    type="type_example",
                    vendor="vendor_example",
                    version="version_example",
                ),
            ),
        ],
        message_source=ValidationpbStartValidationSeriesRequestMessageSource(0),
        number_limit=1,
        time_limit=1,
    ) # CmspbStartValidationSeriesRequest | Validation Series Request

    # example passing only required values which don't have defaults set
    try:
        # Validate activity configuration-version
        api_response = api_instance.validate_activity_configuration_version(id, cmspb_start_validation_series_request)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling CmsApi->validate_activity_configuration_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Activity Configuration Version ID |
 **cmspb_start_validation_series_request** | [**CmspbStartValidationSeriesRequest**](CmspbStartValidationSeriesRequest.md)| Validation Series Request |

### Return type

[**CmspbStartValidationSeriesResponse**](CmspbStartValidationSeriesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

