# PermissionGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**perm_groups** | **List[object]** |  | [optional] 
**target_user_id** | **str** |  | 

## Example

```python
from randori_api_sdk.models.permission_group import PermissionGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionGroup from a JSON string
permission_group_instance = PermissionGroup.from_json(json)
# print the JSON string representation of the object
print PermissionGroup.to_json()

# convert the object into a dict
permission_group_dict = permission_group_instance.to_dict()
# create an instance of PermissionGroup from a dict
permission_group_form_dict = permission_group.from_dict(permission_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


