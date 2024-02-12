# ExternalCommentCreationSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **object** |  | [optional] 
**comment** | **str** |  | 
**entity_ids** | **List[str]** |  | [optional] 

## Example

```python
from randori_api_sdk.models.external_comment_creation_schema import ExternalCommentCreationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalCommentCreationSchema from a JSON string
external_comment_creation_schema_instance = ExternalCommentCreationSchema.from_json(json)
# print the JSON string representation of the object
print ExternalCommentCreationSchema.to_json()

# convert the object into a dict
external_comment_creation_schema_dict = external_comment_creation_schema_instance.to_dict()
# create an instance of ExternalCommentCreationSchema from a dict
external_comment_creation_schema_form_dict = external_comment_creation_schema.from_dict(external_comment_creation_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


