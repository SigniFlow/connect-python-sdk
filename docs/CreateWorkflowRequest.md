# CreateWorkflowRequest

#### The request sent to create a document workflow.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_data_field** | **str** | Sets additional data to be embedded in PDF Meta. | 
**auto_expire_field** | [**AutoExpire**](AutoExpire.md) |  | 
**auto_remind_field** | [**AutoRemind**](AutoRemind.md) |  | 
**doc_field** | **str** | Base64 Encoded String of document | 
**doc_name_field** | **str** | Name of document to display in SigniFlow | 
**extension_field** | [**DocExtension**](DocExtension.md) |  | 
**message_field** | **str** | Custom message to display to participants | 
**priority_field** | [**Priority**](Priority.md) |  | 
**token_field** | [**TokenField**](TokenField.md) |  | 
**sla_field** | **int** | Deprecated field, Pass 0 | defaults to 0
**due_date_field** | **datetime, none_type** | Due date for the document, use in conjunction with Auto Expire. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


