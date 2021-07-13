# SigniFlowconnect.WorkFlowApi

All URIs are relative to *https://server-url/API/SignFlowAPIServiceRest.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow**](WorkFlowApi.md#create_workflow) | **POST** /CreateWorkflow | Create Workflow
[**get_document**](WorkFlowApi.md#get_document) | **POST** /GetDoc | Get Document
[**post_add_workflow_step**](WorkFlowApi.md#post_add_workflow_step) | **POST** /AddWorkflowStepV2 | Add a Workflow step
[**post_cancel_flow**](WorkFlowApi.md#post_cancel_flow) | **POST** /CancelFlow | Cancel Flow
[**post_delete_doc**](WorkFlowApi.md#post_delete_doc) | **POST** /DeleteDoc | Delete Document
[**post_doc_prepper_add_field**](WorkFlowApi.md#post_doc_prepper_add_field) | **POST** /DocPrepperAddFieldsFlowID | Document Prepper Add Fields
[**post_doc_prepper_advanced_fields**](WorkFlowApi.md#post_doc_prepper_advanced_fields) | **POST** /DocPrepperAdvancedFields | Document Prepper Add Advanced Fields
[**post_full_workflow**](WorkFlowApi.md#post_full_workflow) | **POST** /FullWorkflow | FullWorkflow
[**post_get_doc_status**](WorkFlowApi.md#post_get_doc_status) | **POST** /GetDocStatus | Get Document Status
[**post_initiate_flow**](WorkFlowApi.md#post_initiate_flow) | **POST** /InitiateFlow | Initiate Flow
[**post_initiate_flow_no_email**](WorkFlowApi.md#post_initiate_flow_no_email) | **POST** /InitiateFlow_No_Email | Initiate Flow No Email
[**post_initiate_flow_no_initial_email**](WorkFlowApi.md#post_initiate_flow_no_initial_email) | **POST** /InitiateFlow_No_Initial_Email | Initiate Flow No Initial Email
[**post_workflow_sign**](WorkFlowApi.md#post_workflow_sign) | **POST** /WorkflowSign | Workflow Sign


# **create_workflow**
> CreateWorkflowResponse create_workflow(create_workflow_request)

Create Workflow

#### Used to start a new workflow by passing a Base64 encoded document to SigniFlow

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import work_flow_api
from SigniFlowconnect.model.create_workflow_request import CreateWorkflowRequest
from SigniFlowconnect.model.create_workflow_response import CreateWorkflowResponse
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = work_flow_api.WorkFlowApi(api_client)
    create_workflow_request = CreateWorkflowRequest(
        additional_data_field="",
        auto_expire_field=AutoExpire(0),
        auto_remind_field=AutoRemind(0),
        doc_field="String content",
        doc_name_field="String content",
        due_date_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
        extension_field=DocExtension(0),
        message_field="String content",
        priority_field=Priority(0),
        sla_field=0,
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # CreateWorkflowRequest | ##### Create Workflow Request Model

    # example passing only required values which don't have defaults set
    try:
        # Create Workflow
        api_response = api_instance.create_workflow(create_workflow_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->create_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workflow_request** | [**CreateWorkflowRequest**](CreateWorkflowRequest.md)| ##### Create Workflow Request Model |
 **content_type** | **str**|  | defaults to "application/json"

### Return type

[**CreateWorkflowResponse**](CreateWorkflowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Create Workflow Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> GetDocumentResponse get_document()

Get Document

#### Used to download a document from SigniFlow.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import work_flow_api
from SigniFlowconnect.model.get_document_response import GetDocumentResponse
from SigniFlowconnect.model.get_document_request import GetDocumentRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = work_flow_api.WorkFlowApi(api_client)
    get_document_request = GetDocumentRequest(
        doc_id_field=2147483647,
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # GetDocumentRequest | ##### Get Document Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Document
        api_response = api_instance.get_document()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->get_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Document
        api_response = api_instance.get_document(get_document_request=get_document_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->get_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **get_document_request** | [**GetDocumentRequest**](GetDocumentRequest.md)| ##### Get Document Request Model | [optional]

### Return type

[**GetDocumentResponse**](GetDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Get Document Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_add_workflow_step**
> AddWokflowStepV2Response post_add_workflow_step()

Add a Workflow step

#### Used to add a step to a document Workflow process.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import work_flow_api
from SigniFlowconnect.model.add_wokflow_step_v2_response import AddWokflowStepV2Response
from SigniFlowconnect.model.add_workflow_step_v2_request import AddWorkflowStepV2Request
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = work_flow_api.WorkFlowApi(api_client)
    add_workflow_step_v2_request = AddWorkflowStepV2Request(
        action_field=ActionField(0),
        cell_field="cell_field_example",
        doc_id_field="2147483647",
        email_field="email@domain.com",
        first_name_field="John",
        language_code_field="ENG",
        last_name_field="Smith",
        proxy_allowed_field=ProxyAllowedField(0),
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # AddWorkflowStepV2Request | ##### Add A Workflow Step Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a Workflow step
        api_response = api_instance.post_add_workflow_step()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_add_workflow_step: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a Workflow step
        api_response = api_instance.post_add_workflow_step(add_workflow_step_v2_request=add_workflow_step_v2_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_add_workflow_step: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **add_workflow_step_v2_request** | [**AddWorkflowStepV2Request**](AddWorkflowStepV2Request.md)| ##### Add A Workflow Step Request Model | [optional]

### Return type

[**AddWokflowStepV2Response**](AddWokflowStepV2Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Add A Workflow Step Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cancel_flow**
> CancelFlowResponse post_cancel_flow()

Cancel Flow

#### Used to cancel a document workflow.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import work_flow_api
from SigniFlowconnect.model.cancel_flow_response import CancelFlowResponse
from SigniFlowconnect.model.cancel_flow_request import CancelFlowRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = work_flow_api.WorkFlowApi(api_client)
    cancel_flow_request = CancelFlowRequest(
        doc_id_field="2147483647",
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # CancelFlowRequest | ##### Cancel Flow Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Cancel Flow
        api_response = api_instance.post_cancel_flow()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_cancel_flow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Cancel Flow
        api_response = api_instance.post_cancel_flow(cancel_flow_request=cancel_flow_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_cancel_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **cancel_flow_request** | [**CancelFlowRequest**](CancelFlowRequest.md)| ##### Cancel Flow Request Model | [optional]

### Return type

[**CancelFlowResponse**](CancelFlowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Cancel Flow Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_delete_doc**
> DeleteDocResponse post_delete_doc()

Delete Document

#### This is used to delete a document.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import work_flow_api
from SigniFlowconnect.model.delete_doc_response import DeleteDocResponse
from SigniFlowconnect.model.delete_doc_request import DeleteDocRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = work_flow_api.WorkFlowApi(api_client)
    delete_doc_request = DeleteDocRequest(
        doc_id_field=2147483647,
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # DeleteDocRequest | ##### Delete Document Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Document
        api_response = api_instance.post_delete_doc()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_delete_doc: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Document
        api_response = api_instance.post_delete_doc(delete_doc_request=delete_doc_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_delete_doc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **delete_doc_request** | [**DeleteDocRequest**](DeleteDocRequest.md)| ##### Delete Document Request Model | [optional]

### Return type

[**DeleteDocResponse**](DeleteDocResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Delete Document Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_doc_prepper_add_field**
> DocPrepperAddFieldsFlowIDResponse post_doc_prepper_add_field()

Document Prepper Add Fields

#### Used to add fields to a document using the user's FlowID.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import work_flow_api
from SigniFlowconnect.model.doc_prepper_add_fields_flow_id_request import DocPrepperAddFieldsFlowIDRequest
from SigniFlowconnect.model.doc_prepper_add_fields_flow_id_response import DocPrepperAddFieldsFlowIDResponse
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = work_flow_api.WorkFlowApi(api_client)
    doc_prepper_add_fields_flow_id_request = DocPrepperAddFieldsFlowIDRequest(
        doc_field_type_field=FieldType(0),
        doc_id_field=12344,
        flow_id_field=11111,
        height_field="25",
        width_field="20",
        is_invisible_field=True,
        link_to_field="link_to_field_example",
        page_number_field=2,
        name_field="name_field_example",
        user_email_field="email@domain.com",
        x_coordinate_field="50",
        y_coordinate_field="150",
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # DocPrepperAddFieldsFlowIDRequest | ##### Document Prepper Add Fields Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Document Prepper Add Fields
        api_response = api_instance.post_doc_prepper_add_field()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_doc_prepper_add_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Document Prepper Add Fields
        api_response = api_instance.post_doc_prepper_add_field(doc_prepper_add_fields_flow_id_request=doc_prepper_add_fields_flow_id_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_doc_prepper_add_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **doc_prepper_add_fields_flow_id_request** | [**DocPrepperAddFieldsFlowIDRequest**](DocPrepperAddFieldsFlowIDRequest.md)| ##### Document Prepper Add Fields Request Model | [optional]

### Return type

[**DocPrepperAddFieldsFlowIDResponse**](DocPrepperAddFieldsFlowIDResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Document Prepper Add Fields Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_doc_prepper_advanced_fields**
> DocPrepperAddAdvancedFieldsResponse post_doc_prepper_advanced_fields()

Document Prepper Add Advanced Fields

#### Used to add advanced fields to a document.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import work_flow_api
from SigniFlowconnect.model.doc_prepper_add_advanced_fields_response import DocPrepperAddAdvancedFieldsResponse
from SigniFlowconnect.model.doc_prepper_add_advanced_fields_request import DocPrepperAddAdvancedFieldsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = work_flow_api.WorkFlowApi(api_client)
    doc_prepper_add_advanced_fields_request = DocPrepperAddAdvancedFieldsRequest(
        field_info_list_field=[
            DocPrepperAddAdvancedFieldsRequestFieldInfoListField(
                advanced_field_type_field=AdvancedFieldType(0),
                doc_id_field=2147483647,
                field_options_list_field=[
                    DocPrepperAddAdvancedFieldsRequestFieldOptionsListField(
                        linked_value_field="linked_value_field_example",
                        max_field=5,
                        min_field=2,
                        value_field="value_field_example",
                    ),
                ],
                flow_id_field=11111,
                font_family_field="Arial",
                font_size_field=12,
                height_field="30",
                width_field="15",
                link_to_field="link_to_field_example",
                name_field="Text Field",
                page_number_field=2,
                searchable_field=True,
                user_email_field="John@domain.com",
                value_field="value_field_example",
                x_coordinate_field="60",
                y_coordinate_field="120",
            ),
        ],
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # DocPrepperAddAdvancedFieldsRequest | ##### Document Prepper Add Advanced Fields Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Document Prepper Add Advanced Fields
        api_response = api_instance.post_doc_prepper_advanced_fields()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_doc_prepper_advanced_fields: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Document Prepper Add Advanced Fields
        api_response = api_instance.post_doc_prepper_advanced_fields(doc_prepper_add_advanced_fields_request=doc_prepper_add_advanced_fields_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_doc_prepper_advanced_fields: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **doc_prepper_add_advanced_fields_request** | [**DocPrepperAddAdvancedFieldsRequest**](DocPrepperAddAdvancedFieldsRequest.md)| ##### Document Prepper Add Advanced Fields Request Model | [optional]

### Return type

[**DocPrepperAddAdvancedFieldsResponse**](DocPrepperAddAdvancedFieldsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Document Prepper Add Advanced Fields Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_full_workflow**
> FullWorkflowResponse post_full_workflow()

FullWorkflow

#### Used to create a fullworkflow for a document.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import work_flow_api
from SigniFlowconnect.model.full_workflow_request import FullWorkflowRequest
from SigniFlowconnect.model.full_workflow_response import FullWorkflowResponse
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = work_flow_api.WorkFlowApi(api_client)
    full_workflow_request = FullWorkflowRequest(
        additional_data_field="additional_data_field_example",
        auto_remind_field=AutoRemind(0),
        custom_message_field="A message with things.",
        doc_field="doc_field_example",
        doc_name_field="Document 1",
        due_date_field="02/02/2021",
        extension_field=DocExtension(0),
        flatten_document_field=True,
        keep_content_security_field=True,
        keep_custom_properties_field=True,
        keep_xmp_metadata_field=True,
        portfolio_information_field=FullWorkflowRequestPortfolioInformationField(
            create_portfolio_field=True,
            link_to_portfolio_field=True,
            portfolio_id_field=11112,
            portfolio_name_field="Portfolio 1",
        ),
        priority_field=3.14,
        sla_field=3.14,
        send_first_email_field=True,
        send_workflow_emails_field=True,
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
        workflow_users_list_field=[
            FullWorkflowRequestWorkflowUsersListField(
                action_field=3.14,
                allow_proxy_field=3.14,
                auto_sign_field=True,
                email_address_field="email@domain.com",
                group_step_field=FullWorkflowRequestGroupStepField(
                    group_members_field=[
                        FullWorkflowRequestGroupStepFieldGroupMembersField(
                            language_code_field="language_code_field_example",
                            user_email_field="user_email_field_example",
                            user_full_name_field="user_full_name_field_example",
                            user_mobile_number_field="user_mobile_number_field_example",
                        ),
                    ],
                    group_name_field="Managers",
                    required_number_of_signatures_field=3,
                ),
                language_code_field="ENG",
                latitude_field="latitude_field_example",
                longitude_field="longitude_field_example",
                mobile_number_field="078 222 2222",
                preloaded_face_to_face_signers_field=[
                    {},
                ],
                sign_reason_field="Because yes",
                signer_password_field="P@ssw0rd",
                user_first_name_field="John",
                user_full_name_field="John Smith",
                user_last_name_field="Smith",
                workflow_user_fields_field=[
                    FullWorkflowRequestWorkflowUserFieldsField(
                        field_type_field=7,
                        font_family_field="Arial",
                        font_size_field=15,
                        group_user_number_field=5,
                        height_field="15",
                        is_invisible_field=True,
                        page_number_field=2,
                        tag_name_field="tag_name_field_example",
                        value_field="value_field_example",
                        width_field="25",
                        x_coordinate_field="60",
                        x_offset_field=15,
                        y_coordinate_field="150",
                        y_offset_field=20,
                    ),
                ],
            ),
        ],
    ) # FullWorkflowRequest | ##### FullWorkflow Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # FullWorkflow
        api_response = api_instance.post_full_workflow()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_full_workflow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # FullWorkflow
        api_response = api_instance.post_full_workflow(full_workflow_request=full_workflow_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_full_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **full_workflow_request** | [**FullWorkflowRequest**](FullWorkflowRequest.md)| ##### FullWorkflow Request Model | [optional]

### Return type

[**FullWorkflowResponse**](FullWorkflowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### FullWorkflow Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_doc_status**
> GetDocStatusResponse post_get_doc_status()

Get Document Status

#### Used to get the status of the document ex. pending/completed/rejected.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import work_flow_api
from SigniFlowconnect.model.get_doc_status_response import GetDocStatusResponse
from SigniFlowconnect.model.get_doc_status_request import GetDocStatusRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = work_flow_api.WorkFlowApi(api_client)
    get_doc_status_request = GetDocStatusRequest(
        doc_id_field=3.14,
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # GetDocStatusRequest | ##### Get Document Status Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Document Status
        api_response = api_instance.post_get_doc_status()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_get_doc_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Document Status
        api_response = api_instance.post_get_doc_status(get_doc_status_request=get_doc_status_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_get_doc_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **get_doc_status_request** | [**GetDocStatusRequest**](GetDocStatusRequest.md)| ##### Get Document Status Request Model | [optional]

### Return type

[**GetDocStatusResponse**](GetDocStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Get Document Status Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_initiate_flow**
> InitiateFlowResponse post_initiate_flow()

Initiate Flow

#### Used to initiate aworkflow of a document.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import work_flow_api
from SigniFlowconnect.model.initiate_flow_request import InitiateFlowRequest
from SigniFlowconnect.model.initiate_flow_response import InitiateFlowResponse
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = work_flow_api.WorkFlowApi(api_client)
    initiate_flow_request = InitiateFlowRequest(
        doc_id_field="doc_id_field_example",
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # InitiateFlowRequest | ##### Initiate Flow Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Initiate Flow
        api_response = api_instance.post_initiate_flow()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_initiate_flow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initiate Flow
        api_response = api_instance.post_initiate_flow(initiate_flow_request=initiate_flow_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_initiate_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **initiate_flow_request** | [**InitiateFlowRequest**](InitiateFlowRequest.md)| ##### Initiate Flow Request Model | [optional]

### Return type

[**InitiateFlowResponse**](InitiateFlowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Initiate Flow Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_initiate_flow_no_email**
> InitiateFlowNoEmailResponse post_initiate_flow_no_email()

Initiate Flow No Email

#### Used to initiate a workflow without sending out emails.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import work_flow_api
from SigniFlowconnect.model.initiate_flow_no_email_response import InitiateFlowNoEmailResponse
from SigniFlowconnect.model.initiate_flow_no_email_request import InitiateFlowNoEmailRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = work_flow_api.WorkFlowApi(api_client)
    initiate_flow_no_email_request = InitiateFlowNoEmailRequest(
        doc_id_field="doc_id_field_example",
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # InitiateFlowNoEmailRequest | ##### Initiate Flow No Email Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Initiate Flow No Email
        api_response = api_instance.post_initiate_flow_no_email()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_initiate_flow_no_email: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initiate Flow No Email
        api_response = api_instance.post_initiate_flow_no_email(initiate_flow_no_email_request=initiate_flow_no_email_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_initiate_flow_no_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **initiate_flow_no_email_request** | [**InitiateFlowNoEmailRequest**](InitiateFlowNoEmailRequest.md)| ##### Initiate Flow No Email Request Model | [optional]

### Return type

[**InitiateFlowNoEmailResponse**](InitiateFlowNoEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Initiate Flow No Email Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_initiate_flow_no_initial_email**
> InitiateFlowNoInitialEmailResponse post_initiate_flow_no_initial_email()

Initiate Flow No Initial Email

#### Used to initiate a document workflow without an initial email being sent to the user.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import work_flow_api
from SigniFlowconnect.model.initiate_flow_no_initial_email_request import InitiateFlowNoInitialEmailRequest
from SigniFlowconnect.model.initiate_flow_no_initial_email_response import InitiateFlowNoInitialEmailResponse
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = work_flow_api.WorkFlowApi(api_client)
    initiate_flow_no_initial_email_request = InitiateFlowNoInitialEmailRequest(
        doc_id_field="doc_id_field_example",
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # InitiateFlowNoInitialEmailRequest | ##### Initiate Flow No Initial Email Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Initiate Flow No Initial Email
        api_response = api_instance.post_initiate_flow_no_initial_email()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_initiate_flow_no_initial_email: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initiate Flow No Initial Email
        api_response = api_instance.post_initiate_flow_no_initial_email(initiate_flow_no_initial_email_request=initiate_flow_no_initial_email_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_initiate_flow_no_initial_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **initiate_flow_no_initial_email_request** | [**InitiateFlowNoInitialEmailRequest**](InitiateFlowNoInitialEmailRequest.md)| ##### Initiate Flow No Initial Email Request Model | [optional]

### Return type

[**InitiateFlowNoInitialEmailResponse**](InitiateFlowNoInitialEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Initiate Flow No Initial Email Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_workflow_sign**
> WorkflowSignResponse post_workflow_sign()

Workflow Sign

#### Used to send a request to a user to sign a document workflow.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import work_flow_api
from SigniFlowconnect.model.workflow_sign_request import WorkflowSignRequest
from SigniFlowconnect.model.workflow_sign_response import WorkflowSignResponse
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = work_flow_api.WorkFlowApi(api_client)
    workflow_sign_request = WorkflowSignRequest(
        doc_id_field="doc_id_field_example",
        latitude_field="latitude_field_example",
        login_password_field="login_password_field_example",
        login_user_name_field="email@domain.com",
        longitude_field="longitude_field_example",
        sign_reason_field="sign_reason_field_example",
        time_zone_offset_field=3.14,
        token_field=TokenField(
            token_expiry_field=dateutil_parser('1970-01-01T00:00:00.00Z'),
            token_field="aaa111",
        ),
    ) # WorkflowSignRequest | ##### Workflow Sign Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Workflow Sign
        api_response = api_instance.post_workflow_sign()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_workflow_sign: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Workflow Sign
        api_response = api_instance.post_workflow_sign(workflow_sign_request=workflow_sign_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling WorkFlowApi->post_workflow_sign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **workflow_sign_request** | [**WorkflowSignRequest**](WorkflowSignRequest.md)| ##### Workflow Sign Request Model | [optional]

### Return type

[**WorkflowSignResponse**](WorkflowSignResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Workflow Sign Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

