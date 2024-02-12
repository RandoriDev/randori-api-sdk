# HostnamesForIp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliation_state** | **str** |  | [optional] 
**confidence** | **int** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**hostname** | **str** |  | [optional] 
**hostname_id** | **str** |  | [optional] 
**id** | **str** |  | 
**impact_score** | **str** |  | [optional] 
**ip_id** | **str** |  | [optional] 
**last_seen** | **datetime** |  | [optional] 
**lens_id** | **str** |  | [optional] 
**lens_view** | **str** |  | [optional] 
**org_id** | **str** |  | 
**perspective** | **str** |  | [optional] 
**perspective_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.hostnames_for_ip import HostnamesForIp

# TODO update the JSON string below
json = "{}"
# create an instance of HostnamesForIp from a JSON string
hostnames_for_ip_instance = HostnamesForIp.from_json(json)
# print the JSON string representation of the object
print HostnamesForIp.to_json()

# convert the object into a dict
hostnames_for_ip_dict = hostnames_for_ip_instance.to_dict()
# create an instance of HostnamesForIp from a dict
hostnames_for_ip_form_dict = hostnames_for_ip.from_dict(hostnames_for_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


