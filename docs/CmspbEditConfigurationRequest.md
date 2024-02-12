# CmspbEditConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed_fields** | [**List[CmspbEditConfigurationRequestFields]**](CmspbEditConfigurationRequestFields.md) |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**name** | **str** | string activity_configuration_id &#x3D; 1; | [optional] 
**pinned** | **bool** |  | [optional] 
**settings** | [**CmspbSettings**](CmspbSettings.md) |  | [optional] 
**template_version_id** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_edit_configuration_request import CmspbEditConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbEditConfigurationRequest from a JSON string
cmspb_edit_configuration_request_instance = CmspbEditConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print CmspbEditConfigurationRequest.to_json()

# convert the object into a dict
cmspb_edit_configuration_request_dict = cmspb_edit_configuration_request_instance.to_dict()
# create an instance of CmspbEditConfigurationRequest from a dict
cmspb_edit_configuration_request_form_dict = cmspb_edit_configuration_request.from_dict(cmspb_edit_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


