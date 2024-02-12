# MitreMitigation


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
**type** | **str** |  | 
**x_mitre_domains** | **List[str]** |  | 
**x_mitre_modified_by_ref** | **str** |  | 
**x_mitre_version** | **float** |  | 

## Example

```python
from randori_api_sdk.models.mitre_mitigation import MitreMitigation

# TODO update the JSON string below
json = "{}"
# create an instance of MitreMitigation from a JSON string
mitre_mitigation_instance = MitreMitigation.from_json(json)
# print the JSON string representation of the object
print MitreMitigation.to_json()

# convert the object into a dict
mitre_mitigation_dict = mitre_mitigation_instance.to_dict()
# create an instance of MitreMitigation from a dict
mitre_mitigation_form_dict = mitre_mitigation.from_dict(mitre_mitigation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


