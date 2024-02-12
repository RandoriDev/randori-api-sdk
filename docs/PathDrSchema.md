# PathDrSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **object** |  | [optional] 
**dst** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**src** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.path_dr_schema import PathDrSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PathDrSchema from a JSON string
path_dr_schema_instance = PathDrSchema.from_json(json)
# print the JSON string representation of the object
print PathDrSchema.to_json()

# convert the object into a dict
path_dr_schema_dict = path_dr_schema_instance.to_dict()
# create an instance of PathDrSchema from a dict
path_dr_schema_form_dict = path_dr_schema.from_dict(path_dr_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


