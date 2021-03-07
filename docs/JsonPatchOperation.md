# JsonPatchOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | operation, 'add' or 'remove' | [optional] 
**path** | **str** | target location | [optional] 
**value** | **str** | new value for add/replace | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


## Examples

### Apply A Tag To An Entity
```json
{
    "operations": [
        {
            "op": "add",
            "path": "/tags/YOUR_TAG_HERE",
            "value": {}
        }
    ],
    "q": {
        "condition": "OR",
        "rules": [
            {
                "id": "table.id",
                "field": "table.id",
                "type": "object",
                "input": "text",
                "operator": "equal",
                "value": "REPLACE_ME_WITH_ENTITY_ID"
            }
        ]
    }
}
```

### Remove A Tag From An Entity
```json
{
    "operations": [
        {
            "op": "remove",
            "path": "/tags/Atlanta Office",
            "value": {}
        }
    ],
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

### Apply Multiple Tags To An Entity
```json
{
    "operations": [
        {
            "op": "add",
            "path": "/tags/Atlanta Office",
            "value": {}
        },
        {
            "op": "add",
            "path": "/tags/Engineering",
            "value": {}
        }
    ],
    "q": {
        "condition": "OR",
        "rules": [
            {
                "id": "table.id",
                "field": "table.id",
                "type": "object",
                "input": "text",
                "operator": "equal",
                "value": "REPLACE_ME_WITH_ENTITY_ID"
            }
        ]
    }
}
```

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

### Authorize A Target For Attack
```json
{
    "data": {
        "authorization_state": "Authorized"
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

### Remove Authorization For Attack
```json
{
    "data": {
        "authorization_state": "None"
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
