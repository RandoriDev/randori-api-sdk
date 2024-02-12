# AllDetectionsForTargetGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[AllDetectionsForTarget]**](AllDetectionsForTarget.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.all_detections_for_target_get_output import AllDetectionsForTargetGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AllDetectionsForTargetGetOutput from a JSON string
all_detections_for_target_get_output_instance = AllDetectionsForTargetGetOutput.from_json(json)
# print the JSON string representation of the object
print AllDetectionsForTargetGetOutput.to_json()

# convert the object into a dict
all_detections_for_target_get_output_dict = all_detections_for_target_get_output_instance.to_dict()
# create an instance of AllDetectionsForTargetGetOutput from a dict
all_detections_for_target_get_output_form_dict = all_detections_for_target_get_output.from_dict(all_detections_for_target_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


