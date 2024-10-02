# randori_api_sdk.ValidationApi

All URIs are relative to *https://app.randori.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_activity_configuration_version**](ValidationApi.md#validate_activity_configuration_version) | **POST** /cms/api/v1/activity-configuration-versions/{id}/validate | Validate activity configuration-version


# **validate_activity_configuration_version**
> CmspbStartValidationSeriesResponse validate_activity_configuration_version(id, cmspb_start_validation_series_request)

Validate activity configuration-version

Validate activity configuration version

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import randori_api_sdk
from randori_api_sdk.api import validation_api
from randori_api_sdk.model.cmspb_start_validation_series_response import CmspbStartValidationSeriesResponse
from randori_api_sdk.model.cmspb_start_validation_series_request import CmspbStartValidationSeriesRequest
from pprint import pprint
# Defining the host is optional and defaults to https://app.randori.io
# See configuration.py for a list of all supported configuration parameters.
configuration = randori_api_sdk.Configuration(
    host = "https://app.randori.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API Key
configuration = randori_api_sdk.Configuration(
    api_key = 'YOUR_API_KEY'
)

# Configure Bearer authorization (JWT): bearerAuth (Deprecated)
configuration = randori_api_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with randori_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = validation_api.ValidationApi(api_client)
    id = "id_example" # str | Activity Configuration Version ID
    cmspb_start_validation_series_request = CmspbStartValidationSeriesRequest(
        message=[
            ValidationpbValidationEvent(
                detections=[
                    PlatformpbDetection(
                        affiliation=1,
                        affiliation_display=1,
                        affiliation_override=True,
                        authority_display=True,
                        authority_distance=1,
                        authority_override=True,
                        authority_path=[
                            "authority_path_example",
                        ],
                        authority_source="authority_source_example",
                        authorization_state=PlatformpbAuthorizationState(0),
                        confidence=1,
                        confidence_display=1,
                        confidence_override=True,
                        detection_criteria=StructpbStruct(
                            fields={
                                "key": StructpbValue(
                                    kind=None,
                                ),
                            },
                        ),
                        discovery_distance=1,
                        discovery_path=[
                            "discovery_path_example",
                        ],
                        discovery_source="discovery_source_example",
                        first_time=TimestamppbTimestamp(
                            nanos=1,
                            seconds=1,
                        ),
                        hostname_id="hostname_id_example",
                        id="id_example",
                        lens_view="lens_view_example",
                        network_id="network_id_example",
                        perspective="perspective_example",
                        perspective_id="perspective_id_example",
                        poc_id="poc_id_example",
                        port_id="port_id_example",
                        service=PlatformpbService(
                            applicability=1,
                            attack_note="attack_note_example",
                            cpe=StructpbStruct(
                                fields={
                                    "key": StructpbValue(
                                        kind=None,
                                    ),
                                },
                            ),
                            creator_type="creator_type_example",
                            creator_uuid="creator_uuid_example",
                            criticality=1,
                            deleted=True,
                            description="description_example",
                            description_source="description_source_example",
                            enumerability=1,
                            first_time=TimestamppbTimestamp(
                                nanos=1,
                                seconds=1,
                            ),
                            id="id_example",
                            name="name_example",
                            post_exploit=1,
                            private_weakness=1,
                            promoted=True,
                            promoter="promoter_example",
                            promotion_time=TimestamppbTimestamp(
                                nanos=1,
                                seconds=1,
                            ),
                            public_weakness=1,
                            randori_notes="randori_notes_example",
                            reference="reference_example",
                            research=1,
                            svc_type="svc_type_example",
                            sys_period="sys_period_example",
                            target_temptation=1,
                            tech_category=[
                                "tech_category_example",
                            ],
                            temptation_last_modified=TimestamppbTimestamp(
                                nanos=1,
                                seconds=1,
                            ),
                            time=TimestamppbTimestamp(
                                nanos=1,
                                seconds=1,
                            ),
                            type="type_example",
                            vendor="vendor_example",
                            version="version_example",
                        ),
                        service_id="service_id_example",
                        time=TimestamppbTimestamp(
                            nanos=1,
                            seconds=1,
                        ),
                        type="type_example",
                        validated_vulnerabilities=[
                            "validated_vulnerabilities_example",
                        ],
                    ),
                ],
                entity=PlatformpbEntity(
                    authority_display=True,
                    authority_distance=1,
                    authority_override=True,
                    authorization_state=PlatformpbAuthorizationState(0),
                    deleted=True,
                    detection_criteria=StructpbStruct(
                        fields={
                            "key": StructpbValue(
                                kind=None,
                            ),
                        },
                    ),
                    first_time=TimestamppbTimestamp(
                        nanos=1,
                        seconds=1,
                    ),
                    hostname_type="hostname_type_example",
                    id="id_example",
                    lens_view="lens_view_example",
                    network_size=1,
                    orig_lens_view="orig_lens_view_example",
                    perspective=PlatformpbEntityPerspective(
                        capabilities=StructpbStruct(
                            fields={
                                "key": StructpbValue(
                                    kind=None,
                                ),
                            },
                        ),
                        tags=[
                            "tags_example",
                        ],
                        type="type_example",
                    ),
                    perspective_id="perspective_id_example",
                    time=TimestamppbTimestamp(
                        nanos=1,
                        seconds=1,
                    ),
                    type="type_example",
                    value="value_example",
                ),
                open_ports=[
                    1,
                ],
                service=PlatformpbService(
                    applicability=1,
                    attack_note="attack_note_example",
                    cpe=StructpbStruct(
                        fields={
                            "key": StructpbValue(
                                kind=None,
                            ),
                        },
                    ),
                    creator_type="creator_type_example",
                    creator_uuid="creator_uuid_example",
                    criticality=1,
                    deleted=True,
                    description="description_example",
                    description_source="description_source_example",
                    enumerability=1,
                    first_time=TimestamppbTimestamp(
                        nanos=1,
                        seconds=1,
                    ),
                    id="id_example",
                    name="name_example",
                    post_exploit=1,
                    private_weakness=1,
                    promoted=True,
                    promoter="promoter_example",
                    promotion_time=TimestamppbTimestamp(
                        nanos=1,
                        seconds=1,
                    ),
                    public_weakness=1,
                    randori_notes="randori_notes_example",
                    reference="reference_example",
                    research=1,
                    svc_type="svc_type_example",
                    sys_period="sys_period_example",
                    target_temptation=1,
                    tech_category=[
                        "tech_category_example",
                    ],
                    temptation_last_modified=TimestamppbTimestamp(
                        nanos=1,
                        seconds=1,
                    ),
                    time=TimestamppbTimestamp(
                        nanos=1,
                        seconds=1,
                    ),
                    type="type_example",
                    vendor="vendor_example",
                    version="version_example",
                ),
            ),
        ],
        message_source=ValidationpbStartValidationSeriesRequestMessageSource(0),
        number_limit=1,
        time_limit=1,
    ) # CmspbStartValidationSeriesRequest | Validation Series Request

    # example passing only required values which don't have defaults set
    try:
        # Validate activity configuration-version
        api_response = api_instance.validate_activity_configuration_version(id, cmspb_start_validation_series_request)
        pprint(api_response)
    except randori_api_sdk.ApiException as e:
        print("Exception when calling ValidationApi->validate_activity_configuration_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Activity Configuration Version ID |
 **cmspb_start_validation_series_request** | [**CmspbStartValidationSeriesRequest**](CmspbStartValidationSeriesRequest.md)| Validation Series Request |

### Return type

[**CmspbStartValidationSeriesResponse**](CmspbStartValidationSeriesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

