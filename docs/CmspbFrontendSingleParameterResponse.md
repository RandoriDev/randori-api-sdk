# CmspbFrontendSingleParameterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CmspbFrontendParameterObject**](CmspbFrontendParameterObject.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_single_parameter_response import CmspbFrontendSingleParameterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendSingleParameterResponse from a JSON string
cmspb_frontend_single_parameter_response_instance = CmspbFrontendSingleParameterResponse.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendSingleParameterResponse.to_json()

# convert the object into a dict
cmspb_frontend_single_parameter_response_dict = cmspb_frontend_single_parameter_response_instance.to_dict()
# create an instance of CmspbFrontendSingleParameterResponse from a dict
cmspb_frontend_single_parameter_response_form_dict = cmspb_frontend_single_parameter_response.from_dict(cmspb_frontend_single_parameter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


