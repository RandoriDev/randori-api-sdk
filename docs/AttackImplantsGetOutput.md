# AttackImplantsGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[AttackImplants]**](AttackImplants.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.attack_implants_get_output import AttackImplantsGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AttackImplantsGetOutput from a JSON string
attack_implants_get_output_instance = AttackImplantsGetOutput.from_json(json)
# print the JSON string representation of the object
print AttackImplantsGetOutput.to_json()

# convert the object into a dict
attack_implants_get_output_dict = attack_implants_get_output_instance.to_dict()
# create an instance of AttackImplantsGetOutput from a dict
attack_implants_get_output_form_dict = attack_implants_get_output.from_dict(attack_implants_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


