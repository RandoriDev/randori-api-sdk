# UserTagNameList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from randori_api_sdk.models.user_tag_name_list import UserTagNameList

# TODO update the JSON string below
json = "{}"
# create an instance of UserTagNameList from a JSON string
user_tag_name_list_instance = UserTagNameList.from_json(json)
# print the JSON string representation of the object
print UserTagNameList.to_json()

# convert the object into a dict
user_tag_name_list_dict = user_tag_name_list_instance.to_dict()
# create an instance of UserTagNameList from a dict
user_tag_name_list_form_dict = user_tag_name_list.from_dict(user_tag_name_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


