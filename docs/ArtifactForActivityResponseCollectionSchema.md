# ArtifactForActivityResponseCollectionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**data** | [**List[ArtifactForActivityResponseSchema]**](ArtifactForActivityResponseSchema.md) |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from randori_api_sdk.models.artifact_for_activity_response_collection_schema import ArtifactForActivityResponseCollectionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactForActivityResponseCollectionSchema from a JSON string
artifact_for_activity_response_collection_schema_instance = ArtifactForActivityResponseCollectionSchema.from_json(json)
# print the JSON string representation of the object
print ArtifactForActivityResponseCollectionSchema.to_json()

# convert the object into a dict
artifact_for_activity_response_collection_schema_dict = artifact_for_activity_response_collection_schema_instance.to_dict()
# create an instance of ArtifactForActivityResponseCollectionSchema from a dict
artifact_for_activity_response_collection_schema_form_dict = artifact_for_activity_response_collection_schema.from_dict(artifact_for_activity_response_collection_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


