# PortsForIp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **int** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**id** | **str** |  | 
**ip_id** | **str** |  | [optional] 
**last_seen** | **datetime** |  | [optional] 
**lens_id** | **str** |  | [optional] 
**lens_view** | **str** |  | [optional] 
**org_id** | **str** |  | 
**perspective** | **str** |  | [optional] 
**perspective_name** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**protocol** | **int** |  | [optional] 
**seen_open** | **bool** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.ports_for_ip import PortsForIp

# TODO update the JSON string below
json = "{}"
# create an instance of PortsForIp from a JSON string
ports_for_ip_instance = PortsForIp.from_json(json)
# print the JSON string representation of the object
print PortsForIp.to_json()

# convert the object into a dict
ports_for_ip_dict = ports_for_ip_instance.to_dict()
# create an instance of PortsForIp from a dict
ports_for_ip_form_dict = ports_for_ip.from_dict(ports_for_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


