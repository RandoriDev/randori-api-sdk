# HostnameGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[Hostname]**](Hostname.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.hostname_get_output import HostnameGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of HostnameGetOutput from a JSON string
hostname_get_output_instance = HostnameGetOutput.from_json(json)
# print the JSON string representation of the object
print HostnameGetOutput.to_json()

# convert the object into a dict
hostname_get_output_dict = hostname_get_output_instance.to_dict()
# create an instance of HostnameGetOutput from a dict
hostname_get_output_form_dict = hostname_get_output.from_dict(hostname_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


