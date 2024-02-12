# HostnamePatchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**HostnamePatchIn**](HostnamePatchIn.md) |  | [optional] 
**operations** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) |  | [optional] 
**q** | [**QuerybuilderRuleGroupSchema**](QuerybuilderRuleGroupSchema.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.hostname_patch_input import HostnamePatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of HostnamePatchInput from a JSON string
hostname_patch_input_instance = HostnamePatchInput.from_json(json)
# print the JSON string representation of the object
print HostnamePatchInput.to_json()

# convert the object into a dict
hostname_patch_input_dict = hostname_patch_input_instance.to_dict()
# create an instance of HostnamePatchInput from a dict
hostname_patch_input_form_dict = hostname_patch_input.from_dict(hostname_patch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


