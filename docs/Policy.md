# Policy


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
from randori_api_sdk.models.policy import Policy

# TODO update the JSON string below
json = "{}"
# create an instance of Policy from a JSON string
policy_instance = Policy.from_json(json)
# print the JSON string representation of the object
print Policy.to_json()

# convert the object into a dict
policy_dict = policy_instance.to_dict()
# create an instance of Policy from a dict
policy_form_dict = policy.from_dict(policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


