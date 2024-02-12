# ActionMetadataSingleOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ActionMetadata**](ActionMetadata.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.action_metadata_single_output import ActionMetadataSingleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ActionMetadataSingleOutput from a JSON string
action_metadata_single_output_instance = ActionMetadataSingleOutput.from_json(json)
# print the JSON string representation of the object
print ActionMetadataSingleOutput.to_json()

# convert the object into a dict
action_metadata_single_output_dict = action_metadata_single_output_instance.to_dict()
# create an instance of ActionMetadataSingleOutput from a dict
action_metadata_single_output_form_dict = action_metadata_single_output.from_dict(action_metadata_single_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


