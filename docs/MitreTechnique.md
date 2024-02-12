# MitreTechnique


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | 
**created_by_ref** | **str** |  | 
**description** | **str** |  | 
**external_references** | **List[object]** |  | 
**id** | **str** |  | 
**kill_chain_phases** | **List[object]** |  | 
**modified** | **datetime** |  | 
**name** | **str** |  | 
**object_marking_refs** | **List[str]** |  | 
**revoked** | **bool** |  | 
**type** | **str** |  | 
**x_mitre_attack_spec_version** | **str** |  | [optional] 
**x_mitre_data_sources** | **List[str]** |  | [optional] 
**x_mitre_deprecated** | **bool** |  | [optional] 
**x_mitre_detection** | **str** |  | 
**x_mitre_domains** | **List[str]** |  | 
**x_mitre_is_subtechnique** | **bool** |  | 
**x_mitre_modified_by_ref** | **str** |  | 
**x_mitre_permissions_required** | **List[str]** |  | [optional] 
**x_mitre_platforms** | **List[str]** |  | 
**x_mitre_version** | **float** |  | 

## Example

```python
from randori_api_sdk.models.mitre_technique import MitreTechnique

# TODO update the JSON string below
json = "{}"
# create an instance of MitreTechnique from a JSON string
mitre_technique_instance = MitreTechnique.from_json(json)
# print the JSON string representation of the object
print MitreTechnique.to_json()

# convert the object into a dict
mitre_technique_dict = mitre_technique_instance.to_dict()
# create an instance of MitreTechnique from a dict
mitre_technique_form_dict = mitre_technique.from_dict(mitre_technique_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


