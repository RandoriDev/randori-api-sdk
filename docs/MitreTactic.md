# MitreTactic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | 
**created_by_ref** | **str** |  | 
**description** | **str** |  | 
**external_references** | **List[object]** |  | 
**id** | **str** |  | 
**modified** | **datetime** |  | 
**name** | **str** |  | 
**object_marking_refs** | **List[str]** |  | 
**revoked** | **bool** |  | 
**spec_version** | **str** |  | 
**type** | **str** |  | 
**x_mitre_attack_spec_version** | **str** |  | 
**x_mitre_domains** | **List[str]** |  | 
**x_mitre_modified_by_ref** | **str** |  | 
**x_mitre_shortname** | **str** |  | 
**x_mitre_version** | **float** |  | 

## Example

```python
from randori_api_sdk.models.mitre_tactic import MitreTactic

# TODO update the JSON string below
json = "{}"
# create an instance of MitreTactic from a JSON string
mitre_tactic_instance = MitreTactic.from_json(json)
# print the JSON string representation of the object
print MitreTactic.to_json()

# convert the object into a dict
mitre_tactic_dict = mitre_tactic_instance.to_dict()
# create an instance of MitreTactic from a dict
mitre_tactic_form_dict = mitre_tactic.from_dict(mitre_tactic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


