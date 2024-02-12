# Tagcounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_count** | **int** |  | 
**content** | **str** |  | 
**hostname_count** | **int** |  | 
**id** | **str** |  | 
**ip_count** | **int** |  | 
**is_characteristic_tag** | **bool** |  | 
**network_count** | **int** |  | 
**org_id** | **str** |  | 
**poc_count** | **int** |  | 
**service_count** | **int** |  | 
**target_count** | **int** |  | 

## Example

```python
from randori_api_sdk.models.tagcounts import Tagcounts

# TODO update the JSON string below
json = "{}"
# create an instance of Tagcounts from a JSON string
tagcounts_instance = Tagcounts.from_json(json)
# print the JSON string representation of the object
print Tagcounts.to_json()

# convert the object into a dict
tagcounts_dict = tagcounts_instance.to_dict()
# create an instance of Tagcounts from a dict
tagcounts_form_dict = tagcounts.from_dict(tagcounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


