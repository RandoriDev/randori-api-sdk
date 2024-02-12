# ReconWorkerNodeIps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lookbackdays** | **int** |  | [optional] 
**results** | **Dict[str, bool]** |  | [optional] 

## Example

```python
from randori_api_sdk.models.recon_worker_node_ips import ReconWorkerNodeIps

# TODO update the JSON string below
json = "{}"
# create an instance of ReconWorkerNodeIps from a JSON string
recon_worker_node_ips_instance = ReconWorkerNodeIps.from_json(json)
# print the JSON string representation of the object
print ReconWorkerNodeIps.to_json()

# convert the object into a dict
recon_worker_node_ips_dict = recon_worker_node_ips_instance.to_dict()
# create an instance of ReconWorkerNodeIps from a dict
recon_worker_node_ips_form_dict = recon_worker_node_ips.from_dict(recon_worker_node_ips_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


