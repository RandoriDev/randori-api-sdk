# SocialEntityGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[SocialEntity]**](SocialEntity.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.social_entity_get_output import SocialEntityGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SocialEntityGetOutput from a JSON string
social_entity_get_output_instance = SocialEntityGetOutput.from_json(json)
# print the JSON string representation of the object
print SocialEntityGetOutput.to_json()

# convert the object into a dict
social_entity_get_output_dict = social_entity_get_output_instance.to_dict()
# create an instance of SocialEntityGetOutput from a dict
social_entity_get_output_form_dict = social_entity_get_output.from_dict(social_entity_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


