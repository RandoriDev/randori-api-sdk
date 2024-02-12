# PreferenceOutCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preferences** | [**List[PreferenceOut]**](PreferenceOut.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.preference_out_collection import PreferenceOutCollection

# TODO update the JSON string below
json = "{}"
# create an instance of PreferenceOutCollection from a JSON string
preference_out_collection_instance = PreferenceOutCollection.from_json(json)
# print the JSON string representation of the object
print PreferenceOutCollection.to_json()

# convert the object into a dict
preference_out_collection_dict = preference_out_collection_instance.to_dict()
# create an instance of PreferenceOutCollection from a dict
preference_out_collection_form_dict = preference_out_collection.from_dict(preference_out_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


