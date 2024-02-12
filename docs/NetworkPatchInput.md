# NetworkPatchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**NetworkPatchIn**](NetworkPatchIn.md) |  | [optional] 
**operations** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) |  | [optional] 
**q** | [**QuerybuilderRuleGroupSchema**](QuerybuilderRuleGroupSchema.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.network_patch_input import NetworkPatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkPatchInput from a JSON string
network_patch_input_instance = NetworkPatchInput.from_json(json)
# print the JSON string representation of the object
print NetworkPatchInput.to_json()

# convert the object into a dict
network_patch_input_dict = network_patch_input_instance.to_dict()
# create an instance of NetworkPatchInput from a dict
network_patch_input_form_dict = network_patch_input.from_dict(network_patch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


