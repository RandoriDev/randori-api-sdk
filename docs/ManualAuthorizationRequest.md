# ManualAuthorizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**detection_ids** | **List[str]** |  | [optional] 

## Example

```python
from randori_api_sdk.models.manual_authorization_request import ManualAuthorizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManualAuthorizationRequest from a JSON string
manual_authorization_request_instance = ManualAuthorizationRequest.from_json(json)
# print the JSON string representation of the object
print ManualAuthorizationRequest.to_json()

# convert the object into a dict
manual_authorization_request_dict = manual_authorization_request_instance.to_dict()
# create an instance of ManualAuthorizationRequest from a dict
manual_authorization_request_form_dict = manual_authorization_request.from_dict(manual_authorization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


