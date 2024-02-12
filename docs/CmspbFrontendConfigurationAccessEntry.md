# CmspbFrontendConfigurationAccessEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** |  | [optional] 
**var_date** | [**TimestamppbTimestamp**](TimestamppbTimestamp.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_configuration_access_entry import CmspbFrontendConfigurationAccessEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendConfigurationAccessEntry from a JSON string
cmspb_frontend_configuration_access_entry_instance = CmspbFrontendConfigurationAccessEntry.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendConfigurationAccessEntry.to_json()

# convert the object into a dict
cmspb_frontend_configuration_access_entry_dict = cmspb_frontend_configuration_access_entry_instance.to_dict()
# create an instance of CmspbFrontendConfigurationAccessEntry from a dict
cmspb_frontend_configuration_access_entry_form_dict = cmspb_frontend_configuration_access_entry.from_dict(cmspb_frontend_configuration_access_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


