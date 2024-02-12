# CmspbFrontendTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_value** | **str** |  | [optional] 
**field_label** | **str** |  | [optional] 
**field_type** | **str** |  | [optional] 
**input_variable_path** | **str** |  | [optional] 
**is_configurable** | **bool** |  | [optional] 
**is_matching** | **bool** |  | [optional] 
**is_standard** | **bool** |  | [optional] 
**operator** | **str** |  | [optional] 
**trigger_identifier** | **str** |  | [optional] 
**validation** | [**CmspbFrontendValidation**](CmspbFrontendValidation.md) |  | [optional] 
**value** | [**StructpbValue**](StructpbValue.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_trigger import CmspbFrontendTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendTrigger from a JSON string
cmspb_frontend_trigger_instance = CmspbFrontendTrigger.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendTrigger.to_json()

# convert the object into a dict
cmspb_frontend_trigger_dict = cmspb_frontend_trigger_instance.to_dict()
# create an instance of CmspbFrontendTrigger from a dict
cmspb_frontend_trigger_form_dict = cmspb_frontend_trigger.from_dict(cmspb_frontend_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


