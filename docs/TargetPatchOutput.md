# TargetPatchOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records affected by PATCH | [optional] 

## Example

```python
from randori_api_sdk.models.target_patch_output import TargetPatchOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TargetPatchOutput from a JSON string
target_patch_output_instance = TargetPatchOutput.from_json(json)
# print the JSON string representation of the object
print TargetPatchOutput.to_json()

# convert the object into a dict
target_patch_output_dict = target_patch_output_instance.to_dict()
# create an instance of TargetPatchOutput from a dict
target_patch_output_form_dict = target_patch_output.from_dict(target_patch_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


