# AttackStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **bool** |  | 
**id** | **str** |  | [optional] 
**index** | **int** |  | 
**latest** | **bool** |  | 
**name** | **str** |  | 
**org_id** | **str** |  | 
**row_time** | **datetime** |  | 
**time** | **datetime** |  | 
**type** | **str** |  | 
**value** | **int** |  | 

## Example

```python
from randori_api_sdk.models.attack_statistics import AttackStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of AttackStatistics from a JSON string
attack_statistics_instance = AttackStatistics.from_json(json)
# print the JSON string representation of the object
print AttackStatistics.to_json()

# convert the object into a dict
attack_statistics_dict = attack_statistics_instance.to_dict()
# create an instance of AttackStatistics from a dict
attack_statistics_form_dict = attack_statistics.from_dict(attack_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


