# SigniFlowconnect.ViewersApi

All URIs are relative to *https://server-url/API/SignFlowAPIServiceRest.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_get_doc_link**](ViewersApi.md#post_get_doc_link) | **POST** /GetDocLink | Get Document Link
[**post_get_document_prepper_link**](ViewersApi.md#post_get_document_prepper_link) | **POST** /GetDocumentPrepperLink | Get Document Prepper Link


# **post_get_doc_link**
> GetDocLinkResponse post_get_doc_link()

Get Document Link

#### Used to get the document link that will be used to sign a document.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import viewers_api
from SigniFlowconnect.model.get_doc_link_request import GetDocLinkRequest
from SigniFlowconnect.model.get_doc_link_response import GetDocLinkResponse
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = viewers_api.ViewersApi(api_client)
    get_doc_link_request = GetDocLinkRequest(
        doc_id_field="doc_id_field_example",
        email_field="email@domain.com",
        return_url_field="return_url_field_example",
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # GetDocLinkRequest | ##### Get Document Link Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Document Link
        api_response = api_instance.post_get_doc_link()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling ViewersApi->post_get_doc_link: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Document Link
        api_response = api_instance.post_get_doc_link(get_doc_link_request=get_doc_link_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling ViewersApi->post_get_doc_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **get_doc_link_request** | [**GetDocLinkRequest**](GetDocLinkRequest.md)| ##### Get Document Link Request Model | [optional]

### Return type

[**GetDocLinkResponse**](GetDocLinkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Get Document Link Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_document_prepper_link**
> GetDocumentPrepperLinkResponse post_get_document_prepper_link()

Get Document Prepper Link

#### Used to get a document prepper link (url).

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import viewers_api
from SigniFlowconnect.model.get_document_prepper_link_request import GetDocumentPrepperLinkRequest
from SigniFlowconnect.model.get_document_prepper_link_response import GetDocumentPrepperLinkResponse
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = viewers_api.ViewersApi(api_client)
    get_document_prepper_link_request = GetDocumentPrepperLinkRequest(
        doc_id_field="doc_id_field_example",
        email_setting_field=3.14,
        return_url_field="return_url_field_example",
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # GetDocumentPrepperLinkRequest | ##### Get Document Prepper Link Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Document Prepper Link
        api_response = api_instance.post_get_document_prepper_link()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling ViewersApi->post_get_document_prepper_link: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Document Prepper Link
        api_response = api_instance.post_get_document_prepper_link(get_document_prepper_link_request=get_document_prepper_link_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling ViewersApi->post_get_document_prepper_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **get_document_prepper_link_request** | [**GetDocumentPrepperLinkRequest**](GetDocumentPrepperLinkRequest.md)| ##### Get Document Prepper Link Request Model | [optional]

### Return type

[**GetDocumentPrepperLinkResponse**](GetDocumentPrepperLinkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Get Document Prepper Link Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

