# CmsValidateNowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_id** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.cms_validate_now_request import CmsValidateNowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CmsValidateNowRequest from a JSON string
cms_validate_now_request_instance = CmsValidateNowRequest.from_json(json)
# print the JSON string representation of the object
print CmsValidateNowRequest.to_json()

# convert the object into a dict
cms_validate_now_request_dict = cms_validate_now_request_instance.to_dict()
# create an instance of CmsValidateNowRequest from a dict
cms_validate_now_request_form_dict = cms_validate_now_request.from_dict(cms_validate_now_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


