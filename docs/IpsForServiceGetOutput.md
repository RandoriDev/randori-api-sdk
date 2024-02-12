# IpsForServiceGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[IpsForService]**](IpsForService.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.ips_for_service_get_output import IpsForServiceGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of IpsForServiceGetOutput from a JSON string
ips_for_service_get_output_instance = IpsForServiceGetOutput.from_json(json)
# print the JSON string representation of the object
print IpsForServiceGetOutput.to_json()

# convert the object into a dict
ips_for_service_get_output_dict = ips_for_service_get_output_instance.to_dict()
# create an instance of IpsForServiceGetOutput from a dict
ips_for_service_get_output_form_dict = ips_for_service_get_output.from_dict(ips_for_service_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


