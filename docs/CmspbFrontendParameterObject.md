# CmspbFrontendParameterObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**CmspbFrontendParameter**](CmspbFrontendParameter.md) |  | [optional] 
**type** | [**CmspbFrontendType**](CmspbFrontendType.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_parameter_object import CmspbFrontendParameterObject

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendParameterObject from a JSON string
cmspb_frontend_parameter_object_instance = CmspbFrontendParameterObject.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendParameterObject.to_json()

# convert the object into a dict
cmspb_frontend_parameter_object_dict = cmspb_frontend_parameter_object_instance.to_dict()
# create an instance of CmspbFrontendParameterObject from a dict
cmspb_frontend_parameter_object_form_dict = cmspb_frontend_parameter_object.from_dict(cmspb_frontend_parameter_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


