# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_login** | **datetime** |  | [optional] 
**lock_expiry** | **datetime** |  | [optional] 
**lock_reason** | **str** |  | [optional] 
**locked** | **bool** |  | [optional] 
**login_type** | **str** |  | [optional] 
**managed_personnel** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**password_failures** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**tos_date** | **datetime** |  | [optional] 
**tos_version** | **int** |  | [optional] 
**totp_failures** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**view_org** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


