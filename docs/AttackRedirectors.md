# AttackRedirectors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bart_id** | **str** |  | 
**created_on** | **datetime** |  | 
**deleted** | **bool** |  | 
**external_ip** | **str** |  | 
**external_ip_str** | **str** |  | 
**id** | **str** |  | [optional] 
**org_id** | **str** |  | 
**remote_row_id** | **int** |  | 
**retired** | **datetime** |  | [optional] 
**status** | **str** |  | 
**updated_on** | **datetime** |  | [optional] 
**usage** | **List[str]** |  | 

## Example

```python
from randori_api_sdk.models.attack_redirectors import AttackRedirectors

# TODO update the JSON string below
json = "{}"
# create an instance of AttackRedirectors from a JSON string
attack_redirectors_instance = AttackRedirectors.from_json(json)
# print the JSON string representation of the object
print AttackRedirectors.to_json()

# convert the object into a dict
attack_redirectors_dict = attack_redirectors_instance.to_dict()
# create an instance of AttackRedirectors from a dict
attack_redirectors_form_dict = attack_redirectors.from_dict(attack_redirectors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


