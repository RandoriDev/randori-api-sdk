# CmspbFrontendListApplicableConfigurationsResponseAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**last_planned_at** | [**TimestamppbTimestamp**](TimestamppbTimestamp.md) |  | [optional] 
**name** | **str** |  | [optional] 
**needs_authorization** | **bool** |  | [optional] 
**period** | **int** |  | [optional] 
**required_authorization** | **int** |  | [optional] 
**stability** | **int** |  | [optional] 
**stealth** | **int** |  | [optional] 
**trigger_criteria** | [**List[CmspbFrontendListApplicableConfigurationsResponseTriggerCriteria]**](CmspbFrontendListApplicableConfigurationsResponseTriggerCriteria.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_list_applicable_configurations_response_attributes import CmspbFrontendListApplicableConfigurationsResponseAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendListApplicableConfigurationsResponseAttributes from a JSON string
cmspb_frontend_list_applicable_configurations_response_attributes_instance = CmspbFrontendListApplicableConfigurationsResponseAttributes.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendListApplicableConfigurationsResponseAttributes.to_json()

# convert the object into a dict
cmspb_frontend_list_applicable_configurations_response_attributes_dict = cmspb_frontend_list_applicable_configurations_response_attributes_instance.to_dict()
# create an instance of CmspbFrontendListApplicableConfigurationsResponseAttributes from a dict
cmspb_frontend_list_applicable_configurations_response_attributes_form_dict = cmspb_frontend_list_applicable_configurations_response_attributes.from_dict(cmspb_frontend_list_applicable_configurations_response_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


