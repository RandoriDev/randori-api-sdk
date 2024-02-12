# HostnamePatchIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliation_state** | **str** |  | [optional] 
**impact_score** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.hostname_patch_in import HostnamePatchIn

# TODO update the JSON string below
json = "{}"
# create an instance of HostnamePatchIn from a JSON string
hostname_patch_in_instance = HostnamePatchIn.from_json(json)
# print the JSON string representation of the object
print HostnamePatchIn.to_json()

# convert the object into a dict
hostname_patch_in_dict = hostname_patch_in_instance.to_dict()
# create an instance of HostnamePatchIn from a dict
hostname_patch_in_form_dict = hostname_patch_in.from_dict(hostname_patch_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


