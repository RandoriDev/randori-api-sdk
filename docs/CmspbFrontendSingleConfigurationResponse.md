# CmspbFrontendSingleConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CmspbFrontendConfiguration**](CmspbFrontendConfiguration.md) |  | [optional] 
**links** | [**CmspbFrontendLinksSelf**](CmspbFrontendLinksSelf.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_single_configuration_response import CmspbFrontendSingleConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendSingleConfigurationResponse from a JSON string
cmspb_frontend_single_configuration_response_instance = CmspbFrontendSingleConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendSingleConfigurationResponse.to_json()

# convert the object into a dict
cmspb_frontend_single_configuration_response_dict = cmspb_frontend_single_configuration_response_instance.to_dict()
# create an instance of CmspbFrontendSingleConfigurationResponse from a dict
cmspb_frontend_single_configuration_response_form_dict = cmspb_frontend_single_configuration_response.from_dict(cmspb_frontend_single_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


