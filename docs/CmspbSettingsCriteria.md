# CmspbSettingsCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**obsolete_value** | **str** |  | [optional] 
**value** | [**StructpbValue**](StructpbValue.md) |  | [optional] 
**value_format** | [**ContentstorepbConfigurationValueFormat**](ContentstorepbConfigurationValueFormat.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_settings_criteria import CmspbSettingsCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbSettingsCriteria from a JSON string
cmspb_settings_criteria_instance = CmspbSettingsCriteria.from_json(json)
# print the JSON string representation of the object
print CmspbSettingsCriteria.to_json()

# convert the object into a dict
cmspb_settings_criteria_dict = cmspb_settings_criteria_instance.to_dict()
# create an instance of CmspbSettingsCriteria from a dict
cmspb_settings_criteria_form_dict = cmspb_settings_criteria.from_dict(cmspb_settings_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


