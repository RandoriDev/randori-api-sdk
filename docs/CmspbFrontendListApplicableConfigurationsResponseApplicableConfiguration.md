# CmspbFrontendListApplicableConfigurationsResponseApplicableConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**CmspbFrontendListApplicableConfigurationsResponseAttributes**](CmspbFrontendListApplicableConfigurationsResponseAttributes.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | [**CmspbFrontendType**](CmspbFrontendType.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_list_applicable_configurations_response_applicable_configuration import CmspbFrontendListApplicableConfigurationsResponseApplicableConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendListApplicableConfigurationsResponseApplicableConfiguration from a JSON string
cmspb_frontend_list_applicable_configurations_response_applicable_configuration_instance = CmspbFrontendListApplicableConfigurationsResponseApplicableConfiguration.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendListApplicableConfigurationsResponseApplicableConfiguration.to_json()

# convert the object into a dict
cmspb_frontend_list_applicable_configurations_response_applicable_configuration_dict = cmspb_frontend_list_applicable_configurations_response_applicable_configuration_instance.to_dict()
# create an instance of CmspbFrontendListApplicableConfigurationsResponseApplicableConfiguration from a dict
cmspb_frontend_list_applicable_configurations_response_applicable_configuration_form_dict = cmspb_frontend_list_applicable_configurations_response_applicable_configuration.from_dict(cmspb_frontend_list_applicable_configurations_response_applicable_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


