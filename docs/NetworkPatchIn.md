# NetworkPatchIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliation_state** | **str** |  | [optional] 
**impact_score** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.network_patch_in import NetworkPatchIn

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkPatchIn from a JSON string
network_patch_in_instance = NetworkPatchIn.from_json(json)
# print the JSON string representation of the object
print NetworkPatchIn.to_json()

# convert the object into a dict
network_patch_in_dict = network_patch_in_instance.to_dict()
# create an instance of NetworkPatchIn from a dict
network_patch_in_form_dict = network_patch_in.from_dict(network_patch_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


