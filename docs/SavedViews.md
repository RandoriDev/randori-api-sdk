# SavedViews


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**description** | **str** |  | [optional] 
**edited_at** | **datetime** |  | 
**entity_type** | **str** |  | 
**filter_data** | **object** |  | 
**id** | **str** |  | [optional] 
**is_favorite** | **bool** |  | [optional] 
**is_global** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**sort_data** | **object** |  | 

## Example

```python
from randori_api_sdk.models.saved_views import SavedViews

# TODO update the JSON string below
json = "{}"
# create an instance of SavedViews from a JSON string
saved_views_instance = SavedViews.from_json(json)
# print the JSON string representation of the object
print SavedViews.to_json()

# convert the object into a dict
saved_views_dict = saved_views_instance.to_dict()
# create an instance of SavedViews from a dict
saved_views_form_dict = saved_views.from_dict(saved_views_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


