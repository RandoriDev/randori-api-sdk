# UserPatchSingleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed_password** | **str** |  | [optional] 
**data** | [**UserPatchIn**](UserPatchIn.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.user_patch_single_input import UserPatchSingleInput

# TODO update the JSON string below
json = "{}"
# create an instance of UserPatchSingleInput from a JSON string
user_patch_single_input_instance = UserPatchSingleInput.from_json(json)
# print the JSON string representation of the object
print UserPatchSingleInput.to_json()

# convert the object into a dict
user_patch_single_input_dict = user_patch_single_input_instance.to_dict()
# create an instance of UserPatchSingleInput from a dict
user_patch_single_input_form_dict = user_patch_single_input.from_dict(user_patch_single_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


