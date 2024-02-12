# QuerybuilderRuleGroupSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** |  | 
**label** | **str** |  | [optional] 
**rules** | **List[object]** |  | 
**ui_id** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.querybuilder_rule_group_schema import QuerybuilderRuleGroupSchema

# TODO update the JSON string below
json = "{}"
# create an instance of QuerybuilderRuleGroupSchema from a JSON string
querybuilder_rule_group_schema_instance = QuerybuilderRuleGroupSchema.from_json(json)
# print the JSON string representation of the object
print QuerybuilderRuleGroupSchema.to_json()

# convert the object into a dict
querybuilder_rule_group_schema_dict = querybuilder_rule_group_schema_instance.to_dict()
# create an instance of QuerybuilderRuleGroupSchema from a dict
querybuilder_rule_group_schema_form_dict = querybuilder_rule_group_schema.from_dict(querybuilder_rule_group_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


