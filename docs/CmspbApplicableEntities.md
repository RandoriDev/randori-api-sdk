# CmspbApplicableEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CmspbFrontendApplicableEntity]**](CmspbFrontendApplicableEntity.md) |  | [optional] 
**links** | [**CmspbFrontendLinks**](CmspbFrontendLinks.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_applicable_entities import CmspbApplicableEntities

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbApplicableEntities from a JSON string
cmspb_applicable_entities_instance = CmspbApplicableEntities.from_json(json)
# print the JSON string representation of the object
print CmspbApplicableEntities.to_json()

# convert the object into a dict
cmspb_applicable_entities_dict = cmspb_applicable_entities_instance.to_dict()
# create an instance of CmspbApplicableEntities from a dict
cmspb_applicable_entities_form_dict = cmspb_applicable_entities.from_dict(cmspb_applicable_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


