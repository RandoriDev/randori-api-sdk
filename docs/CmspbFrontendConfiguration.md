# CmspbFrontendConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**CmspbFrontendConfigurationAttributes**](CmspbFrontendConfigurationAttributes.md) |  | [optional] 
**id** | **str** |  | [optional] 
**relationships** | [**CmspbRelationships**](CmspbRelationships.md) |  | [optional] 
**type** | [**CmspbFrontendType**](CmspbFrontendType.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_configuration import CmspbFrontendConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendConfiguration from a JSON string
cmspb_frontend_configuration_instance = CmspbFrontendConfiguration.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendConfiguration.to_json()

# convert the object into a dict
cmspb_frontend_configuration_dict = cmspb_frontend_configuration_instance.to_dict()
# create an instance of CmspbFrontendConfiguration from a dict
cmspb_frontend_configuration_form_dict = cmspb_frontend_configuration.from_dict(cmspb_frontend_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


