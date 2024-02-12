# CmspbSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_parameters** | [**List[CmspbSettingsParameter]**](CmspbSettingsParameter.md) |  | [optional] 
**matching_criteria** | [**List[CmspbSettingsCriteria]**](CmspbSettingsCriteria.md) |  | [optional] 
**parameters** | [**List[CmspbSettingsParameter]**](CmspbSettingsParameter.md) |  | [optional] 
**trigger_criteria** | [**List[CmspbSettingsCriteria]**](CmspbSettingsCriteria.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_settings import CmspbSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbSettings from a JSON string
cmspb_settings_instance = CmspbSettings.from_json(json)
# print the JSON string representation of the object
print CmspbSettings.to_json()

# convert the object into a dict
cmspb_settings_dict = cmspb_settings_instance.to_dict()
# create an instance of CmspbSettings from a dict
cmspb_settings_form_dict = cmspb_settings.from_dict(cmspb_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


