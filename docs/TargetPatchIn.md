# TargetPatchIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliation_state** | **str** |  | [optional] 
**authorization_state** | **str** |  | [optional] 
**impact_score** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.target_patch_in import TargetPatchIn

# TODO update the JSON string below
json = "{}"
# create an instance of TargetPatchIn from a JSON string
target_patch_in_instance = TargetPatchIn.from_json(json)
# print the JSON string representation of the object
print TargetPatchIn.to_json()

# convert the object into a dict
target_patch_in_dict = target_patch_in_instance.to_dict()
# create an instance of TargetPatchIn from a dict
target_patch_in_form_dict = target_patch_in.from_dict(target_patch_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


