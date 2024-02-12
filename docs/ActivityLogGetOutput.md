# ActivityLogGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[ActivityLog]**](ActivityLog.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.activity_log_get_output import ActivityLogGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityLogGetOutput from a JSON string
activity_log_get_output_instance = ActivityLogGetOutput.from_json(json)
# print the JSON string representation of the object
print ActivityLogGetOutput.to_json()

# convert the object into a dict
activity_log_get_output_dict = activity_log_get_output_instance.to_dict()
# create an instance of ActivityLogGetOutput from a dict
activity_log_get_output_form_dict = activity_log_get_output.from_dict(activity_log_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


