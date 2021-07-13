# SigniFlowconnect.SigningCeremonyApi

All URIs are relative to *https://server-url/API/SignFlowAPIServiceRest.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_multiple_signers_signing_ceremony**](SigningCeremonyApi.md#post_multiple_signers_signing_ceremony) | **POST** /MultipleSignersSigningCeremony | Multiple Signers Signing Ceremony
[**post_signing_ceremony_v2**](SigningCeremonyApi.md#post_signing_ceremony_v2) | **POST** /SigningCeremonyV2 | Signing Ceremony V2


# **post_multiple_signers_signing_ceremony**
> MultipleSignersSigningCeremonyResponse post_multiple_signers_signing_ceremony()

Multiple Signers Signing Ceremony

#### Used when there are multiple signers on a document.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import signing_ceremony_api
from SigniFlowconnect.model.multiple_signers_signing_ceremony_response import MultipleSignersSigningCeremonyResponse
from SigniFlowconnect.model.multiple_signers_signing_ceremony_request import MultipleSignersSigningCeremonyRequest
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = signing_ceremony_api.SigningCeremonyApi(api_client)
    multiple_signers_signing_ceremony_request = MultipleSignersSigningCeremonyRequest(
        doc_field="doc_field_example",
        doc_name_field="doc_name_field_example",
        login_password_field="12345",
        login_user_name_field="John@gmail.com",
        signer_list_field=[
            MultipleSignersSigningCeremonyRequestSignerListField(
                signature_h_field=3.14,
                signature_image_field="signature_image_field_example",
                signature_image_include_border_field=True,
                signature_image_include_reason_field=True,
                signature_image_include_signed_by_field=True,
                signature_image_include_signed_date_field=True,
                signature_image_type_field=3.14,
                signature_page_field=3.14,
                signature_w_field=3.14,
                signature_x_field=3.14,
                signature_y_field=3.14,
                signer_email_field="signer_email_field_example",
                signer_full_name_field="signer_full_name_field_example",
                signer_indentification_number_field="signer_indentification_number_field_example",
                signer_location_field="signer_location_field_example",
                signer_mobile_number_field="signer_mobile_number_field_example",
                signer_reason_field="signer_reason_field_example",
                signer_trust_origin_field="signer_trust_origin_field_example",
                signer_trust_reference_field="signer_trust_reference_field_example",
            ),
        ],
    ) # MultipleSignersSigningCeremonyRequest | ##### Multiple Signers Signing Ceremony Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Multiple Signers Signing Ceremony
        api_response = api_instance.post_multiple_signers_signing_ceremony()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling SigningCeremonyApi->post_multiple_signers_signing_ceremony: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Multiple Signers Signing Ceremony
        api_response = api_instance.post_multiple_signers_signing_ceremony(multiple_signers_signing_ceremony_request=multiple_signers_signing_ceremony_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling SigningCeremonyApi->post_multiple_signers_signing_ceremony: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **multiple_signers_signing_ceremony_request** | [**MultipleSignersSigningCeremonyRequest**](MultipleSignersSigningCeremonyRequest.md)| ##### Multiple Signers Signing Ceremony Request Model | [optional]

### Return type

[**MultipleSignersSigningCeremonyResponse**](MultipleSignersSigningCeremonyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Multiple Signers Signing Ceremony Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_signing_ceremony_v2**
> SigningCeremonyV2Response post_signing_ceremony_v2()

Signing Ceremony V2

#### Used to initiate the signing process of a document.

### Example

```python
import time
import SigniFlowconnect
from SigniFlowconnect.api import signing_ceremony_api
from SigniFlowconnect.model.signing_ceremony_v2_request import SigningCeremonyV2Request
from SigniFlowconnect.model.signing_ceremony_v2_response import SigningCeremonyV2Response
from pprint import pprint
# Defining the host is optional and defaults to https://server-url/API/SignFlowAPIServiceRest.svc
# See configuration.py for a list of all supported configuration parameters.
configuration = SigniFlowconnect.Configuration(
    host = "https://server-url/API/SignFlowAPIServiceRest.svc"
)


# Enter a context with an instance of the API client
with SigniFlowconnect.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = signing_ceremony_api.SigningCeremonyApi(api_client)
    signing_ceremony_v2_request = SigningCeremonyV2Request(
        checkbox_fields_list_field=[
            {
                checkbox_h_field=3.14,
                checkbox_page_field=3.14,
                checkbox_w_field=3.14,
                checkbox_x_field=3.14,
                checkbox_y_field=3.14,
                is_checked_field=True,
            },
        ],
        doc_field="doc_field_example",
        doc_name_field="doc_name_field_example",
        initial_fields_list_field=[
            {
                initial_h_field=3.14,
                initial_image_field="initial_image_field_example",
                initial_image_type_field=3.14,
                initial_page_field=3.14,
                initial_w_field=3.14,
                initial_x_field=3.14,
                initial_y_field=3.14,
            },
        ],
        login_password_field="login_password_field_example",
        login_user_name_field="login_user_name_field_example",
        signature_h_field=3.14,
        signature_image_field="signature_image_field_example",
        signature_image_include_border_field=True,
        signature_image_include_reason_field=True,
        signature_image_include_signed_by_field=True,
        signature_image_include_signed_date_field=True,
        signature_image_type_field=3.14,
        signature_page_field=3.14,
        signature_w_field=3.14,
        signature_x_field=3.14,
        signature_y_field=3.14,
        signer_email_field="signer_email_field_example",
        signer_full_name_field="signer_full_name_field_example",
        signer_identification_number_field="signer_identification_number_field_example",
        signer_location_field="signer_location_field_example",
        signer_mobile_number_field="signer_mobile_number_field_example",
        signer_reason_field="signer_reason_field_example",
        signer_trust_origin_field="signer_trust_origin_field_example",
        signer_trust_reference_field="signer_trust_reference_field_example",
        text_fields_list_field=[
            {
                text_field_h_field=3.14,
                text_field_page_field=3.14,
                text_field_value_field="text_field_value_field_example",
                text_field_w_field=3.14,
                text_field_x_field=3.14,
                text_field_y_field=3.14,
            },
        ],
    ) # SigningCeremonyV2Request | ##### Signing Ceremony V2 Request Model (optional)

    # example passing only required values which don't have defaults set
    try:
        # Signing Ceremony V2
        api_response = api_instance.post_signing_ceremony_v2()
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling SigningCeremonyApi->post_signing_ceremony_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Signing Ceremony V2
        api_response = api_instance.post_signing_ceremony_v2(signing_ceremony_v2_request=signing_ceremony_v2_request)
        pprint(api_response)
    except SigniFlowconnect.ApiException as e:
        print("Exception when calling SigningCeremonyApi->post_signing_ceremony_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/json"
 **signing_ceremony_v2_request** | [**SigningCeremonyV2Request**](SigningCeremonyV2Request.md)| ##### Signing Ceremony V2 Request Model | [optional]

### Return type

[**SigningCeremonyV2Response**](SigningCeremonyV2Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ##### Signing Ceremony V2 Response Model |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

