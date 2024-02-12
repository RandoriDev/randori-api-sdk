# CommentResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **object** |  | [optional] 
**comment** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**is_author** | **bool** |  | [optional] 
**is_bulk_applied** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**rel_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.comment_response_schema import CommentResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CommentResponseSchema from a JSON string
comment_response_schema_instance = CommentResponseSchema.from_json(json)
# print the JSON string representation of the object
print CommentResponseSchema.to_json()

# convert the object into a dict
comment_response_schema_dict = comment_response_schema_instance.to_dict()
# create an instance of CommentResponseSchema from a dict
comment_response_schema_form_dict = comment_response_schema.from_dict(comment_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


