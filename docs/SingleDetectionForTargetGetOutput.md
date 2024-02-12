# SingleDetectionForTargetGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[SingleDetectionForTarget]**](SingleDetectionForTarget.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.single_detection_for_target_get_output import SingleDetectionForTargetGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SingleDetectionForTargetGetOutput from a JSON string
single_detection_for_target_get_output_instance = SingleDetectionForTargetGetOutput.from_json(json)
# print the JSON string representation of the object
print SingleDetectionForTargetGetOutput.to_json()

# convert the object into a dict
single_detection_for_target_get_output_dict = single_detection_for_target_get_output_instance.to_dict()
# create an instance of SingleDetectionForTargetGetOutput from a dict
single_detection_for_target_get_output_form_dict = single_detection_for_target_get_output.from_dict(single_detection_for_target_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


