# AllDetectionsForTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliation_state** | **str** |  | [optional] 
**applicability** | **int** |  | [optional] 
**attack_note** | **str** |  | [optional] 
**authority** | **bool** |  | [optional] 
**authority_distance** | **int** |  | [optional] 
**authority_override** | **bool** |  | [optional] 
**authorization_state** | **str** |  | [optional] 
**authorizing_policies** | **List[str]** |  | [optional] 
**banners_uuid** | **str** |  | [optional] 
**cert_uuid** | **str** |  | [optional] 
**characteristic_tags** | **List[str]** |  | [optional] 
**characteristics_count** | **int** |  | [optional] 
**confidence** | **int** |  | [optional] 
**cpe** | **object** |  | [optional] 
**criticality** | **int** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**description_source** | **str** |  | [optional] 
**detection_authorization_state** | **str** |  | [optional] 
**detection_criteria** | **object** |  | [optional] 
**detection_relevance** | **int** |  | [optional] 
**detection_uuid** | **str** |  | [optional] 
**enumerability** | **int** |  | [optional] 
**exploitability** | **int** |  | [optional] 
**first_seen** | **datetime** |  | [optional] 
**headers_uuid** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**hostname_id** | **str** |  | [optional] 
**id** | **str** |  | 
**impact_score** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**ip_id** | **str** |  | [optional] 
**ip_str** | **str** |  | [optional] 
**last_seen** | **datetime** |  | [optional] 
**lens_id** | **str** |  | [optional] 
**lens_view** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **str** |  | 
**path** | **str** |  | [optional] 
**perspective** | **str** |  | [optional] 
**perspective_name** | **str** |  | [optional] 
**poc_email** | **str** |  | [optional] 
**poc_id** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**post_exploit** | **int** |  | [optional] 
**priority_impact_factor** | **float** |  | [optional] 
**priority_score** | **float** |  | [optional] 
**priority_status_factor** | **float** |  | [optional] 
**priority_tags_factor** | **float** |  | [optional] 
**private_weakness** | **int** |  | [optional] 
**protocol** | **str** |  | [optional] 
**public_weakness** | **int** |  | [optional] 
**randori_notes** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**research** | **int** |  | [optional] 
**screenshot_uuid** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**target_confidence** | **int** |  | [optional] 
**target_first_seen** | **datetime** |  | [optional] 
**target_id** | **str** |  | [optional] 
**target_last_seen** | **datetime** |  | [optional] 
**target_num_authorized_detections** | **int** |  | [optional] 
**target_num_detections** | **int** |  | [optional] 
**target_temptation** | **int** |  | [optional] 
**tech_category** | **List[str]** |  | [optional] 
**temptation_last_modified** | **datetime** |  | [optional] 
**thumbnail_uuid** | **str** |  | [optional] 
**user_tags** | **List[str]** |  | [optional] 
**validated_vulnerabilities_detection** | **List[str]** |  | [optional] 
**validated_vulnerabilities_detection_count** | **int** |  | [optional] 
**validated_vulnerabilities_target** | **List[str]** |  | [optional] 
**validated_vulnerabilities_target_count** | **int** |  | [optional] 
**vendor** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.all_detections_for_target import AllDetectionsForTarget

# TODO update the JSON string below
json = "{}"
# create an instance of AllDetectionsForTarget from a JSON string
all_detections_for_target_instance = AllDetectionsForTarget.from_json(json)
# print the JSON string representation of the object
print AllDetectionsForTarget.to_json()

# convert the object into a dict
all_detections_for_target_dict = all_detections_for_target_instance.to_dict()
# create an instance of AllDetectionsForTarget from a dict
all_detections_for_target_form_dict = all_detections_for_target.from_dict(all_detections_for_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


