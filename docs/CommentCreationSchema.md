# CommentCreationSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | 

## Example

```python
from randori_api_sdk.models.comment_creation_schema import CommentCreationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CommentCreationSchema from a JSON string
comment_creation_schema_instance = CommentCreationSchema.from_json(json)
# print the JSON string representation of the object
print CommentCreationSchema.to_json()

# convert the object into a dict
comment_creation_schema_dict = comment_creation_schema_instance.to_dict()
# create an instance of CommentCreationSchema from a dict
comment_creation_schema_form_dict = comment_creation_schema.from_dict(comment_creation_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


