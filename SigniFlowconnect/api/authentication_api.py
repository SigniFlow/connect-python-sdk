"""
    SigniFlow OpenAPI Spec v1

    ## SigniFlow API used to automate esignature workflow creation and management.   # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@signiflow.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from SigniFlowconnect.api_client import ApiClient, Endpoint as _Endpoint
from SigniFlowconnect.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from SigniFlowconnect.model.login_request import LoginRequest
from SigniFlowconnect.model.login_response import LoginResponse
from SigniFlowconnect.model.logout_request import LogoutRequest
from SigniFlowconnect.model.logout_response import LogoutResponse
from SigniFlowconnect.model.token_extend_request import TokenExtendRequest
from SigniFlowconnect.model.token_extend_response import TokenExtendResponse
from SigniFlowconnect.model.token_validate_request import TokenValidateRequest
from SigniFlowconnect.model.token_validate_response import TokenValidateResponse


class AuthenticationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __login(
            self,
            login_request,
            content_type="application/json",
            **kwargs
        ):
            """Login  # noqa: E501

            #### Generates a API Token for the User  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.login(login_request, content_type="application/json", async_req=True)
            >>> result = thread.get()

            Args:
                login_request (LoginRequest): ##### Login Request Model
                content_type (str): defaults to "application/json", must be one of ["application/json"]

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                LoginResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['content_type'] = \
                content_type
            kwargs['login_request'] = \
                login_request
            return self.call_with_http_info(**kwargs)

        self.login = _Endpoint(
            settings={
                'response_type': (LoginResponse,),
                'auth': [],
                'endpoint_path': '/Login',
                'operation_id': 'login',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'content_type',
                    'login_request',
                ],
                'required': [
                    'content_type',
                    'login_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'content_type':
                        (str,),
                    'login_request':
                        (LoginRequest,),
                },
                'attribute_map': {
                    'content_type': 'Content-Type',
                },
                'location_map': {
                    'content_type': 'header',
                    'login_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__login
        )

        def __post_logout(
            self,
            content_type="application/json",
            **kwargs
        ):
            """Logout  # noqa: E501

            #### Used to log out a user from SigniFlow.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_logout(content_type="application/json", async_req=True)
            >>> result = thread.get()

            Args:
                content_type (str): defaults to "application/json", must be one of ["application/json"]

            Keyword Args:
                logout_request (LogoutRequest): ##### Logout Request Model. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                LogoutResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['content_type'] = \
                content_type
            return self.call_with_http_info(**kwargs)

        self.post_logout = _Endpoint(
            settings={
                'response_type': (LogoutResponse,),
                'auth': [],
                'endpoint_path': '/Logout',
                'operation_id': 'post_logout',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'content_type',
                    'logout_request',
                ],
                'required': [
                    'content_type',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'content_type':
                        (str,),
                    'logout_request':
                        (LogoutRequest,),
                },
                'attribute_map': {
                    'content_type': 'Content-Type',
                },
                'location_map': {
                    'content_type': 'header',
                    'logout_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__post_logout
        )

        def __post_token_extend(
            self,
            content_type="application/json",
            **kwargs
        ):
            """Token Extend  # noqa: E501

            #### Used to extend the period of time in which the session token is valid.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_token_extend(content_type="application/json", async_req=True)
            >>> result = thread.get()

            Args:
                content_type (str): defaults to "application/json", must be one of ["application/json"]

            Keyword Args:
                token_extend_request (TokenExtendRequest): ##### Token Extend Request Model. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                TokenExtendResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['content_type'] = \
                content_type
            return self.call_with_http_info(**kwargs)

        self.post_token_extend = _Endpoint(
            settings={
                'response_type': (TokenExtendResponse,),
                'auth': [],
                'endpoint_path': '/TokenExtend',
                'operation_id': 'post_token_extend',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'content_type',
                    'token_extend_request',
                ],
                'required': [
                    'content_type',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'content_type':
                        (str,),
                    'token_extend_request':
                        (TokenExtendRequest,),
                },
                'attribute_map': {
                    'content_type': 'Content-Type',
                },
                'location_map': {
                    'content_type': 'header',
                    'token_extend_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__post_token_extend
        )

        def __post_token_validate(
            self,
            content_type="application/json",
            **kwargs
        ):
            """Token Validate  # noqa: E501

            #### Used to validate the user's session token.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_token_validate(content_type="application/json", async_req=True)
            >>> result = thread.get()

            Args:
                content_type (str): defaults to "application/json", must be one of ["application/json"]

            Keyword Args:
                token_validate_request (TokenValidateRequest): ##### Token Validate Request Model. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                TokenValidateResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['content_type'] = \
                content_type
            return self.call_with_http_info(**kwargs)

        self.post_token_validate = _Endpoint(
            settings={
                'response_type': (TokenValidateResponse,),
                'auth': [],
                'endpoint_path': '/TokenValidate',
                'operation_id': 'post_token_validate',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'content_type',
                    'token_validate_request',
                ],
                'required': [
                    'content_type',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'content_type':
                        (str,),
                    'token_validate_request':
                        (TokenValidateRequest,),
                },
                'attribute_map': {
                    'content_type': 'Content-Type',
                },
                'location_map': {
                    'content_type': 'header',
                    'token_validate_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__post_token_validate
        )
