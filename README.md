# Randori-API
Endpoints accessible using API tokens

- API version: 1.0
- Package version: 1.4.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

For more information, please visit [https://www.randori.com/contact/](https://www.randori.com/contact/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

The python package is hosted in a github repository, you can install directly using:

```sh
pip install git+https://github.com/RandoriDev/randori-api-sdk.git
```
Or you may need to run `pip` with root permission:
```sh
sudo pip install git+https://github.com/RandoriDev/randori-api-sdk.git
```

To upgrade and existing installation:
```sh
pip install --upgrade git+https://github.com/RandoriDev/randori-api-sdk.git
```
or
```sh
sudo pip install --upgrade git+https://github.com/RandoriDev/randori-api-sdk.git
```

To verify proper installation, run python, then import the package:
```python
import randori_api
```

Exit python.


### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
Or to install the package for all users
```sh
sudo python setup.py install
```

To verify proper installation run python, then import the package:
```python
import randori_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:


An example script that will pull all detections for targets with Medium or greater Target Temptation.

```python
from __future__ import print_function

import base64
import json
import randori_api
from randori_api.rest import ApiException
from pprint import pprint

configuration = randori_api.Configuration()

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_API_TOKEN_HERE'

# Defining host is optional and default to https://alpha.randori.io
configuration.host = "https://app.randori.io"

# Create an instance of the API class
api_instance = randori_api.DefaultApi(randori_api.ApiClient(configuration))

# int | offset into avilable records after filtering (optional)
offset = 0

# int | maximum number of records to return (optional). Max value = 1000
limit = 5

# list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
sort = ['-priority_score']

# sample jquery query
# Medium temptation
initial_query = json.loads('''{
  "condition": "AND",
  "rules": [
    {
      "field": "table.target_temptation",
      "operator": "greater_or_equal",
      "value": 15
    }
  ],
  "valid": true
  }''')

iq = json.dumps(initial_query).encode()

# str | base64 encoded jquery querybuilder complex search field (optional)
query = base64.b64encode(iq)

# bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)
reversed_nulls = True

try:

    api_response = api_instance.get_all_detections_for_target(offset=offset, limit=limit, sort=sort, q=query, reversed_nulls=reversed_nulls)

    pprint(api_response)

except ApiException as e:

    print("Exception when calling DefaultApi->get_all_detections_for_target: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://app.randori.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**delete_single_saved_views**](docs/DefaultApi.md#delete_single_saved_views) | **DELETE** /recon/api/v1/saved-views/{id} | 
*DefaultApi* | [**get_all_detections_for_target**](docs/DefaultApi.md#get_all_detections_for_target) | **GET** /recon/api/v1/all-detections-for-target | 
*DefaultApi* | [**get_artifact**](docs/DefaultApi.md#get_artifact) | **GET** /recon/api/v1/artifact | 
*DefaultApi* | [**get_detection**](docs/DefaultApi.md#get_detection) | **GET** /recon/api/v1/detection | 
*DefaultApi* | [**get_hostname**](docs/DefaultApi.md#get_hostname) | **GET** /recon/api/v1/hostname | 
*DefaultApi* | [**get_hostnames_for_ip**](docs/DefaultApi.md#get_hostnames_for_ip) | **GET** /recon/api/v1/hostnames-for-ip | 
*DefaultApi* | [**get_ip**](docs/DefaultApi.md#get_ip) | **GET** /recon/api/v1/ip | 
*DefaultApi* | [**get_ips_for_hostname**](docs/DefaultApi.md#get_ips_for_hostname) | **GET** /recon/api/v1/ips-for-hostname | 
*DefaultApi* | [**get_ips_for_network**](docs/DefaultApi.md#get_ips_for_network) | **GET** /recon/api/v1/ips-for-network | 
*DefaultApi* | [**get_ips_for_service**](docs/DefaultApi.md#get_ips_for_service) | **GET** /recon/api/v1/ips-for-service | 
*DefaultApi* | [**get_network**](docs/DefaultApi.md#get_network) | **GET** /recon/api/v1/network | 
*DefaultApi* | [**get_ports_for_ip**](docs/DefaultApi.md#get_ports_for_ip) | **GET** /recon/api/v1/ports-for-ip | 
*DefaultApi* | [**get_saved_views**](docs/DefaultApi.md#get_saved_views) | **GET** /recon/api/v1/saved-views | 
*DefaultApi* | [**get_service**](docs/DefaultApi.md#get_service) | **GET** /recon/api/v1/service | 
*DefaultApi* | [**get_single_detection_for_target**](docs/DefaultApi.md#get_single_detection_for_target) | **GET** /recon/api/v1/single-detection-for-target | 
*DefaultApi* | [**get_single_hostname**](docs/DefaultApi.md#get_single_hostname) | **GET** /recon/api/v1/hostname/{id} | 
*DefaultApi* | [**get_single_hostnames_for_ip**](docs/DefaultApi.md#get_single_hostnames_for_ip) | **GET** /recon/api/v1/hostnames-for-ip/{id} | 
*DefaultApi* | [**get_single_ip**](docs/DefaultApi.md#get_single_ip) | **GET** /recon/api/v1/ip/{id} | 
*DefaultApi* | [**get_single_ips_for_hostname**](docs/DefaultApi.md#get_single_ips_for_hostname) | **GET** /recon/api/v1/ips-for-hostname/{id} | 
*DefaultApi* | [**get_single_ips_for_network**](docs/DefaultApi.md#get_single_ips_for_network) | **GET** /recon/api/v1/ips-for-network/{id} | 
*DefaultApi* | [**get_single_ips_for_service**](docs/DefaultApi.md#get_single_ips_for_service) | **GET** /recon/api/v1/ips-for-service/{id} | 
*DefaultApi* | [**get_single_network**](docs/DefaultApi.md#get_single_network) | **GET** /recon/api/v1/network/{id} | 
*DefaultApi* | [**get_single_ports_for_ip**](docs/DefaultApi.md#get_single_ports_for_ip) | **GET** /recon/api/v1/ports-for-ip/{id} | 
*DefaultApi* | [**get_single_saved_views**](docs/DefaultApi.md#get_single_saved_views) | **GET** /recon/api/v1/saved-views/{id} | 
*DefaultApi* | [**get_single_service**](docs/DefaultApi.md#get_single_service) | **GET** /recon/api/v1/service/{id} | 
*DefaultApi* | [**get_single_tagcounts**](docs/DefaultApi.md#get_single_tagcounts) | **GET** /recon/api/v1/tagcounts/{id} | 
*DefaultApi* | [**get_single_target**](docs/DefaultApi.md#get_single_target) | **GET** /recon/api/v1/target/{id} | 
*DefaultApi* | [**get_social_entity**](docs/DefaultApi.md#get_social_entity) | **GET** /recon/api/v1/social-entity | 
*DefaultApi* | [**get_statistics**](docs/DefaultApi.md#get_statistics) | **GET** /recon/api/v1/statistics | 
*DefaultApi* | [**get_tagcounts**](docs/DefaultApi.md#get_tagcounts) | **GET** /recon/api/v1/tagcounts | 
*DefaultApi* | [**get_target**](docs/DefaultApi.md#get_target) | **GET** /recon/api/v1/target | 
*DefaultApi* | [**patch_hostname**](docs/DefaultApi.md#patch_hostname) | **PATCH** /recon/api/v1/hostname | 
*DefaultApi* | [**patch_ip**](docs/DefaultApi.md#patch_ip) | **PATCH** /recon/api/v1/ip | 
*DefaultApi* | [**patch_network**](docs/DefaultApi.md#patch_network) | **PATCH** /recon/api/v1/network | 
*DefaultApi* | [**patch_single_saved_views**](docs/DefaultApi.md#patch_single_saved_views) | **PATCH** /recon/api/v1/saved-views/{id} | 
*DefaultApi* | [**patch_social_entity**](docs/DefaultApi.md#patch_social_entity) | **PATCH** /recon/api/v1/social-entity | 
*DefaultApi* | [**patch_target**](docs/DefaultApi.md#patch_target) | **PATCH** /recon/api/v1/target | 
*DefaultApi* | [**paths**](docs/DefaultApi.md#paths) | **GET** /recon/api/v1/paths | 
*DefaultApi* | [**post_saved_views**](docs/DefaultApi.md#post_saved_views) | **POST** /recon/api/v1/saved-views | 
*DefaultApi* | [**tag**](docs/DefaultApi.md#tag) | **GET** /recon/api/v1/tag | 


## Documentation For Models

 - [AllDetectionsForTarget](docs/AllDetectionsForTarget.md)
 - [AllDetectionsForTargetGetOutput](docs/AllDetectionsForTargetGetOutput.md)
 - [Artifact](docs/Artifact.md)
 - [ArtifactGetOutput](docs/ArtifactGetOutput.md)
 - [Detection](docs/Detection.md)
 - [DetectionGetOutput](docs/DetectionGetOutput.md)
 - [EdgeSchema](docs/EdgeSchema.md)
 - [ErrorSchema](docs/ErrorSchema.md)
 - [Hostname](docs/Hostname.md)
 - [HostnameGetOutput](docs/HostnameGetOutput.md)
 - [HostnamePatchIn](docs/HostnamePatchIn.md)
 - [HostnamePatchInput](docs/HostnamePatchInput.md)
 - [HostnamePatchOutput](docs/HostnamePatchOutput.md)
 - [HostnameSingleOutput](docs/HostnameSingleOutput.md)
 - [HostnamesForIp](docs/HostnamesForIp.md)
 - [HostnamesForIpGetOutput](docs/HostnamesForIpGetOutput.md)
 - [HostnamesForIpSingleOutput](docs/HostnamesForIpSingleOutput.md)
 - [Ip](docs/Ip.md)
 - [IpGetOutput](docs/IpGetOutput.md)
 - [IpPatchIn](docs/IpPatchIn.md)
 - [IpPatchInput](docs/IpPatchInput.md)
 - [IpPatchOutput](docs/IpPatchOutput.md)
 - [IpSingleOutput](docs/IpSingleOutput.md)
 - [IpsForHostname](docs/IpsForHostname.md)
 - [IpsForHostnameGetOutput](docs/IpsForHostnameGetOutput.md)
 - [IpsForHostnameSingleOutput](docs/IpsForHostnameSingleOutput.md)
 - [IpsForNetwork](docs/IpsForNetwork.md)
 - [IpsForNetworkGetOutput](docs/IpsForNetworkGetOutput.md)
 - [IpsForNetworkSingleOutput](docs/IpsForNetworkSingleOutput.md)
 - [IpsForService](docs/IpsForService.md)
 - [IpsForServiceGetOutput](docs/IpsForServiceGetOutput.md)
 - [IpsForServiceSingleOutput](docs/IpsForServiceSingleOutput.md)
 - [JsonPatchOperation](docs/JsonPatchOperation.md)
 - [Network](docs/Network.md)
 - [NetworkGetOutput](docs/NetworkGetOutput.md)
 - [NetworkPatchIn](docs/NetworkPatchIn.md)
 - [NetworkPatchInput](docs/NetworkPatchInput.md)
 - [NetworkPatchOutput](docs/NetworkPatchOutput.md)
 - [NetworkSingleOutput](docs/NetworkSingleOutput.md)
 - [NodeSchema](docs/NodeSchema.md)
 - [PathsDataSchema](docs/PathsDataSchema.md)
 - [PathsOutputSchema](docs/PathsOutputSchema.md)
 - [PortsForIp](docs/PortsForIp.md)
 - [PortsForIpGetOutput](docs/PortsForIpGetOutput.md)
 - [PortsForIpSingleOutput](docs/PortsForIpSingleOutput.md)
 - [QuerybuilderGroupMemberSchema](docs/QuerybuilderGroupMemberSchema.md)
 - [QuerybuilderGroupMemberSchema2](docs/QuerybuilderGroupMemberSchema2.md)
 - [QuerybuilderGroupMemberSchema3](docs/QuerybuilderGroupMemberSchema3.md)
 - [QuerybuilderGroupMemberSchema4](docs/QuerybuilderGroupMemberSchema4.md)
 - [QuerybuilderGroupMemberSchema5](docs/QuerybuilderGroupMemberSchema5.md)
 - [QuerybuilderGroupMemberSchema6](docs/QuerybuilderGroupMemberSchema6.md)
 - [QuerybuilderRuleGroupSchema](docs/QuerybuilderRuleGroupSchema.md)
 - [QuerybuilderRuleGroupSchema2](docs/QuerybuilderRuleGroupSchema2.md)
 - [QuerybuilderRuleGroupSchema3](docs/QuerybuilderRuleGroupSchema3.md)
 - [QuerybuilderRuleGroupSchema4](docs/QuerybuilderRuleGroupSchema4.md)
 - [QuerybuilderRuleSchema](docs/QuerybuilderRuleSchema.md)
 - [SavedViews](docs/SavedViews.md)
 - [SavedViewsGetOutput](docs/SavedViewsGetOutput.md)
 - [SavedViewsModelCustomIn](docs/SavedViewsModelCustomIn.md)
 - [SavedViewsPatchIn](docs/SavedViewsPatchIn.md)
 - [SavedViewsPatchSingleInput](docs/SavedViewsPatchSingleInput.md)
 - [SavedViewsPostInput](docs/SavedViewsPostInput.md)
 - [SavedViewsPostOutput](docs/SavedViewsPostOutput.md)
 - [SavedViewsSingleOutput](docs/SavedViewsSingleOutput.md)
 - [Service](docs/Service.md)
 - [ServiceGetOutput](docs/ServiceGetOutput.md)
 - [ServiceSingleOutput](docs/ServiceSingleOutput.md)
 - [SingleDetectionForTarget](docs/SingleDetectionForTarget.md)
 - [SingleDetectionForTargetGetOutput](docs/SingleDetectionForTargetGetOutput.md)
 - [SocialEntity](docs/SocialEntity.md)
 - [SocialEntityGetOutput](docs/SocialEntityGetOutput.md)
 - [SocialEntityPatchIn](docs/SocialEntityPatchIn.md)
 - [SocialEntityPatchInput](docs/SocialEntityPatchInput.md)
 - [SocialEntityPatchOutput](docs/SocialEntityPatchOutput.md)
 - [Statistics](docs/Statistics.md)
 - [StatisticsGetOutput](docs/StatisticsGetOutput.md)
 - [Tagcounts](docs/Tagcounts.md)
 - [TagcountsGetOutput](docs/TagcountsGetOutput.md)
 - [TagcountsSingleOutput](docs/TagcountsSingleOutput.md)
 - [Target](docs/Target.md)
 - [TargetGetOutput](docs/TargetGetOutput.md)
 - [TargetPatchIn](docs/TargetPatchIn.md)
 - [TargetPatchInput](docs/TargetPatchInput.md)
 - [TargetPatchOutput](docs/TargetPatchOutput.md)
 - [TargetSingleOutput](docs/TargetSingleOutput.md)
 - [UserTagNameList](docs/UserTagNameList.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication (JWT)


## Author

support@randori.com


