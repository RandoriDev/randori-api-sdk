# CmspbFrontendConfigurationObjective


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attackers_perspective** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**implication** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_configuration_objective import CmspbFrontendConfigurationObjective

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendConfigurationObjective from a JSON string
cmspb_frontend_configuration_objective_instance = CmspbFrontendConfigurationObjective.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendConfigurationObjective.to_json()

# convert the object into a dict
cmspb_frontend_configuration_objective_dict = cmspb_frontend_configuration_objective_instance.to_dict()
# create an instance of CmspbFrontendConfigurationObjective from a dict
cmspb_frontend_configuration_objective_form_dict = cmspb_frontend_configuration_objective.from_dict(cmspb_frontend_configuration_objective_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


