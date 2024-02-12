# IpPatchOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records affected by PATCH | [optional] 

## Example

```python
from randori_api_sdk.models.ip_patch_output import IpPatchOutput

# TODO update the JSON string below
json = "{}"
# create an instance of IpPatchOutput from a JSON string
ip_patch_output_instance = IpPatchOutput.from_json(json)
# print the JSON string representation of the object
print IpPatchOutput.to_json()

# convert the object into a dict
ip_patch_output_dict = ip_patch_output_instance.to_dict()
# create an instance of IpPatchOutput from a dict
ip_patch_output_form_dict = ip_patch_output.from_dict(ip_patch_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


