# Service


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicability** | **int** |  | [optional] 
**attack_note** | **str** |  | [optional] 
**confidence** | **int** |  | [optional] 
**cpe** | **object** |  | [optional] 
**criticality** | **int** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**description_source** | **str** |  | [optional] 
**enumerability** | **int** |  | [optional] 
**exploitability** | **int** |  | [optional] 
**first_seen** | **datetime** |  | [optional] 
**id** | **str** |  | 
**instance_count** | **float** |  | [optional] 
**ip_count** | **float** |  | [optional] 
**last_seen** | **datetime** |  | [optional] 
**lens_id** | **str** |  | [optional] 
**lens_view** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **str** |  | 
**perspective** | **str** |  | [optional] 
**perspective_name** | **str** |  | [optional] 
**post_exploit** | **int** |  | [optional] 
**private_weakness** | **int** |  | [optional] 
**public_weakness** | **int** |  | [optional] 
**randori_notes** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**research** | **int** |  | [optional] 
**service_id** | **str** |  | [optional] 
**target_temptation** | **int** |  | [optional] 
**tech_category** | **List[str]** |  | [optional] 
**temptation_last_modified** | **datetime** |  | [optional] 
**vendor** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from randori_api_sdk.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print Service.to_json()

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_form_dict = service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


