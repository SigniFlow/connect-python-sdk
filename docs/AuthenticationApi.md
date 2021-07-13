# SigniFlowconnect.AuthenticationApi

All URIs are relative to *https://server-url/API/SignFlowAPIServiceRest.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthenticationApi.md#login) | **POST** /Login | Login
[**post_logout**](AuthenticationApi.md#post_logout) | **POST** /Logout | Logout
[**post_token_extend**](AuthenticationApi.md#post_token_extend) | **POST** /TokenExtend | Token Extend
[**post_token_validate**](AuthenticationApi.md#post_token_validate) | **POST** /TokenValidate | Token Validate


# **login**
> LoginResponse login(login_request)

Login

#### Generates a API Token for the User

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import authentication_api
from SigniFlowconnect.model.login_response import LoginResponse
from SigniFlowconnect.model.login_request import LoginRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    login_request = LoginRequest(
        user_name_field="email@domain.com",
        password_field="Password",
    ) # LoginRequest | ##### Login Request Model

    # example passing only required values which don't have defaults set
    try:
        # Login
        api_response = api_instance.login(login_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling AuthenticationApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)| ##### Login Request Model |
 **content_type** | **str**|  | defaults to "application/json"

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Login Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_logout**
> LogoutResponse post_logout()

Logout

#### Used to log out a user from SigniFlow.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import authentication_api
from SigniFlowconnect.model.logout_request import LogoutRequest
from SigniFlowconnect.model.logout_response import LogoutResponse
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    logout_request = LogoutRequest(
        token_field="token_field_example",
    ) # LogoutRequest | ##### Logout Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Logout
        api_response = api_instance.post_logout()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling AuthenticationApi->post_logout: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Logout
        api_response = api_instance.post_logout(logout_request=logout_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling AuthenticationApi->post_logout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **logout_request** | [**LogoutRequest**](LogoutRequest.md)| ##### Logout Request Model | [optional]

### Return type

[**LogoutResponse**](LogoutResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Logout Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_token_extend**
> TokenExtendResponse post_token_extend()

Token Extend

#### Used to extend the period of time in which the session token is valid.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import authentication_api
from SigniFlowconnect.model.token_extend_response import TokenExtendResponse
from SigniFlowconnect.model.token_extend_request import TokenExtendRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    token_extend_request = TokenExtendRequest(
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
        token_validity_field=3.14,
    ) # TokenExtendRequest | ##### Token Extend Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Token Extend
        api_response = api_instance.post_token_extend()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling AuthenticationApi->post_token_extend: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Token Extend
        api_response = api_instance.post_token_extend(token_extend_request=token_extend_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling AuthenticationApi->post_token_extend: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **token_extend_request** | [**TokenExtendRequest**](TokenExtendRequest.md)| ##### Token Extend Request Model | [optional]

### Return type

[**TokenExtendResponse**](TokenExtendResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Token Extend Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_token_validate**
> TokenValidateResponse post_token_validate()

Token Validate

#### Used to validate the user's session token.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import authentication_api
from SigniFlowconnect.model.token_validate_response import TokenValidateResponse
from SigniFlowconnect.model.token_validate_request import TokenValidateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    token_validate_request = TokenValidateRequest(
        _0="_0_example",
    ) # TokenValidateRequest | ##### Token Validate Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Token Validate
        api_response = api_instance.post_token_validate()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling AuthenticationApi->post_token_validate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Token Validate
        api_response = api_instance.post_token_validate(token_validate_request=token_validate_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling AuthenticationApi->post_token_validate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **token_validate_request** | [**TokenValidateRequest**](TokenValidateRequest.md)| ##### Token Validate Request Model | [optional]

### Return type

[**TokenValidateResponse**](TokenValidateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Token Validate Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

