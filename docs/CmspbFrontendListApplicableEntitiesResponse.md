# CmspbFrontendListApplicableEntitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CmspbFrontendApplicableEntity]**](CmspbFrontendApplicableEntity.md) |  | [optional] 
**links** | [**CmspbFrontendLinks**](CmspbFrontendLinks.md) |  | [optional] 
**meta** | [**CmspbFrontendMeta**](CmspbFrontendMeta.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_list_applicable_entities_response import CmspbFrontendListApplicableEntitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendListApplicableEntitiesResponse from a JSON string
cmspb_frontend_list_applicable_entities_response_instance = CmspbFrontendListApplicableEntitiesResponse.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendListApplicableEntitiesResponse.to_json()

# convert the object into a dict
cmspb_frontend_list_applicable_entities_response_dict = cmspb_frontend_list_applicable_entities_response_instance.to_dict()
# create an instance of CmspbFrontendListApplicableEntitiesResponse from a dict
cmspb_frontend_list_applicable_entities_response_form_dict = cmspb_frontend_list_applicable_entities_response.from_dict(cmspb_frontend_list_applicable_entities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


