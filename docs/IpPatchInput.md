# IpPatchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IpPatchIn**](IpPatchIn.md) |  | [optional] 
**operations** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) |  | [optional] 
**q** | [**QuerybuilderRuleGroupSchema**](QuerybuilderRuleGroupSchema.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.ip_patch_input import IpPatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of IpPatchInput from a JSON string
ip_patch_input_instance = IpPatchInput.from_json(json)
# print the JSON string representation of the object
print IpPatchInput.to_json()

# convert the object into a dict
ip_patch_input_dict = ip_patch_input_instance.to_dict()
# create an instance of IpPatchInput from a dict
ip_patch_input_form_dict = ip_patch_input.from_dict(ip_patch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


