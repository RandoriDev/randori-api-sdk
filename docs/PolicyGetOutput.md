# PolicyGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[Policy]**](Policy.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.policy_get_output import PolicyGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyGetOutput from a JSON string
policy_get_output_instance = PolicyGetOutput.from_json(json)
# print the JSON string representation of the object
print PolicyGetOutput.to_json()

# convert the object into a dict
policy_get_output_dict = policy_get_output_instance.to_dict()
# create an instance of PolicyGetOutput from a dict
policy_get_output_form_dict = policy_get_output.from_dict(policy_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


