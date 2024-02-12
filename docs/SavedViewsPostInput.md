# SavedViewsPostInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SavedViewsModelCustomIn]**](SavedViewsModelCustomIn.md) | list of objects to add to the table | [optional] 

## Example

```python
from randori_api_sdk.models.saved_views_post_input import SavedViewsPostInput

# TODO update the JSON string below
json = "{}"
# create an instance of SavedViewsPostInput from a JSON string
saved_views_post_input_instance = SavedViewsPostInput.from_json(json)
# print the JSON string representation of the object
print SavedViewsPostInput.to_json()

# convert the object into a dict
saved_views_post_input_dict = saved_views_post_input_instance.to_dict()
# create an instance of SavedViewsPostInput from a dict
saved_views_post_input_form_dict = saved_views_post_input.from_dict(saved_views_post_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


