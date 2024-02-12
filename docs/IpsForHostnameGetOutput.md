# IpsForHostnameGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[IpsForHostname]**](IpsForHostname.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.ips_for_hostname_get_output import IpsForHostnameGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of IpsForHostnameGetOutput from a JSON string
ips_for_hostname_get_output_instance = IpsForHostnameGetOutput.from_json(json)
# print the JSON string representation of the object
print IpsForHostnameGetOutput.to_json()

# convert the object into a dict
ips_for_hostname_get_output_dict = ips_for_hostname_get_output_instance.to_dict()
# create an instance of IpsForHostnameGetOutput from a dict
ips_for_hostname_get_output_form_dict = ips_for_hostname_get_output.from_dict(ips_for_hostname_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


