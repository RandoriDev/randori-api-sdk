# IpGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[Ip]**](Ip.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.ip_get_output import IpGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of IpGetOutput from a JSON string
ip_get_output_instance = IpGetOutput.from_json(json)
# print the JSON string representation of the object
print IpGetOutput.to_json()

# convert the object into a dict
ip_get_output_dict = ip_get_output_instance.to_dict()
# create an instance of IpGetOutput from a dict
ip_get_output_form_dict = ip_get_output.from_dict(ip_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


