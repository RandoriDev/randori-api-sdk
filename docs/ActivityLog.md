# ActivityLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration__description** | **str** |  | [optional] 
**configuration__id** | **str** |  | [optional] 
**configuration__name** | **str** |  | [optional] 
**configuration__version_id** | **str** |  | [optional] 
**count__artifacts** | **int** |  | [optional] 
**count__entities_updated** | **int** |  | [optional] 
**count__relationships_deleted** | **int** |  | [optional] 
**id** | **str** |  | 
**instance__most_recent_instance_id** | **str** |  | 
**instance__perspective** | **str** |  | [optional] 
**instance__state** | **str** |  | [optional] 
**instance__time_duration** | **int** |  | [optional] 
**instance__time_end** | **datetime** |  | [optional] 
**instance__time_start** | **datetime** |  | [optional] 
**matching_entity__detection** | **str** |  | [optional] 
**matching_entity__email** | **str** |  | [optional] 
**matching_entity__hostname** | **str** |  | [optional] 
**matching_entity__id** | **str** |  | 
**matching_entity__ip** | **str** |  | [optional] 
**matching_entity__name** | **str** |  | [optional] 
**matching_entity__network** | **str** |  | [optional] 
**matching_entity__target** | **str** |  | [optional] 
**matching_entity__term** | **str** |  | [optional] 
**matching_entity__type** | **str** |  | [optional] 
**mitre__mitigations** | **List[str]** |  | [optional] 
**mitre__tactics** | **List[str]** |  | [optional] 
**mitre__techniques** | **List[str]** |  | [optional] 
**objective__attacker_perspective** | **str** |  | [optional] 
**objective__description** | **str** |  | [optional] 
**objective__implication** | **str** |  | [optional] 
**objective__status** | **str** |  | [optional] 
**org_id** | **str** |  | 
**traffic_destination** | **str** |  | [optional] 
**traffic_destination_detail** | **object** |  | [optional] 
**traffic_source__ip_name** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.activity_log import ActivityLog

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityLog from a JSON string
activity_log_instance = ActivityLog.from_json(json)
# print the JSON string representation of the object
print ActivityLog.to_json()

# convert the object into a dict
activity_log_dict = activity_log_instance.to_dict()
# create an instance of ActivityLog from a dict
activity_log_form_dict = activity_log.from_dict(activity_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


