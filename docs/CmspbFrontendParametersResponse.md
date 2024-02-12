# CmspbFrontendParametersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CmspbFrontendParameterObject]**](CmspbFrontendParameterObject.md) |  | [optional] 
**links** | [**CmspbFrontendLinks**](CmspbFrontendLinks.md) |  | [optional] 
**meta** | [**CmspbFrontendMeta**](CmspbFrontendMeta.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_parameters_response import CmspbFrontendParametersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendParametersResponse from a JSON string
cmspb_frontend_parameters_response_instance = CmspbFrontendParametersResponse.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendParametersResponse.to_json()

# convert the object into a dict
cmspb_frontend_parameters_response_dict = cmspb_frontend_parameters_response_instance.to_dict()
# create an instance of CmspbFrontendParametersResponse from a dict
cmspb_frontend_parameters_response_form_dict = cmspb_frontend_parameters_response.from_dict(cmspb_frontend_parameters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


