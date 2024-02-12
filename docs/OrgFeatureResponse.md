# OrgFeatureResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_utc** | **datetime** |  | [optional] 
**feature_uuid** | **str** |  | [optional] 
**name** | **object** |  | [optional] 
**org_uuid** | **str** |  | [optional] 
**start_time_utc** | **datetime** |  | [optional] 
**type** | **object** |  | [optional] 

## Example

```python
from randori_api_sdk.models.org_feature_response import OrgFeatureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrgFeatureResponse from a JSON string
org_feature_response_instance = OrgFeatureResponse.from_json(json)
# print the JSON string representation of the object
print OrgFeatureResponse.to_json()

# convert the object into a dict
org_feature_response_dict = org_feature_response_instance.to_dict()
# create an instance of OrgFeatureResponse from a dict
org_feature_response_form_dict = org_feature_response.from_dict(org_feature_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


