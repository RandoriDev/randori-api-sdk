# TimestamppbTimestamp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nanos** | **int** | Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. | [optional] 
**seconds** | **int** | Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. | [optional] 

## Example

```python
from randori_api_sdk.models.timestamppb_timestamp import TimestamppbTimestamp

# TODO update the JSON string below
json = "{}"
# create an instance of TimestamppbTimestamp from a JSON string
timestamppb_timestamp_instance = TimestamppbTimestamp.from_json(json)
# print the JSON string representation of the object
print TimestamppbTimestamp.to_json()

# convert the object into a dict
timestamppb_timestamp_dict = timestamppb_timestamp_instance.to_dict()
# create an instance of TimestamppbTimestamp from a dict
timestamppb_timestamp_form_dict = timestamppb_timestamp.from_dict(timestamppb_timestamp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


