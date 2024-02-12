# PathsDataSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edges** | [**Dict[str, PathDrSchema]**](PathDrSchema.md) |  | [optional] 
**nodes** | [**Dict[str, PathEntitySchema]**](PathEntitySchema.md) |  | [optional] 
**paths** | **List[List[str]]** |  | [optional] 

## Example

```python
from randori_api_sdk.models.paths_data_schema import PathsDataSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PathsDataSchema from a JSON string
paths_data_schema_instance = PathsDataSchema.from_json(json)
# print the JSON string representation of the object
print PathsDataSchema.to_json()

# convert the object into a dict
paths_data_schema_dict = paths_data_schema_instance.to_dict()
# create an instance of PathsDataSchema from a dict
paths_data_schema_form_dict = paths_data_schema.from_dict(paths_data_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


