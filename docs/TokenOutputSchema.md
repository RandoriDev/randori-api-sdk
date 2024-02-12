# TokenOutputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exp** | **int** |  | [optional] 
**iat** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**paying** | **bool** |  | [optional] 
**perms** | **List[str]** |  | [optional] 
**shortname** | **str** |  | [optional] 
**stasis** | **bool** |  | [optional] 
**tracking** | **bool** |  | [optional] 
**username** | **str** |  | [optional] 
**view_org** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.token_output_schema import TokenOutputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TokenOutputSchema from a JSON string
token_output_schema_instance = TokenOutputSchema.from_json(json)
# print the JSON string representation of the object
print TokenOutputSchema.to_json()

# convert the object into a dict
token_output_schema_dict = token_output_schema_instance.to_dict()
# create an instance of TokenOutputSchema from a dict
token_output_schema_form_dict = token_output_schema.from_dict(token_output_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


