# AttackRunbook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**dst_email** | **List[str]** |  | [optional] 
**dst_host** | **List[str]** |  | [optional] 
**dst_ip** | **List[str]** |  | [optional] 
**dst_mac** | **List[str]** |  | [optional] 
**dst_misc** | **List[str]** |  | [optional] 
**dst_network** | **List[str]** |  | [optional] 
**dst_path** | **List[str]** |  | [optional] 
**dst_port** | **List[int]** |  | [optional] 
**dst_search** | **str** |  | 
**end_time** | **datetime** |  | [optional] 
**guidance** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**implant_ids** | **List[str]** |  | [optional] 
**implant_nick** | **str** |  | [optional] 
**implant_src_host** | **List[str]** |  | [optional] 
**implant_src_ip** | **List[str]** |  | [optional] 
**instance_label** | **str** |  | [optional] 
**name** | **str** |  | 
**objective** | **str** |  | [optional] 
**org_id** | **str** |  | 
**perspective_metadata** | **List[object]** |  | [optional] 
**randori_notes** | **str** |  | [optional] 
**results** | **str** |  | [optional] 
**runbook_id** | **str** |  | 
**src_email** | **List[str]** |  | [optional] 
**src_host** | **List[str]** |  | [optional] 
**src_ip** | **List[str]** |  | [optional] 
**src_mac** | **List[str]** |  | [optional] 
**src_misc** | **List[str]** |  | [optional] 
**src_search** | **str** |  | 
**start_time** | **datetime** |  | 
**status** | **str** |  | 
**technique_ids** | **List[str]** |  | 
**trigger** | **List[object]** |  | [optional] 
**uid** | **str** |  | 

## Example

```python
from randori_api_sdk.models.attack_runbook import AttackRunbook

# TODO update the JSON string below
json = "{}"
# create an instance of AttackRunbook from a JSON string
attack_runbook_instance = AttackRunbook.from_json(json)
# print the JSON string representation of the object
print AttackRunbook.to_json()

# convert the object into a dict
attack_runbook_dict = attack_runbook_instance.to_dict()
# create an instance of AttackRunbook from a dict
attack_runbook_form_dict = attack_runbook.from_dict(attack_runbook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


