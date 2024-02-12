# StatisticsGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[Statistics]**](Statistics.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.statistics_get_output import StatisticsGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsGetOutput from a JSON string
statistics_get_output_instance = StatisticsGetOutput.from_json(json)
# print the JSON string representation of the object
print StatisticsGetOutput.to_json()

# convert the object into a dict
statistics_get_output_dict = statistics_get_output_instance.to_dict()
# create an instance of StatisticsGetOutput from a dict
statistics_get_output_form_dict = statistics_get_output.from_dict(statistics_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


