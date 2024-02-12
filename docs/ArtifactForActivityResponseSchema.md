# ArtifactForActivityResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_description** | **str** |  | [optional] 
**artifact_renderer** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**filename** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_renderable** | **bool** |  | [optional] 
**org_id** | **str** |  | [optional] 
**renderable_metadata** | **object** |  | [optional] 
**shasum** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from randori_api_sdk.models.artifact_for_activity_response_schema import ArtifactForActivityResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactForActivityResponseSchema from a JSON string
artifact_for_activity_response_schema_instance = ArtifactForActivityResponseSchema.from_json(json)
# print the JSON string representation of the object
print ArtifactForActivityResponseSchema.to_json()

# convert the object into a dict
artifact_for_activity_response_schema_dict = artifact_for_activity_response_schema_instance.to_dict()
# create an instance of ArtifactForActivityResponseSchema from a dict
artifact_for_activity_response_schema_form_dict = artifact_for_activity_response_schema.from_dict(artifact_for_activity_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


