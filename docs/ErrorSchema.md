# ErrorSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | explaination of the error | [optional] 
**ref** | **str** | internal reference id for Randori support to track this error | [optional] 

## Example

```python
from randori_api_sdk.models.error_schema import ErrorSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorSchema from a JSON string
error_schema_instance = ErrorSchema.from_json(json)
# print the JSON string representation of the object
print ErrorSchema.to_json()

# convert the object into a dict
error_schema_dict = error_schema_instance.to_dict()
# create an instance of ErrorSchema from a dict
error_schema_form_dict = error_schema.from_dict(error_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


