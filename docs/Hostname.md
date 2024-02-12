# Hostname


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliation_state** | **str** |  | [optional] 
**authority** | **bool** |  | [optional] 
**authority_distance** | **int** |  | [optional] 
**authority_override** | **bool** |  | [optional] 
**characteristic_tags** | **List[str]** |  | [optional] 
**confidence** | **int** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**first_seen** | **datetime** |  | [optional] 
**hostname** | **str** |  | [optional] 
**id** | **str** |  | 
**impact_score** | **str** |  | [optional] 
**ip_count** | **int** |  | [optional] 
**ips** | **List[str]** |  | [optional] 
**is_prime** | **bool** |  | [optional] 
**last_seen** | **datetime** |  | [optional] 
**lens_id** | **str** |  | [optional] 
**lens_view** | **str** |  | [optional] 
**max_confidence** | **int** |  | [optional] 
**name_type** | **int** |  | [optional] 
**only_in_review_targets** | **bool** |  | [optional] 
**org_id** | **str** |  | 
**perspective** | **str** |  | [optional] 
**perspective_name** | **str** |  | [optional] 
**priority_impact_factor** | **float** |  | [optional] 
**priority_score** | **float** |  | [optional] 
**priority_status_factor** | **float** |  | [optional] 
**priority_tags_factor** | **float** |  | [optional] 
**status** | **str** |  | [optional] 
**target_temptation** | **int** |  | [optional] 
**user_tags** | **List[str]** |  | [optional] 

## Example

```python
from randori_api_sdk.models.hostname import Hostname

# TODO update the JSON string below
json = "{}"
# create an instance of Hostname from a JSON string
hostname_instance = Hostname.from_json(json)
# print the JSON string representation of the object
print Hostname.to_json()

# convert the object into a dict
hostname_dict = hostname_instance.to_dict()
# create an instance of Hostname from a dict
hostname_form_dict = hostname.from_dict(hostname_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


