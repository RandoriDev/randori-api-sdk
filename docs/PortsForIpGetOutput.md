# PortsForIpGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[PortsForIp]**](PortsForIp.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.ports_for_ip_get_output import PortsForIpGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of PortsForIpGetOutput from a JSON string
ports_for_ip_get_output_instance = PortsForIpGetOutput.from_json(json)
# print the JSON string representation of the object
print PortsForIpGetOutput.to_json()

# convert the object into a dict
ports_for_ip_get_output_dict = ports_for_ip_get_output_instance.to_dict()
# create an instance of PortsForIpGetOutput from a dict
ports_for_ip_get_output_form_dict = ports_for_ip_get_output.from_dict(ports_for_ip_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


