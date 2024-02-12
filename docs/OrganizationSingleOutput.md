# OrganizationSingleOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Organization**](Organization.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.organization_single_output import OrganizationSingleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSingleOutput from a JSON string
organization_single_output_instance = OrganizationSingleOutput.from_json(json)
# print the JSON string representation of the object
print OrganizationSingleOutput.to_json()

# convert the object into a dict
organization_single_output_dict = organization_single_output_instance.to_dict()
# create an instance of OrganizationSingleOutput from a dict
organization_single_output_form_dict = organization_single_output.from_dict(organization_single_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


