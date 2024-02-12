# ServiceGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[Service]**](Service.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.service_get_output import ServiceGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceGetOutput from a JSON string
service_get_output_instance = ServiceGetOutput.from_json(json)
# print the JSON string representation of the object
print ServiceGetOutput.to_json()

# convert the object into a dict
service_get_output_dict = service_get_output_instance.to_dict()
# create an instance of ServiceGetOutput from a dict
service_get_output_form_dict = service_get_output.from_dict(service_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


