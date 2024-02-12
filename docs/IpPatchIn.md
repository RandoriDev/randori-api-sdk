# IpPatchIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliation_state** | **str** |  | [optional] 
**impact_score** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.ip_patch_in import IpPatchIn

# TODO update the JSON string below
json = "{}"
# create an instance of IpPatchIn from a JSON string
ip_patch_in_instance = IpPatchIn.from_json(json)
# print the JSON string representation of the object
print IpPatchIn.to_json()

# convert the object into a dict
ip_patch_in_dict = ip_patch_in_instance.to_dict()
# create an instance of IpPatchIn from a dict
ip_patch_in_form_dict = ip_patch_in.from_dict(ip_patch_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


