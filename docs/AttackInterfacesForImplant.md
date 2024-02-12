# AttackInterfacesForImplant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**bart_id** | **str** |  | 
**id** | **str** |  | 
**implant_id** | **str** |  | 
**ip_strs** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**org_id** | **str** |  | 

## Example

```python
from randori_api_sdk.models.attack_interfaces_for_implant import AttackInterfacesForImplant

# TODO update the JSON string below
json = "{}"
# create an instance of AttackInterfacesForImplant from a JSON string
attack_interfaces_for_implant_instance = AttackInterfacesForImplant.from_json(json)
# print the JSON string representation of the object
print AttackInterfacesForImplant.to_json()

# convert the object into a dict
attack_interfaces_for_implant_dict = attack_interfaces_for_implant_instance.to_dict()
# create an instance of AttackInterfacesForImplant from a dict
attack_interfaces_for_implant_form_dict = attack_interfaces_for_implant.from_dict(attack_interfaces_for_implant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


