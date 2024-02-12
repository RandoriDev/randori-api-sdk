# UserGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[User]**](User.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.user_get_output import UserGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetOutput from a JSON string
user_get_output_instance = UserGetOutput.from_json(json)
# print the JSON string representation of the object
print UserGetOutput.to_json()

# convert the object into a dict
user_get_output_dict = user_get_output_instance.to_dict()
# create an instance of UserGetOutput from a dict
user_get_output_form_dict = user_get_output.from_dict(user_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


