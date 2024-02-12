# FeatureResponseCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**List[FeatureResponse]**](FeatureResponse.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.feature_response_collection import FeatureResponseCollection

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureResponseCollection from a JSON string
feature_response_collection_instance = FeatureResponseCollection.from_json(json)
# print the JSON string representation of the object
print FeatureResponseCollection.to_json()

# convert the object into a dict
feature_response_collection_dict = feature_response_collection_instance.to_dict()
# create an instance of FeatureResponseCollection from a dict
feature_response_collection_form_dict = feature_response_collection.from_dict(feature_response_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


