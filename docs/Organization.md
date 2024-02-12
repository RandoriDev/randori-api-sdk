# Organization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**allowed_email_domains** | **List[str]** |  | [optional] 
**contact** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**license_level** | **object** | License tier for the organization | [optional] 
**login_methods** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**paying** | **bool** |  | [optional] 
**platform_subscription_id** | **str** |  | [optional] 
**shortname** | **str** |  | [optional] 
**sso_path** | **str** | If SSO is enabled, is a unique login link | [optional] 
**stasis** | **bool** |  | [optional] 
**stasis_last_update_by** | **str** |  | [optional] 
**stasis_last_update_on** | **datetime** |  | [optional] 

## Example

```python
from randori_api_sdk.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print Organization.to_json()

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_form_dict = organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


