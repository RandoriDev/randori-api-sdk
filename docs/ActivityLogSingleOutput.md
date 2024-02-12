# ActivityLogSingleOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ActivityLog**](ActivityLog.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.activity_log_single_output import ActivityLogSingleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityLogSingleOutput from a JSON string
activity_log_single_output_instance = ActivityLogSingleOutput.from_json(json)
# print the JSON string representation of the object
print ActivityLogSingleOutput.to_json()

# convert the object into a dict
activity_log_single_output_dict = activity_log_single_output_instance.to_dict()
# create an instance of ActivityLogSingleOutput from a dict
activity_log_single_output_form_dict = activity_log_single_output.from_dict(activity_log_single_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


