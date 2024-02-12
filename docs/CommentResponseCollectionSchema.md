# CommentResponseCollectionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**List[CommentResponseSchema]**](CommentResponseSchema.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.comment_response_collection_schema import CommentResponseCollectionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CommentResponseCollectionSchema from a JSON string
comment_response_collection_schema_instance = CommentResponseCollectionSchema.from_json(json)
# print the JSON string representation of the object
print CommentResponseCollectionSchema.to_json()

# convert the object into a dict
comment_response_collection_schema_dict = comment_response_collection_schema_instance.to_dict()
# create an instance of CommentResponseCollectionSchema from a dict
comment_response_collection_schema_form_dict = comment_response_collection_schema.from_dict(comment_response_collection_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


