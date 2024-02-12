# CmspbFrontendRunNowJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**status** | [**CmspbFrontendRunNowJobStatus**](CmspbFrontendRunNowJobStatus.md) |  | [optional] 

## Example

```python
from randori_api_sdk.models.cmspb_frontend_run_now_job_response import CmspbFrontendRunNowJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CmspbFrontendRunNowJobResponse from a JSON string
cmspb_frontend_run_now_job_response_instance = CmspbFrontendRunNowJobResponse.from_json(json)
# print the JSON string representation of the object
print CmspbFrontendRunNowJobResponse.to_json()

# convert the object into a dict
cmspb_frontend_run_now_job_response_dict = cmspb_frontend_run_now_job_response_instance.to_dict()
# create an instance of CmspbFrontendRunNowJobResponse from a dict
cmspb_frontend_run_now_job_response_form_dict = cmspb_frontend_run_now_job_response.from_dict(cmspb_frontend_run_now_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


