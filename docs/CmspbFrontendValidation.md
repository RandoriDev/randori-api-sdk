# CmspbFrontendValidation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_text** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_validation import CmspbFrontendValidation

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendValidation from a JSON string
cmspb_frontend_validation_instance = CmspbFrontendValidation.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendValidation.to_json()

# convert the object into a dict
cmspb_frontend_validation_dict = cmspb_frontend_validation_instance.to_dict()
# create an instance of CmspbFrontendValidation from a dict
cmspb_frontend_validation_form_dict = cmspb_frontend_validation.from_dict(cmspb_frontend_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


