# OrgFeatureResponseCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_features** | [**List[OrgFeatureResponse]**](OrgFeatureResponse.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.org_feature_response_collection import OrgFeatureResponseCollection

# TODO update the JSON string below
json = "{}"
# create an instance of OrgFeatureResponseCollection from a JSON string
org_feature_response_collection_instance = OrgFeatureResponseCollection.from_json(json)
# print the JSON string representation of the object
print OrgFeatureResponseCollection.to_json()

# convert the object into a dict
org_feature_response_collection_dict = org_feature_response_collection_instance.to_dict()
# create an instance of OrgFeatureResponseCollection from a dict
org_feature_response_collection_form_dict = org_feature_response_collection.from_dict(org_feature_response_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


