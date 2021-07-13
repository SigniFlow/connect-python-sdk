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
from SigniFlowconnect.model.get_audit_document_request import GetAuditDocumentRequest
from SigniFlowconnect.model.get_audit_document_response import GetAuditDocumentResponse
from SigniFlowconnect.model.get_document_audit_request import GetDocumentAuditRequest
from SigniFlowconnect.model.get_document_audit_response import GetDocumentAuditResponse


class AuditsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __post_get_audit_document(
            self,
            content_type="application/json",
            **kwargs
        ):
            """Get Audit Document  # noqa: E501

            #### Used to get an audit document.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_get_audit_document(content_type="application/json", async_req=True)
            >>> result = thread.get()

            Args:
                content_type (str): defaults to "application/json", must be one of ["application/json"]

            Keyword Args:
                get_audit_document_request (GetAuditDocumentRequest): ##### Get Audit Document Request Model. [optional]
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
                GetAuditDocumentResponse
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

        self.post_get_audit_document = _Endpoint(
            settings={
                'response_type': (GetAuditDocumentResponse,),
                'auth': [],
                'endpoint_path': '/GetAuditDocument',
                'operation_id': 'post_get_audit_document',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'content_type',
                    'get_audit_document_request',
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
                    'get_audit_document_request':
                        (GetAuditDocumentRequest,),
                },
                'attribute_map': {
                    'content_type': 'Content-Type',
                },
                'location_map': {
                    'content_type': 'header',
                    'get_audit_document_request': 'body',
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
            callable=__post_get_audit_document
        )

        def __post_get_document_audit(
            self,
            content_type="application/json",
            **kwargs
        ):
            """Get Document Audit  # noqa: E501

            #### Used to get the audit information from a document.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_get_document_audit(content_type="application/json", async_req=True)
            >>> result = thread.get()

            Args:
                content_type (str): defaults to "application/json", must be one of ["application/json"]

            Keyword Args:
                get_document_audit_request (GetDocumentAuditRequest): ##### Get Document Audit Request Model. [optional]
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
                GetDocumentAuditResponse
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

        self.post_get_document_audit = _Endpoint(
            settings={
                'response_type': (GetDocumentAuditResponse,),
                'auth': [],
                'endpoint_path': '/GetDocumentAudit',
                'operation_id': 'post_get_document_audit',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'content_type',
                    'get_document_audit_request',
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
                    'get_document_audit_request':
                        (GetDocumentAuditRequest,),
                },
                'attribute_map': {
                    'content_type': 'Content-Type',
                },
                'location_map': {
                    'content_type': 'header',
                    'get_document_audit_request': 'body',
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
            callable=__post_get_document_audit
        )
