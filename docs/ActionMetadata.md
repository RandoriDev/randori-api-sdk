# ActionMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** |  | 
**artifacts_status** | **str** |  | [optional] 
**bart_id** | **str** |  | 
**completed** | **datetime** |  | [optional] 
**config_hash** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**description_id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**dst_email** | **List[str]** |  | [optional] 
**dst_host** | **List[str]** |  | [optional] 
**dst_ip** | **List[str]** |  | [optional] 
**dst_mac** | **List[str]** |  | [optional] 
**dst_misc** | **List[str]** |  | [optional] 
**dst_network** | **List[str]** |  | [optional] 
**dst_path** | **List[str]** |  | [optional] 
**dst_port** | **List[int]** |  | [optional] 
**id** | **str** |  | 
**implant_id** | **str** |  | [optional] 
**implant_nick** | **str** |  | [optional] 
**implant_uid** | **str** |  | [optional] 
**mitre_techniques** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **str** |  | 
**perspective_metadata** | **object** |  | [optional] 
**randori_notes** | **str** |  | [optional] 
**result** | **str** |  | 
**result_hash** | **str** |  | [optional] 
**runbook_instance_id** | **str** |  | 
**src_email** | **List[str]** |  | [optional] 
**src_host** | **List[str]** |  | [optional] 
**src_ip** | **List[str]** |  | [optional] 
**src_mac** | **List[str]** |  | [optional] 
**src_misc** | **List[str]** |  | [optional] 
**stability** | **int** |  | [optional] 
**started** | **datetime** |  | [optional] 
**stealth** | **int** |  | [optional] 
**summary_sha** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**trigger** | **object** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from randori_api_sdk.models.action_metadata import ActionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ActionMetadata from a JSON string
action_metadata_instance = ActionMetadata.from_json(json)
# print the JSON string representation of the object
print ActionMetadata.to_json()

# convert the object into a dict
action_metadata_dict = action_metadata_instance.to_dict()
# create an instance of ActionMetadata from a dict
action_metadata_form_dict = action_metadata.from_dict(action_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


