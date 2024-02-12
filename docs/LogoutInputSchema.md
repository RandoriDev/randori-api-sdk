# LogoutInputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jti** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.logout_input_schema import LogoutInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LogoutInputSchema from a JSON string
logout_input_schema_instance = LogoutInputSchema.from_json(json)
# print the JSON string representation of the object
print LogoutInputSchema.to_json()

# convert the object into a dict
logout_input_schema_dict = logout_input_schema_instance.to_dict()
# create an instance of LogoutInputSchema from a dict
logout_input_schema_form_dict = logout_input_schema.from_dict(logout_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


