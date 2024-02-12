# CmspbFrontendConfigurationAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type_description** | **str** |  | [optional] 
**activity_type_name** | **str** |  | [optional] 
**authority_display** | **bool** |  | [optional] 
**authority_distance_max** | **int** |  | [optional] 
**authority_distance_min** | **int** |  | [optional] 
**configuration_id** | **str** |  | [optional] 
**created** | [**CmspbFrontendConfigurationAccessEntry**](CmspbFrontendConfigurationAccessEntry.md) |  | [optional] 
**cves** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**entities_count** | **int** |  | [optional] 
**last_planned_at** | [**TimestamppbTimestamp**](TimestamppbTimestamp.md) |  | [optional] 
**matching_entity_types** | **List[str]** |  | [optional] 
**mitre** | [**CmspbFrontendConfigurationMitre**](CmspbFrontendConfigurationMitre.md) |  | [optional] 
**name** | **str** |  | [optional] 
**objective** | [**CmspbFrontendConfigurationObjective**](CmspbFrontendConfigurationObjective.md) |  | [optional] 
**parameters** | [**List[CmspbFrontendParameterObject]**](CmspbFrontendParameterObject.md) |  | [optional] 
**period** | **int** |  | [optional] 
**required_authorization** | **int** |  | [optional] 
**stability** | **int** |  | [optional] 
**stealth** | **int** |  | [optional] 
**targets_count** | **int** |  | [optional] 
**trigger_criteria** | [**List[CmspbFrontendTriggerObject]**](CmspbFrontendTriggerObject.md) |  | [optional] 
**updated** | [**CmspbFrontendConfigurationAccessEntry**](CmspbFrontendConfigurationAccessEntry.md) |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_configuration_attributes import CmspbFrontendConfigurationAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendConfigurationAttributes from a JSON string
cmspb_frontend_configuration_attributes_instance = CmspbFrontendConfigurationAttributes.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendConfigurationAttributes.to_json()

# convert the object into a dict
cmspb_frontend_configuration_attributes_dict = cmspb_frontend_configuration_attributes_instance.to_dict()
# create an instance of CmspbFrontendConfigurationAttributes from a dict
cmspb_frontend_configuration_attributes_form_dict = cmspb_frontend_configuration_attributes.from_dict(cmspb_frontend_configuration_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


