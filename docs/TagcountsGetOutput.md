# TagcountsGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[Tagcounts]**](Tagcounts.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.tagcounts_get_output import TagcountsGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TagcountsGetOutput from a JSON string
tagcounts_get_output_instance = TagcountsGetOutput.from_json(json)
# print the JSON string representation of the object
print TagcountsGetOutput.to_json()

# convert the object into a dict
tagcounts_get_output_dict = tagcounts_get_output_instance.to_dict()
# create an instance of TagcountsGetOutput from a dict
tagcounts_get_output_form_dict = tagcounts_get_output.from_dict(tagcounts_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


