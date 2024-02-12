# PathsOutputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PathsDataSchema**](PathsDataSchema.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.paths_output_schema import PathsOutputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PathsOutputSchema from a JSON string
paths_output_schema_instance = PathsOutputSchema.from_json(json)
# print the JSON string representation of the object
print PathsOutputSchema.to_json()

# convert the object into a dict
paths_output_schema_dict = paths_output_schema_instance.to_dict()
# create an instance of PathsOutputSchema from a dict
paths_output_schema_form_dict = paths_output_schema.from_dict(paths_output_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


