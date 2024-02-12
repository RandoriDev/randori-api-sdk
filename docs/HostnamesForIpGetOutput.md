# HostnamesForIpGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[HostnamesForIp]**](HostnamesForIp.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.hostnames_for_ip_get_output import HostnamesForIpGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of HostnamesForIpGetOutput from a JSON string
hostnames_for_ip_get_output_instance = HostnamesForIpGetOutput.from_json(json)
# print the JSON string representation of the object
print HostnamesForIpGetOutput.to_json()

# convert the object into a dict
hostnames_for_ip_get_output_dict = hostnames_for_ip_get_output_instance.to_dict()
# create an instance of HostnamesForIpGetOutput from a dict
hostnames_for_ip_get_output_form_dict = hostnames_for_ip_get_output.from_dict(hostnames_for_ip_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


