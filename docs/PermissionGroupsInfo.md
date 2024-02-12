# PermissionGroupsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**perm_group_info** | [**List[PermissionGroupInfo]**](PermissionGroupInfo.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.permission_groups_info import PermissionGroupsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionGroupsInfo from a JSON string
permission_groups_info_instance = PermissionGroupsInfo.from_json(json)
# print the JSON string representation of the object
print PermissionGroupsInfo.to_json()

# convert the object into a dict
permission_groups_info_dict = permission_groups_info_instance.to_dict()
# create an instance of PermissionGroupsInfo from a dict
permission_groups_info_form_dict = permission_groups_info.from_dict(permission_groups_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


