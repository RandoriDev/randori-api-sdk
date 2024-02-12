# Target


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
**characteristic_tags** | **List[str]** |  | [optional] 
**confidence** | **int** |  | [optional] 
**cpe** | **object** |  | [optional] 
**criticality** | **int** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**description_source** | **str** |  | [optional] 
**detection_criteria** | **object** |  | [optional] 
**enumerability** | **int** |  | [optional] 
**first_seen** | **datetime** |  | [optional] 
**id** | **str** |  | 
**impact_score** | **str** |  | [optional] 
**last_seen** | **datetime** |  | [optional] 
**lens_id** | **str** |  | [optional] 
**lens_view** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **str** |  | 
**perspective** | **str** |  | [optional] 
**perspective_name** | **str** |  | [optional] 
**post_exploit** | **int** |  | [optional] 
**priority_impact_factor** | **float** |  | [optional] 
**priority_score** | **float** |  | [optional] 
**priority_status_factor** | **float** |  | [optional] 
**priority_tags_factor** | **float** |  | [optional] 
**private_weakness** | **int** |  | [optional] 
**public_weakness** | **int** |  | [optional] 
**randori_notes** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**research** | **int** |  | [optional] 
**service_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**target_temptation** | **int** |  | [optional] 
**tech_category** | **List[str]** |  | [optional] 
**temptation_last_modified** | **datetime** |  | [optional] 
**user_tags** | **List[str]** |  | [optional] 
**validated_vulnerabilities_target** | **List[str]** |  | [optional] 
**validated_vulnerabilities_target_count** | **int** |  | [optional] 
**vendor** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.target import Target

# TODO update the JSON string below
json = "{}"
# create an instance of Target from a JSON string
target_instance = Target.from_json(json)
# print the JSON string representation of the object
print Target.to_json()

# convert the object into a dict
target_dict = target_instance.to_dict()
# create an instance of Target from a dict
target_form_dict = target.from_dict(target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


