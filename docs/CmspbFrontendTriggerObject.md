# CmspbFrontendTriggerObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**CmspbFrontendTrigger**](CmspbFrontendTrigger.md) |  | [optional] 
**type** | [**CmspbFrontendType**](CmspbFrontendType.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_trigger_object import CmspbFrontendTriggerObject

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendTriggerObject from a JSON string
cmspb_frontend_trigger_object_instance = CmspbFrontendTriggerObject.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendTriggerObject.to_json()

# convert the object into a dict
cmspb_frontend_trigger_object_dict = cmspb_frontend_trigger_object_instance.to_dict()
# create an instance of CmspbFrontendTriggerObject from a dict
cmspb_frontend_trigger_object_form_dict = cmspb_frontend_trigger_object.from_dict(cmspb_frontend_trigger_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


