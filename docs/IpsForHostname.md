# IpsForHostname


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliation_state** | **str** |  | [optional] 
**confidence** | **int** |  | [optional] 
**country** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**hostname_id** | **str** |  | [optional] 
**id** | **str** |  | 
**impact_score** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**ip_id** | **str** |  | [optional] 
**ip_str** | **str** |  | [optional] 
**last_seen** | **datetime** |  | [optional] 
**latitude** | **float** |  | [optional] 
**lens_id** | **str** |  | [optional] 
**lens_view** | **str** |  | [optional] 
**longitude** | **float** |  | [optional] 
**open_port_count** | **int** |  | [optional] 
**org_id** | **str** |  | 
**perspective** | **str** |  | [optional] 
**perspective_name** | **str** |  | [optional] 
**radius** | **float** |  | [optional] 
**service_count** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**target_count** | **int** |  | [optional] 
**target_temptation** | **int** |  | [optional] 
**top_hostname** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.ips_for_hostname import IpsForHostname

# TODO update the JSON string below
json = "{}"
# create an instance of IpsForHostname from a JSON string
ips_for_hostname_instance = IpsForHostname.from_json(json)
# print the JSON string representation of the object
print IpsForHostname.to_json()

# convert the object into a dict
ips_for_hostname_dict = ips_for_hostname_instance.to_dict()
# create an instance of IpsForHostname from a dict
ips_for_hostname_form_dict = ips_for_hostname.from_dict(ips_for_hostname_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


