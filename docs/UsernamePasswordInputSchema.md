# UsernamePasswordInputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 
**username** | **str** |  | 

## Example

```python
from randori_api_sdk.models.username_password_input_schema import UsernamePasswordInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UsernamePasswordInputSchema from a JSON string
username_password_input_schema_instance = UsernamePasswordInputSchema.from_json(json)
# print the JSON string representation of the object
print UsernamePasswordInputSchema.to_json()

# convert the object into a dict
username_password_input_schema_dict = username_password_input_schema_instance.to_dict()
# create an instance of UsernamePasswordInputSchema from a dict
username_password_input_schema_form_dict = username_password_input_schema.from_dict(username_password_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


