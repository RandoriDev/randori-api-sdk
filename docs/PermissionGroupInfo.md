# PermissionGroupInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**perm_group_desc** | **str** |  | [optional] 
**perm_group_name** | **str** |  | [optional] 
**perm_group_type** | **object** |  | 

## Example

```python
from randori_api_sdk.models.permission_group_info import PermissionGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionGroupInfo from a JSON string
permission_group_info_instance = PermissionGroupInfo.from_json(json)
# print the JSON string representation of the object
print PermissionGroupInfo.to_json()

# convert the object into a dict
permission_group_info_dict = permission_group_info_instance.to_dict()
# create an instance of PermissionGroupInfo from a dict
permission_group_info_form_dict = permission_group_info.from_dict(permission_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


