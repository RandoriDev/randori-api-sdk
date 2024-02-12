# AttackCheckinsForImplant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bart_id** | **str** |  | 
**id** | **str** |  | 
**implant_id** | **str** |  | 
**last_checkin** | **datetime** |  | 
**method** | **object** |  | 
**org_id** | **str** |  | 
**src_ip** | **str** |  | 
**src_ip_str** | **str** |  | 

## Example

```python
from randori_api_sdk.models.attack_checkins_for_implant import AttackCheckinsForImplant

# TODO update the JSON string below
json = "{}"
# create an instance of AttackCheckinsForImplant from a JSON string
attack_checkins_for_implant_instance = AttackCheckinsForImplant.from_json(json)
# print the JSON string representation of the object
print AttackCheckinsForImplant.to_json()

# convert the object into a dict
attack_checkins_for_implant_dict = attack_checkins_for_implant_instance.to_dict()
# create an instance of AttackCheckinsForImplant from a dict
attack_checkins_for_implant_form_dict = attack_checkins_for_implant.from_dict(attack_checkins_for_implant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


