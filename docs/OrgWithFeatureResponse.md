# OrgWithFeatureResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_utc** | **datetime** |  | [optional] 
**feature_name** | **object** |  | [optional] 
**feature_type** | **object** |  | [optional] 
**feature_uuid** | **str** |  | [optional] 
**org_name** | **str** |  | [optional] 
**org_uuid** | **str** |  | [optional] 
**start_time_utc** | **datetime** |  | [optional] 

## Example

```python
from randori_api_sdk.models.org_with_feature_response import OrgWithFeatureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrgWithFeatureResponse from a JSON string
org_with_feature_response_instance = OrgWithFeatureResponse.from_json(json)
# print the JSON string representation of the object
print OrgWithFeatureResponse.to_json()

# convert the object into a dict
org_with_feature_response_dict = org_with_feature_response_instance.to_dict()
# create an instance of OrgWithFeatureResponse from a dict
org_with_feature_response_form_dict = org_with_feature_response.from_dict(org_with_feature_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


