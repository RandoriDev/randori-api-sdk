# HostnamePatchOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records affected by PATCH | [optional] 

## Example

```python
from randori_api_sdk.models.hostname_patch_output import HostnamePatchOutput

# TODO update the JSON string below
json = "{}"
# create an instance of HostnamePatchOutput from a JSON string
hostname_patch_output_instance = HostnamePatchOutput.from_json(json)
# print the JSON string representation of the object
print HostnamePatchOutput.to_json()

# convert the object into a dict
hostname_patch_output_dict = hostname_patch_output_instance.to_dict()
# create an instance of HostnamePatchOutput from a dict
hostname_patch_output_form_dict = hostname_patch_output.from_dict(hostname_patch_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


