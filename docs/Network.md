# Network


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
**id** | **str** |  | 
**impact_score** | **str** |  | [optional] 
**ip_count** | **float** |  | [optional] 
**last_seen** | **datetime** |  | [optional] 
**lens_id** | **str** |  | [optional] 
**lens_view** | **str** |  | [optional] 
**max_confidence** | **int** |  | [optional] 
**network** | **str** |  | [optional] 
**network_str** | **str** |  | [optional] 
**only_in_review_targets** | **bool** |  | [optional] 
**open_port_count** | **int** |  | [optional] 
**org_id** | **str** |  | 
**perspective** | **str** |  | [optional] 
**perspective_name** | **str** |  | [optional] 
**priority_impact_factor** | **float** |  | [optional] 
**priority_score** | **float** |  | [optional] 
**priority_status_factor** | **float** |  | [optional] 
**priority_tags_factor** | **float** |  | [optional] 
**service_count** | **float** |  | [optional] 
**status** | **str** |  | [optional] 
**target_count** | **float** |  | [optional] 
**target_temptation** | **int** |  | [optional] 
**user_tags** | **List[str]** |  | [optional] 

## Example

```python
from randori_api_sdk.models.network import Network

# TODO update the JSON string below
json = "{}"
# create an instance of Network from a JSON string
network_instance = Network.from_json(json)
# print the JSON string representation of the object
print Network.to_json()

# convert the object into a dict
network_dict = network_instance.to_dict()
# create an instance of Network from a dict
network_form_dict = network.from_dict(network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


