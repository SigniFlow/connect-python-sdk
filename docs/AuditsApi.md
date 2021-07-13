# SigniFlowconnect.AuditsApi

All URIs are relative to *https://server-url/API/SignFlowAPIServiceRest.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_get_audit_document**](AuditsApi.md#post_get_audit_document) | **POST** /GetAuditDocument | Get Audit Document
[**post_get_document_audit**](AuditsApi.md#post_get_document_audit) | **POST** /GetDocumentAudit | Get Document Audit


# **post_get_audit_document**
> GetAuditDocumentResponse post_get_audit_document()

Get Audit Document

#### Used to get an audit document.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import audits_api
from SigniFlowconnect.model.get_audit_document_request import GetAuditDocumentRequest
from SigniFlowconnect.model.get_audit_document_response import GetAuditDocumentResponse
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = audits_api.AuditsApi(api_client)
    get_audit_document_request = GetAuditDocumentRequest(
        doc_id_field="doc_id_field_example",
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # GetAuditDocumentRequest | ##### Get Audit Document Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Audit Document
        api_response = api_instance.post_get_audit_document()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling AuditsApi->post_get_audit_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Audit Document
        api_response = api_instance.post_get_audit_document(get_audit_document_request=get_audit_document_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling AuditsApi->post_get_audit_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **get_audit_document_request** | [**GetAuditDocumentRequest**](GetAuditDocumentRequest.md)| ##### Get Audit Document Request Model | [optional]

### Return type

[**GetAuditDocumentResponse**](GetAuditDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Get Audit Document Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_document_audit**
> GetDocumentAuditResponse post_get_document_audit()

Get Document Audit

#### Used to get the audit information from a document.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import audits_api
from SigniFlowconnect.model.get_document_audit_request import GetDocumentAuditRequest
from SigniFlowconnect.model.get_document_audit_response import GetDocumentAuditResponse
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = audits_api.AuditsApi(api_client)
    get_document_audit_request = GetDocumentAuditRequest(
        doc_id_field="doc_id_field_example",
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # GetDocumentAuditRequest | ##### Get Document Audit Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Document Audit
        api_response = api_instance.post_get_document_audit()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling AuditsApi->post_get_document_audit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Document Audit
        api_response = api_instance.post_get_document_audit(get_document_audit_request=get_document_audit_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling AuditsApi->post_get_document_audit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **get_document_audit_request** | [**GetDocumentAuditRequest**](GetDocumentAuditRequest.md)| ##### Get Document Audit Request Model | [optional]

### Return type

[**GetDocumentAuditResponse**](GetDocumentAuditResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Get Document Audit Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

