# FullWorkflowRequestWorkflowUsersListField


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_field** | **float** | Refers to the order of signatures from the users. | 
**allow_proxy_field** | **float** | Allow proxy confirmation field. | 
**auto_sign_field** | **bool** | ### Enable auto sign.  &#x60;True &#x3D; Signature will be applied automaticly False &#x3D; User will need to login and Sign&#x60;  | 
**email_address_field** | **str** | Workflow user&#39;s email addresses. | 
**language_code_field** | **str** | #### Sets the display language for the user ##### ISO 2 Digit Code  &#x60;en &#x3D; English es &#x3D; Spanish fr &#x3D; French&#x60;  | 
**latitude_field** | **str** | Location latitude. | 
**longitude_field** | **str** | Location longtitude. | 
**mobile_number_field** | **str** | Group user&#39;s mobile number. | 
**sign_reason_field** | **str** | Reason for signature. | 
**signer_password_field** | **str** | Face to face user&#39;s password. | 
**user_first_name_field** | **str** | Face to face user&#39;s first name. | 
**user_full_name_field** | **str** | Face to face user&#39;s full name. | 
**user_last_name_field** | **str** | Face to face user&#39;s last name. | 
**group_step_field** | [**FullWorkflowRequestGroupStepField**](FullWorkflowRequestGroupStepField.md) |  | [optional] 
**preloaded_face_to_face_signers_field** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | Preloaded user&#39;s who will be using the face to face signature field. | [optional] 
**workflow_user_fields_field** | [**[FullWorkflowRequestWorkflowUserFieldsField]**](FullWorkflowRequestWorkflowUserFieldsField.md) | The list of the workflowed documents field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


