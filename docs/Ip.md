# Ip


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliation_state** | **str** |  | [optional] 
**all_ports** | **List[object]** |  | [optional] 
**authority** | **bool** |  | [optional] 
**authority_distance** | **int** |  | [optional] 
**authority_override** | **bool** |  | [optional] 
**characteristic_tags** | **List[str]** |  | [optional] 
**confidence** | **int** |  | [optional] 
**country** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**first_seen** | **datetime** |  | [optional] 
**hostname_count** | **int** |  | [optional] 
**hostnames** | **List[str]** |  | [optional] 
**id** | **str** |  | 
**impact_score** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**ip_str** | **str** |  | [optional] 
**last_seen** | **datetime** |  | [optional] 
**latitude** | **float** |  | [optional] 
**lens_id** | **str** |  | [optional] 
**lens_view** | **str** |  | [optional] 
**longitude** | **float** |  | [optional] 
**only_in_review_targets** | **bool** |  | [optional] 
**open_port_count** | **int** |  | [optional] 
**org_id** | **str** |  | 
**perspective** | **str** |  | [optional] 
**perspective_name** | **str** |  | [optional] 
**priority_impact_factor** | **float** |  | [optional] 
**priority_score** | **float** |  | [optional] 
**priority_status_factor** | **float** |  | [optional] 
**priority_tags_factor** | **float** |  | [optional] 
**radius** | **float** |  | [optional] 
**service_count** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**target_count** | **int** |  | [optional] 
**target_temptation** | **int** |  | [optional] 
**user_tags** | **List[str]** |  | [optional] 

## Example

```python
from randori_api_sdk.models.ip import Ip

# TODO update the JSON string below
json = "{}"
# create an instance of Ip from a JSON string
ip_instance = Ip.from_json(json)
# print the JSON string representation of the object
print Ip.to_json()

# convert the object into a dict
ip_dict = ip_instance.to_dict()
# create an instance of Ip from a dict
ip_form_dict = ip.from_dict(ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


