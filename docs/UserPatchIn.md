# UserPatchIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**managed_personnel** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**tos_date** | **datetime** |  | [optional] 
**tos_version** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**view_org** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.user_patch_in import UserPatchIn

# TODO update the JSON string below
json = "{}"
# create an instance of UserPatchIn from a JSON string
user_patch_in_instance = UserPatchIn.from_json(json)
# print the JSON string representation of the object
print UserPatchIn.to_json()

# convert the object into a dict
user_patch_in_dict = user_patch_in_instance.to_dict()
# create an instance of UserPatchIn from a dict
user_patch_in_form_dict = user_patch_in.from_dict(user_patch_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


