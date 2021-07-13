# SigniFlowconnect.TemplatesApi

All URIs are relative to *https://server-url/API/SignFlowAPIServiceRest.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_apply_prepper_template**](TemplatesApi.md#post_apply_prepper_template) | **POST** /ApplyPrepperTemplate | Apply a Prepper template
[**post_get_document_tag_field_box_position**](TemplatesApi.md#post_get_document_tag_field_box_position) | **POST** /GetDocumentTagFieldBoxPosition | Get Document Tag Field Box Position
[**post_get_document_tag_field_position**](TemplatesApi.md#post_get_document_tag_field_position) | **POST** /GetDocumentTagFieldPosition | Get Document Tag Field Position
[**post_get_prepper_template**](TemplatesApi.md#post_get_prepper_template) | **POST** /GetPrepperTemplate | Get Prepper Template
[**post_get_prepper_template_list**](TemplatesApi.md#post_get_prepper_template_list) | **POST** /GetPrepperTemplateList | Get Prepper Template List


# **post_apply_prepper_template**
> ApplyPrepperTemplateResponse post_apply_prepper_template()

Apply a Prepper template

#### Used when applying a templaet to a document.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import templates_api
from SigniFlowconnect.model.apply_prepper_template_request import ApplyPrepperTemplateRequest
from SigniFlowconnect.model.apply_prepper_template_response import ApplyPrepperTemplateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)
    apply_prepper_template_request = ApplyPrepperTemplateRequest(
        doc_id_field=2147483647,
        prepper_template_id_field=21344,
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # ApplyPrepperTemplateRequest | ##### Apply A Prepper Template Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Apply a Prepper template
        api_response = api_instance.post_apply_prepper_template()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling TemplatesApi->post_apply_prepper_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Apply a Prepper template
        api_response = api_instance.post_apply_prepper_template(apply_prepper_template_request=apply_prepper_template_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling TemplatesApi->post_apply_prepper_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **apply_prepper_template_request** | [**ApplyPrepperTemplateRequest**](ApplyPrepperTemplateRequest.md)| ##### Apply A Prepper Template Request Model | [optional]

### Return type

[**ApplyPrepperTemplateResponse**](ApplyPrepperTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Apply A Prepper Template Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_document_tag_field_box_position**
> GetDocumentTagFieldBoxPositionResponse post_get_document_tag_field_box_position()

Get Document Tag Field Box Position

#### Used to get the tag field box position on a document.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import templates_api
from SigniFlowconnect.model.get_document_tag_field_box_position_response import GetDocumentTagFieldBoxPositionResponse
from SigniFlowconnect.model.get_document_tag_field_box_position_request import GetDocumentTagFieldBoxPositionRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)
    get_document_tag_field_box_position_request = GetDocumentTagFieldBoxPositionRequest(
        doc_id_field=3.14,
        tag_name_field="tag_name_field_example",
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # GetDocumentTagFieldBoxPositionRequest | ##### Get Document Tag Field Box Position Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Document Tag Field Box Position
        api_response = api_instance.post_get_document_tag_field_box_position()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling TemplatesApi->post_get_document_tag_field_box_position: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Document Tag Field Box Position
        api_response = api_instance.post_get_document_tag_field_box_position(get_document_tag_field_box_position_request=get_document_tag_field_box_position_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling TemplatesApi->post_get_document_tag_field_box_position: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **get_document_tag_field_box_position_request** | [**GetDocumentTagFieldBoxPositionRequest**](GetDocumentTagFieldBoxPositionRequest.md)| ##### Get Document Tag Field Box Position Request Model | [optional]

### Return type

[**GetDocumentTagFieldBoxPositionResponse**](GetDocumentTagFieldBoxPositionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Get Document Tag Field Box Position Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_document_tag_field_position**
> GetDocumentTagFieldPositionResponse post_get_document_tag_field_position()

Get Document Tag Field Position

#### Used to get the tag position on a document.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import templates_api
from SigniFlowconnect.model.get_document_tag_field_position_response import GetDocumentTagFieldPositionResponse
from SigniFlowconnect.model.get_document_tag_field_position_request import GetDocumentTagFieldPositionRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)
    get_document_tag_field_position_request = GetDocumentTagFieldPositionRequest(
        doc_id_field=3.14,
        tag_name_field="tag_name_field_example",
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # GetDocumentTagFieldPositionRequest | ##### Get Document Tag Field Position Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Document Tag Field Position
        api_response = api_instance.post_get_document_tag_field_position()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling TemplatesApi->post_get_document_tag_field_position: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Document Tag Field Position
        api_response = api_instance.post_get_document_tag_field_position(get_document_tag_field_position_request=get_document_tag_field_position_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling TemplatesApi->post_get_document_tag_field_position: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **get_document_tag_field_position_request** | [**GetDocumentTagFieldPositionRequest**](GetDocumentTagFieldPositionRequest.md)| ##### Get Document Tag Field Position Request Model | [optional]

### Return type

[**GetDocumentTagFieldPositionResponse**](GetDocumentTagFieldPositionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Get Document Tag Field Position Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_prepper_template**
> GetPrepperTemplateResponse post_get_prepper_template()

Get Prepper Template

#### Used to get a document template.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import templates_api
from SigniFlowconnect.model.get_prepper_template_response import GetPrepperTemplateResponse
from SigniFlowconnect.model.get_prepper_template_request import GetPrepperTemplateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)
    get_prepper_template_request = GetPrepperTemplateRequest(
        doc_id_field=3.14,
        prepper_template_id_field=3.14,
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # GetPrepperTemplateRequest | ##### Get Prepper Template Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Prepper Template
        api_response = api_instance.post_get_prepper_template()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling TemplatesApi->post_get_prepper_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Prepper Template
        api_response = api_instance.post_get_prepper_template(get_prepper_template_request=get_prepper_template_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling TemplatesApi->post_get_prepper_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **get_prepper_template_request** | [**GetPrepperTemplateRequest**](GetPrepperTemplateRequest.md)| ##### Get Prepper Template Request Model | [optional]

### Return type

[**GetPrepperTemplateResponse**](GetPrepperTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Get Prepper Template Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_prepper_template_list**
> GetPrepperTemplateListResponse post_get_prepper_template_list()

Get Prepper Template List

#### Used to get a list of document templates.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import templates_api
from SigniFlowconnect.model.get_prepper_template_list_request import GetPrepperTemplateListRequest
from SigniFlowconnect.model.get_prepper_template_list_response import GetPrepperTemplateListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)
    get_prepper_template_list_request = GetPrepperTemplateListRequest(
        template_folder_field=3.14,
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # GetPrepperTemplateListRequest | ##### Get Prepper Template List Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Prepper Template List
        api_response = api_instance.post_get_prepper_template_list()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling TemplatesApi->post_get_prepper_template_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Prepper Template List
        api_response = api_instance.post_get_prepper_template_list(get_prepper_template_list_request=get_prepper_template_list_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling TemplatesApi->post_get_prepper_template_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **get_prepper_template_list_request** | [**GetPrepperTemplateListRequest**](GetPrepperTemplateListRequest.md)| ##### Get Prepper Template List Request Model | [optional]

### Return type

[**GetPrepperTemplateListResponse**](GetPrepperTemplateListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Get Prepper Template List Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

