# ReceiptRecognitionResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | **bool** | True if the operation was successful, false otherwise | [optional] 
**timestamp** | **datetime** | The date and time printed on the receipt (if included on the receipt) | [optional] 
**business_name** | **str** | The name of the business printed on the receipt (if included on the receipt) | [optional] 
**business_website** | **str** | The website URL of the business printed on the receipt (if included on the receipt) | [optional] 
**address_string** | **str** | The address of the business printed on the receipt (if included on the receipt) | [optional] 
**phone_number** | **str** | The phone number printed on the receipt (if included on the receipt) | [optional] 
**receipt_items** | [**list[ReceiptLineItem]**](ReceiptLineItem.md) | The individual line items comprising the order; does not include total (see ReceiptTotal) | [optional] 
**receipt_sub_total** | **float** | Optional; if available, the monetary value of the receipt subtotal - typically not including specialized line items such as Tax. If this value is not available, it will be 0. | [optional] 
**receipt_total** | **float** | The total monetary value of the receipt (if included on the receipt) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


