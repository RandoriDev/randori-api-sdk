# SocialEntityPatchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SocialEntityPatchIn**](SocialEntityPatchIn.md) |  | [optional] 
**operations** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) |  | [optional] 
**q** | [**QuerybuilderRuleGroupSchema**](QuerybuilderRuleGroupSchema.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.social_entity_patch_input import SocialEntityPatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of SocialEntityPatchInput from a JSON string
social_entity_patch_input_instance = SocialEntityPatchInput.from_json(json)
# print the JSON string representation of the object
print SocialEntityPatchInput.to_json()

# convert the object into a dict
social_entity_patch_input_dict = social_entity_patch_input_instance.to_dict()
# create an instance of SocialEntityPatchInput from a dict
social_entity_patch_input_form_dict = social_entity_patch_input.from_dict(social_entity_patch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


