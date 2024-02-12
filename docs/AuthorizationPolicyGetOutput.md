# AuthorizationPolicyGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of records in this result | [optional] 
**data** | [**List[AuthorizationPolicy]**](AuthorizationPolicy.md) | list of objects | [optional] 
**offset** | **int** | starting offset after filtering | [optional] 
**total** | **int** | number of records total after filtering | [optional] 

## Example

```python
from randori_api_sdk.models.authorization_policy_get_output import AuthorizationPolicyGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationPolicyGetOutput from a JSON string
authorization_policy_get_output_instance = AuthorizationPolicyGetOutput.from_json(json)
# print the JSON string representation of the object
print AuthorizationPolicyGetOutput.to_json()

# convert the object into a dict
authorization_policy_get_output_dict = authorization_policy_get_output_instance.to_dict()
# create an instance of AuthorizationPolicyGetOutput from a dict
authorization_policy_get_output_form_dict = authorization_policy_get_output.from_dict(authorization_policy_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


