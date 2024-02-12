# TargetGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[Target]**](Target.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.target_get_output import TargetGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TargetGetOutput from a JSON string
target_get_output_instance = TargetGetOutput.from_json(json)
# print the JSON string representation of the object
print TargetGetOutput.to_json()

# convert the object into a dict
target_get_output_dict = target_get_output_instance.to_dict()
# create an instance of TargetGetOutput from a dict
target_get_output_form_dict = target_get_output.from_dict(target_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


