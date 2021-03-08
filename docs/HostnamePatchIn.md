# HostnamePatchIn

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliation_state** | **str** |  | [optional] 
**impact_score** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

## Examples

### Set Status Of An Entity
```json
{
    "data": {
        "status": "Needs Investigation"
    },
    "q": {
        "condition": "OR",
        "rules": [
            {
                "id": "table.id",
                "field": "table.id",
                "type": "object",
                "input": "text",
                "operator": "equal",
                "value": "REPLACE_ME_WITH_AN_ENTITY_ID"
            }
        ]
    }
}
```

### Set Impact Of An Entity
```json
{
    "data": {
        "impact_score": "Medium"
    },
    "q": {
        "condition": "OR",
        "rules": [
            {
                "id": "table.id",
                "field": "table.id",
                "type": "object",
                "input": "text",
                "operator": "equal",
                "value": "REPLACE_ME_WITH_AN_ENTITY_ID"
            }
        ]
    }
}
```

### Set Affiliation Of An Entity
```json
{
    "data": {
        "affiliation_state": "Unaffiliated"
    },
    "q": {
        "condition": "OR",
        "rules": [
            {
                "id": "table.id",
                "field": "table.id",
                "type": "object",
                "input": "text",
                "operator": "equal",
                "value": "REPLACE_ME_WITH_AN_ENTITY_ID"
            }
        ]
    }
}
```
