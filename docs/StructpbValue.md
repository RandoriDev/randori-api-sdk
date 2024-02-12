# StructpbValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **object** | The kind of value.  Types that are assignable to Kind:   *Value_NullValue  *Value_NumberValue  *Value_StringValue  *Value_BoolValue  *Value_StructValue  *Value_ListValue | [optional] 

## Example

```python
from randori_api_sdk.models.structpb_value import StructpbValue

# TODO update the JSON string below
json = "{}"
# create an instance of StructpbValue from a JSON string
structpb_value_instance = StructpbValue.from_json(json)
# print the JSON string representation of the object
print StructpbValue.to_json()

# convert the object into a dict
structpb_value_dict = structpb_value_instance.to_dict()
# create an instance of StructpbValue from a dict
structpb_value_form_dict = structpb_value.from_dict(structpb_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


