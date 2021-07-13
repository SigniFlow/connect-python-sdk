# SigniFlowconnect.PortfoliosApi

All URIs are relative to *https://server-url/API/SignFlowAPIServiceRest.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_create_portfolio**](PortfoliosApi.md#post_create_portfolio) | **POST** /CreatePortfolio | Create Portfolio
[**post_download_portfolio**](PortfoliosApi.md#post_download_portfolio) | **POST** /DownloadPortfolio | Download Portfolio
[**post_link_to_portfolio**](PortfoliosApi.md#post_link_to_portfolio) | **POST** /LinkToPortfolio | Link To Portfolio
[**post_set_document_order**](PortfoliosApi.md#post_set_document_order) | **POST** /SetDocumentOrder | Set Document Order
[**post_share_portfolio**](PortfoliosApi.md#post_share_portfolio) | **POST** /SharePortfolio | Share Portfolio
[**post_share_portfolio_no_email**](PortfoliosApi.md#post_share_portfolio_no_email) | **POST** /SharePortfolio_No_Email | Share Portfolio No Email


# **post_create_portfolio**
> CreatePortfolioResponse post_create_portfolio()

Create Portfolio

#### Used to create a portfolio to group documents.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import portfolios_api
from SigniFlowconnect.model.create_portfolio_request import CreatePortfolioRequest
from SigniFlowconnect.model.create_portfolio_response import CreatePortfolioResponse
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = portfolios_api.PortfoliosApi(api_client)
    create_portfolio_request = CreatePortfolioRequest(
        doc_id_field=2147483647,
        portfolio_name_field="Application Portfolio",
        token_id_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # CreatePortfolioRequest | ##### Create Portfolio Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Portfolio
        api_response = api_instance.post_create_portfolio()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling PortfoliosApi->post_create_portfolio: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Portfolio
        api_response = api_instance.post_create_portfolio(create_portfolio_request=create_portfolio_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling PortfoliosApi->post_create_portfolio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **create_portfolio_request** | [**CreatePortfolioRequest**](CreatePortfolioRequest.md)| ##### Create Portfolio Request Model | [optional]

### Return type

[**CreatePortfolioResponse**](CreatePortfolioResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Create Portfolio Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_download_portfolio**
> DownloadPortfolioResponse post_download_portfolio()

Download Portfolio

#### Used to return a string that is then used to download a portfolio.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import portfolios_api
from SigniFlowconnect.model.download_portfolio_response import DownloadPortfolioResponse
from SigniFlowconnect.model.download_portfolio_request import DownloadPortfolioRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = portfolios_api.PortfoliosApi(api_client)
    download_portfolio_request = DownloadPortfolioRequest(
        portfolio_id_field=111112,
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # DownloadPortfolioRequest | ##### Download Portfolio Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Download Portfolio
        api_response = api_instance.post_download_portfolio()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling PortfoliosApi->post_download_portfolio: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Download Portfolio
        api_response = api_instance.post_download_portfolio(download_portfolio_request=download_portfolio_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling PortfoliosApi->post_download_portfolio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **download_portfolio_request** | [**DownloadPortfolioRequest**](DownloadPortfolioRequest.md)| ##### Download Portfolio Request Model | [optional]

### Return type

[**DownloadPortfolioResponse**](DownloadPortfolioResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Download Portfolio Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_link_to_portfolio**
> LinkToPortfolioResponse post_link_to_portfolio()

Link To Portfolio

#### Used to get the url link to a portfolio.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import portfolios_api
from SigniFlowconnect.model.link_to_portfolio_response import LinkToPortfolioResponse
from SigniFlowconnect.model.link_to_portfolio_request import LinkToPortfolioRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = portfolios_api.PortfoliosApi(api_client)
    link_to_portfolio_request = LinkToPortfolioRequest(
        doc_id_field="doc_id_field_example",
        document_name_field="document_name_field_example",
        portfolio_id_field="portfolio_id_field_example",
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # LinkToPortfolioRequest | ##### Link To Portfolio Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Link To Portfolio
        api_response = api_instance.post_link_to_portfolio()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling PortfoliosApi->post_link_to_portfolio: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Link To Portfolio
        api_response = api_instance.post_link_to_portfolio(link_to_portfolio_request=link_to_portfolio_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling PortfoliosApi->post_link_to_portfolio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **link_to_portfolio_request** | [**LinkToPortfolioRequest**](LinkToPortfolioRequest.md)| ##### Link To Portfolio Request Model | [optional]

### Return type

[**LinkToPortfolioResponse**](LinkToPortfolioResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Link To Portfolio Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_set_document_order**
> SetDocumentOrderResponse post_set_document_order()

Set Document Order

#### Used to set the order of documents that needs to be signed.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import portfolios_api
from SigniFlowconnect.model.set_document_order_response import SetDocumentOrderResponse
from SigniFlowconnect.model.set_document_order_request import SetDocumentOrderRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = portfolios_api.PortfoliosApi(api_client)
    set_document_order_request = SetDocumentOrderRequest(
        doc_id_field="doc_id_field_example",
        document_order_field="document_order_field_example",
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # SetDocumentOrderRequest | ##### Set Document Order Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set Document Order
        api_response = api_instance.post_set_document_order()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling PortfoliosApi->post_set_document_order: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set Document Order
        api_response = api_instance.post_set_document_order(set_document_order_request=set_document_order_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling PortfoliosApi->post_set_document_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **set_document_order_request** | [**SetDocumentOrderRequest**](SetDocumentOrderRequest.md)| ##### Set Document Order Request Model | [optional]

### Return type

[**SetDocumentOrderResponse**](SetDocumentOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Set Document Order Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_share_portfolio**
> SharePortfolioResponse post_share_portfolio()

Share Portfolio

#### Used when a user wants to share a portfolio with someone else.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import portfolios_api
from SigniFlowconnect.model.share_portfolio_request import SharePortfolioRequest
from SigniFlowconnect.model.share_portfolio_response import SharePortfolioResponse
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = portfolios_api.PortfoliosApi(api_client)
    share_portfolio_request = SharePortfolioRequest(
        access_level_field=3.14,
        portfolio_id_field="portfolio_id_field_example",
        share_option_field=3.14,
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
        unique_id_field="unique_id_field_example",
    ) # SharePortfolioRequest | ##### Share Portfolio Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Share Portfolio
        api_response = api_instance.post_share_portfolio()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling PortfoliosApi->post_share_portfolio: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Share Portfolio
        api_response = api_instance.post_share_portfolio(share_portfolio_request=share_portfolio_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling PortfoliosApi->post_share_portfolio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **share_portfolio_request** | [**SharePortfolioRequest**](SharePortfolioRequest.md)| ##### Share Portfolio Request Model | [optional]

### Return type

[**SharePortfolioResponse**](SharePortfolioResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Share Portfolio Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_share_portfolio_no_email**
> SharePortfolioNoEmailResponse post_share_portfolio_no_email()

Share Portfolio No Email

#### Used when a user wants to share a portfolio without sending out an email.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import portfolios_api
from SigniFlowconnect.model.share_portfolio_no_email_response import SharePortfolioNoEmailResponse
from SigniFlowconnect.model.share_portfolio_no_email_request import SharePortfolioNoEmailRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = portfolios_api.PortfoliosApi(api_client)
    share_portfolio_no_email_request = SharePortfolioNoEmailRequest(
        access_level_field=3.14,
        portfolio_id_field="portfolio_id_field_example",
        share_option_field=3.14,
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
        unique_id_field="unique_id_field_example",
    ) # SharePortfolioNoEmailRequest | ##### Share Portfolio No Email Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Share Portfolio No Email
        api_response = api_instance.post_share_portfolio_no_email()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling PortfoliosApi->post_share_portfolio_no_email: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Share Portfolio No Email
        api_response = api_instance.post_share_portfolio_no_email(share_portfolio_no_email_request=share_portfolio_no_email_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling PortfoliosApi->post_share_portfolio_no_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **share_portfolio_no_email_request** | [**SharePortfolioNoEmailRequest**](SharePortfolioNoEmailRequest.md)| ##### Share Portfolio No Email Request Model | [optional]

### Return type

[**SharePortfolioNoEmailResponse**](SharePortfolioNoEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Share Portfolio No Email Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

