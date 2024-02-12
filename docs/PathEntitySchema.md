# PathEntitySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.path_entity_schema import PathEntitySchema

# TODO update the JSON string below
json = "{}"
# create an instance of PathEntitySchema from a JSON string
path_entity_schema_instance = PathEntitySchema.from_json(json)
# print the JSON string representation of the object
print PathEntitySchema.to_json()

# convert the object into a dict
path_entity_schema_dict = path_entity_schema_instance.to_dict()
# create an instance of PathEntitySchema from a dict
path_entity_schema_form_dict = path_entity_schema.from_dict(path_entity_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


