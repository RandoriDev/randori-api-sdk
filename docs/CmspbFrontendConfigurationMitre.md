# CmspbFrontendConfigurationMitre


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mitigations** | **List[str]** |  | [optional] 
**tactics** | **List[str]** |  | [optional] 
**techniques** | **List[str]** |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_configuration_mitre import CmspbFrontendConfigurationMitre

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendConfigurationMitre from a JSON string
cmspb_frontend_configuration_mitre_instance = CmspbFrontendConfigurationMitre.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendConfigurationMitre.to_json()

# convert the object into a dict
cmspb_frontend_configuration_mitre_dict = cmspb_frontend_configuration_mitre_instance.to_dict()
# create an instance of CmspbFrontendConfigurationMitre from a dict
cmspb_frontend_configuration_mitre_form_dict = cmspb_frontend_configuration_mitre.from_dict(cmspb_frontend_configuration_mitre_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


