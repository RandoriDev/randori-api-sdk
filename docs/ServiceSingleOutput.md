# ServiceSingleOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Service**](Service.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.service_single_output import ServiceSingleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSingleOutput from a JSON string
service_single_output_instance = ServiceSingleOutput.from_json(json)
# print the JSON string representation of the object
print ServiceSingleOutput.to_json()

# convert the object into a dict
service_single_output_dict = service_single_output_instance.to_dict()
# create an instance of ServiceSingleOutput from a dict
service_single_output_form_dict = service_single_output.from_dict(service_single_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


