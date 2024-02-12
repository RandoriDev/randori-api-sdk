# OrganizationGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[Organization]**](Organization.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.organization_get_output import OrganizationGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationGetOutput from a JSON string
organization_get_output_instance = OrganizationGetOutput.from_json(json)
# print the JSON string representation of the object
print OrganizationGetOutput.to_json()

# convert the object into a dict
organization_get_output_dict = organization_get_output_instance.to_dict()
# create an instance of OrganizationGetOutput from a dict
organization_get_output_form_dict = organization_get_output.from_dict(organization_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


