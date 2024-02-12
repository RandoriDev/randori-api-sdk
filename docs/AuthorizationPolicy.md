# AuthorizationPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **List[object]** |  | [optional] 
**created_at** | **datetime** |  | 
**edited_at** | **datetime** |  | 
**entity_types** | **List[str]** |  | 
**expires_at** | **datetime** |  | [optional] 
**filter_data** | **object** |  | 
**id** | **str** |  | [optional] 
**is_active** | **bool** |  | 
**is_deleted** | **bool** |  | [optional] 
**is_dirty** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**org_id** | **str** |  | 
**version** | **int** |  | [optional] 

## Example

```python
from randori_api_sdk.models.authorization_policy import AuthorizationPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationPolicy from a JSON string
authorization_policy_instance = AuthorizationPolicy.from_json(json)
# print the JSON string representation of the object
print AuthorizationPolicy.to_json()

# convert the object into a dict
authorization_policy_dict = authorization_policy_instance.to_dict()
# create an instance of AuthorizationPolicy from a dict
authorization_policy_form_dict = authorization_policy.from_dict(authorization_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


