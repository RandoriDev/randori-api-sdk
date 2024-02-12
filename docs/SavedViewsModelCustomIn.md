# SavedViewsModelCustomIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**entity_type** | **str** |  | 
**filter_data** | **object** |  | 
**is_favorite** | **bool** |  | [optional] 
**is_global** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**sort_data** | **object** |  | 

## Example

```python
from randori_api_sdk.models.saved_views_model_custom_in import SavedViewsModelCustomIn

# TODO update the JSON string below
json = "{}"
# create an instance of SavedViewsModelCustomIn from a JSON string
saved_views_model_custom_in_instance = SavedViewsModelCustomIn.from_json(json)
# print the JSON string representation of the object
print SavedViewsModelCustomIn.to_json()

# convert the object into a dict
saved_views_model_custom_in_dict = saved_views_model_custom_in_instance.to_dict()
# create an instance of SavedViewsModelCustomIn from a dict
saved_views_model_custom_in_form_dict = saved_views_model_custom_in.from_dict(saved_views_model_custom_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


