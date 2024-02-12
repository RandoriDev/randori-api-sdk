# SavedViewsPatchSingleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SavedViewsPatchIn**](SavedViewsPatchIn.md) |  | [optional] 
**org_id** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.saved_views_patch_single_input import SavedViewsPatchSingleInput

# TODO update the JSON string below
json = "{}"
# create an instance of SavedViewsPatchSingleInput from a JSON string
saved_views_patch_single_input_instance = SavedViewsPatchSingleInput.from_json(json)
# print the JSON string representation of the object
print SavedViewsPatchSingleInput.to_json()

# convert the object into a dict
saved_views_patch_single_input_dict = saved_views_patch_single_input_instance.to_dict()
# create an instance of SavedViewsPatchSingleInput from a dict
saved_views_patch_single_input_form_dict = saved_views_patch_single_input.from_dict(saved_views_patch_single_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


