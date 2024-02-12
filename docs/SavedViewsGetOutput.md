# SavedViewsGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[SavedViews]**](SavedViews.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.saved_views_get_output import SavedViewsGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SavedViewsGetOutput from a JSON string
saved_views_get_output_instance = SavedViewsGetOutput.from_json(json)
# print the JSON string representation of the object
print SavedViewsGetOutput.to_json()

# convert the object into a dict
saved_views_get_output_dict = saved_views_get_output_instance.to_dict()
# create an instance of SavedViewsGetOutput from a dict
saved_views_get_output_form_dict = saved_views_get_output.from_dict(saved_views_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


