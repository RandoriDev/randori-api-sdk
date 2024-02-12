# SocialEntityPatchOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records affected by PATCH | [optional] 

## Example

```python
from randori_api_sdk.models.social_entity_patch_output import SocialEntityPatchOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SocialEntityPatchOutput from a JSON string
social_entity_patch_output_instance = SocialEntityPatchOutput.from_json(json)
# print the JSON string representation of the object
print SocialEntityPatchOutput.to_json()

# convert the object into a dict
social_entity_patch_output_dict = social_entity_patch_output_instance.to_dict()
# create an instance of SocialEntityPatchOutput from a dict
social_entity_patch_output_form_dict = social_entity_patch_output.from_dict(social_entity_patch_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


