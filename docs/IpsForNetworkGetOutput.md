# IpsForNetworkGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[IpsForNetwork]**](IpsForNetwork.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.ips_for_network_get_output import IpsForNetworkGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of IpsForNetworkGetOutput from a JSON string
ips_for_network_get_output_instance = IpsForNetworkGetOutput.from_json(json)
# print the JSON string representation of the object
print IpsForNetworkGetOutput.to_json()

# convert the object into a dict
ips_for_network_get_output_dict = ips_for_network_get_output_instance.to_dict()
# create an instance of IpsForNetworkGetOutput from a dict
ips_for_network_get_output_form_dict = ips_for_network_get_output.from_dict(ips_for_network_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


