# OtpTokenInputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp** | **str** |  | 

## Example

```python
from randori_api_sdk.models.otp_token_input_schema import OtpTokenInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OtpTokenInputSchema from a JSON string
otp_token_input_schema_instance = OtpTokenInputSchema.from_json(json)
# print the JSON string representation of the object
print OtpTokenInputSchema.to_json()

# convert the object into a dict
otp_token_input_schema_dict = otp_token_input_schema_instance.to_dict()
# create an instance of OtpTokenInputSchema from a dict
otp_token_input_schema_form_dict = otp_token_input_schema.from_dict(otp_token_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


