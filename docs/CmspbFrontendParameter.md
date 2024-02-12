# CmspbFrontendParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**field_label** | **str** |  | [optional] 
**field_type** | **str** |  | [optional] 
**is_configurable** | **bool** |  | [optional] 
**is_not_set** | **bool** |  | [optional] 
**is_optional** | **bool** |  | [optional] 
**parameter** | **str** |  | [optional] 
**parameter_type** | [**CmspbFrontendParameterKind**](CmspbFrontendParameterKind.md) |  | [optional] 
**validation** | [**CmspbFrontendValidation**](CmspbFrontendValidation.md) |  | [optional] 
**value** | [**StructpbValue**](StructpbValue.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_parameter import CmspbFrontendParameter

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendParameter from a JSON string
cmspb_frontend_parameter_instance = CmspbFrontendParameter.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendParameter.to_json()

# convert the object into a dict
cmspb_frontend_parameter_dict = cmspb_frontend_parameter_instance.to_dict()
# create an instance of CmspbFrontendParameter from a dict
cmspb_frontend_parameter_form_dict = cmspb_frontend_parameter.from_dict(cmspb_frontend_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


