# TokenInputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 

## Example

```python
from randori_api_sdk.models.token_input_schema import TokenInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInputSchema from a JSON string
token_input_schema_instance = TokenInputSchema.from_json(json)
# print the JSON string representation of the object
print TokenInputSchema.to_json()

# convert the object into a dict
token_input_schema_dict = token_input_schema_instance.to_dict()
# create an instance of TokenInputSchema from a dict
token_input_schema_form_dict = token_input_schema.from_dict(token_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


