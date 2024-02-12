# NetworkGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[Network]**](Network.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.network_get_output import NetworkGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkGetOutput from a JSON string
network_get_output_instance = NetworkGetOutput.from_json(json)
# print the JSON string representation of the object
print NetworkGetOutput.to_json()

# convert the object into a dict
network_get_output_dict = network_get_output_instance.to_dict()
# create an instance of NetworkGetOutput from a dict
network_get_output_form_dict = network_get_output.from_dict(network_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


