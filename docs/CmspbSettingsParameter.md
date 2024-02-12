# CmspbSettingsParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_unset** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**obsolete_value** | **str** |  | [optional] 
**value** | [**StructpbValue**](StructpbValue.md) |  | [optional] 
**value_format** | [**ContentstorepbConfigurationValueFormat**](ContentstorepbConfigurationValueFormat.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_settings_parameter import CmspbSettingsParameter

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbSettingsParameter from a JSON string
cmspb_settings_parameter_instance = CmspbSettingsParameter.from_json(json)
# print the JSON string representation of the object
print CmspbSettingsParameter.to_json()

# convert the object into a dict
cmspb_settings_parameter_dict = cmspb_settings_parameter_instance.to_dict()
# create an instance of CmspbSettingsParameter from a dict
cmspb_settings_parameter_form_dict = cmspb_settings_parameter.from_dict(cmspb_settings_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


