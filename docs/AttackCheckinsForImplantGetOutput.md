# AttackCheckinsForImplantGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[AttackCheckinsForImplant]**](AttackCheckinsForImplant.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.attack_checkins_for_implant_get_output import AttackCheckinsForImplantGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AttackCheckinsForImplantGetOutput from a JSON string
attack_checkins_for_implant_get_output_instance = AttackCheckinsForImplantGetOutput.from_json(json)
# print the JSON string representation of the object
print AttackCheckinsForImplantGetOutput.to_json()

# convert the object into a dict
attack_checkins_for_implant_get_output_dict = attack_checkins_for_implant_get_output_instance.to_dict()
# create an instance of AttackCheckinsForImplantGetOutput from a dict
attack_checkins_for_implant_get_output_form_dict = attack_checkins_for_implant_get_output.from_dict(attack_checkins_for_implant_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


