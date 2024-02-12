# CmspbRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicable_entities** | [**CmspbApplicableEntities**](CmspbApplicableEntities.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_relationships import CmspbRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbRelationships from a JSON string
cmspb_relationships_instance = CmspbRelationships.from_json(json)
# print the JSON string representation of the object
print CmspbRelationships.to_json()

# convert the object into a dict
cmspb_relationships_dict = cmspb_relationships_instance.to_dict()
# create an instance of CmspbRelationships from a dict
cmspb_relationships_form_dict = cmspb_relationships.from_dict(cmspb_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


