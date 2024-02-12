# SocialEntityPatchIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliation_state** | **str** |  | [optional] 
**authorization_state** | **str** |  | [optional] 
**impact_score** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.social_entity_patch_in import SocialEntityPatchIn

# TODO update the JSON string below
json = "{}"
# create an instance of SocialEntityPatchIn from a JSON string
social_entity_patch_in_instance = SocialEntityPatchIn.from_json(json)
# print the JSON string representation of the object
print SocialEntityPatchIn.to_json()

# convert the object into a dict
social_entity_patch_in_dict = social_entity_patch_in_instance.to_dict()
# create an instance of SocialEntityPatchIn from a dict
social_entity_patch_in_form_dict = social_entity_patch_in.from_dict(social_entity_patch_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


