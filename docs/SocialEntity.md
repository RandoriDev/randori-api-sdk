# SocialEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**affiliation_state** | **str** |  | [optional] 
**authority** | **bool** |  | [optional] 
**authority_distance** | **int** |  | [optional] 
**authority_override** | **bool** |  | [optional] 
**authorization_state** | **str** |  | [optional] 
**characteristic_tags** | **List[str]** |  | [optional] 
**city** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**confidence** | **int** |  | [optional] 
**country** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**details** | **object** |  | [optional] 
**domain** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**email_type** | **str** |  | [optional] 
**first_seen** | **datetime** |  | [optional] 
**id** | **str** |  | 
**impact_score** | **str** |  | [optional] 
**last_seen** | **datetime** |  | [optional] 
**lens_id** | **str** |  | [optional] 
**lens_view** | **str** |  | [optional] 
**only_in_review_targets** | **bool** |  | [optional] 
**org_id** | **str** |  | 
**person_first_name** | **str** |  | [optional] 
**person_last_name** | **str** |  | [optional] 
**person_middle_name** | **str** |  | [optional] 
**person_name** | **str** |  | [optional] 
**perspective** | **str** |  | [optional] 
**perspective_name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**priority_impact_factor** | **float** |  | [optional] 
**priority_score** | **float** |  | [optional] 
**priority_status_factor** | **float** |  | [optional] 
**priority_tags_factor** | **float** |  | [optional] 
**role** | **str** |  | [optional] 
**seniority** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**sub_role** | **str** |  | [optional] 
**target_temptation** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**tld** | **str** |  | [optional] 
**user_tags** | **List[str]** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.social_entity import SocialEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SocialEntity from a JSON string
social_entity_instance = SocialEntity.from_json(json)
# print the JSON string representation of the object
print SocialEntity.to_json()

# convert the object into a dict
social_entity_dict = social_entity_instance.to_dict()
# create an instance of SocialEntity from a dict
social_entity_form_dict = social_entity.from_dict(social_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


