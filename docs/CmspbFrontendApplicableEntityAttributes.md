# CmspbFrontendApplicableEntityAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_applicable_entity_attributes import CmspbFrontendApplicableEntityAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendApplicableEntityAttributes from a JSON string
cmspb_frontend_applicable_entity_attributes_instance = CmspbFrontendApplicableEntityAttributes.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendApplicableEntityAttributes.to_json()

# convert the object into a dict
cmspb_frontend_applicable_entity_attributes_dict = cmspb_frontend_applicable_entity_attributes_instance.to_dict()
# create an instance of CmspbFrontendApplicableEntityAttributes from a dict
cmspb_frontend_applicable_entity_attributes_form_dict = cmspb_frontend_applicable_entity_attributes.from_dict(cmspb_frontend_applicable_entity_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


