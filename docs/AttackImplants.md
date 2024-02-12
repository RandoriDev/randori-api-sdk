# AttackImplants


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arch** | **str** |  | 
**bart_id** | **str** |  | 
**bits** | **int** |  | [optional] 
**created_on** | **datetime** |  | 
**host_ips** | **List[str]** |  | [optional] 
**hostnames** | **List[str]** |  | 
**id** | **str** |  | [optional] 
**last_checkin** | **datetime** |  | 
**method** | **object** |  | 
**next_checkin** | **datetime** |  | 
**nick** | **str** |  | [optional] 
**org_id** | **str** |  | 
**os** | **str** |  | [optional] 
**ostype** | **str** |  | [optional] 
**osver** | **str** |  | [optional] 
**status** | **str** |  | 
**uid** | **str** |  | 

## Example

```python
from randori_api_sdk.models.attack_implants import AttackImplants

# TODO update the JSON string below
json = "{}"
# create an instance of AttackImplants from a JSON string
attack_implants_instance = AttackImplants.from_json(json)
# print the JSON string representation of the object
print AttackImplants.to_json()

# convert the object into a dict
attack_implants_dict = attack_implants_instance.to_dict()
# create an instance of AttackImplants from a dict
attack_implants_form_dict = attack_implants.from_dict(attack_implants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


