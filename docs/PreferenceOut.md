# PreferenceOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_override** | **bool** |  | [optional] 
**preference** | **object** |  | 
**preference_source** | **object** |  | 
**value** | **object** |  | [optional] 

## Example

```python
from randori_api_sdk.models.preference_out import PreferenceOut

# TODO update the JSON string below
json = "{}"
# create an instance of PreferenceOut from a JSON string
preference_out_instance = PreferenceOut.from_json(json)
# print the JSON string representation of the object
print PreferenceOut.to_json()

# convert the object into a dict
preference_out_dict = preference_out_instance.to_dict()
# create an instance of PreferenceOut from a dict
preference_out_form_dict = preference_out.from_dict(preference_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


