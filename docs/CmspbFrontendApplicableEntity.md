# CmspbFrontendApplicableEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**CmspbFrontendApplicableEntityAttributes**](CmspbFrontendApplicableEntityAttributes.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | [**CmspbFrontendType**](CmspbFrontendType.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_applicable_entity import CmspbFrontendApplicableEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendApplicableEntity from a JSON string
cmspb_frontend_applicable_entity_instance = CmspbFrontendApplicableEntity.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendApplicableEntity.to_json()

# convert the object into a dict
cmspb_frontend_applicable_entity_dict = cmspb_frontend_applicable_entity_instance.to_dict()
# create an instance of CmspbFrontendApplicableEntity from a dict
cmspb_frontend_applicable_entity_form_dict = cmspb_frontend_applicable_entity.from_dict(cmspb_frontend_applicable_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


