# TargetPatchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TargetPatchIn**](TargetPatchIn.md) |  | [optional] 
**operations** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) |  | [optional] 
**q** | [**QuerybuilderRuleGroupSchema**](QuerybuilderRuleGroupSchema.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.target_patch_input import TargetPatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of TargetPatchInput from a JSON string
target_patch_input_instance = TargetPatchInput.from_json(json)
# print the JSON string representation of the object
print TargetPatchInput.to_json()

# convert the object into a dict
target_patch_input_dict = target_patch_input_instance.to_dict()
# create an instance of TargetPatchInput from a dict
target_patch_input_form_dict = target_patch_input.from_dict(target_patch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


