# cloudmersive_ocr_api_client.ReceiptsApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**receipts_photo_to_csv**](ReceiptsApi.md#receipts_photo_to_csv) | **POST** /ocr/receipts/photo/to/csv | Convert a photo of a receipt into a CSV file containing structured information from the receipt


# **receipts_photo_to_csv**
> object receipts_photo_to_csv(image_file)

Convert a photo of a receipt into a CSV file containing structured information from the receipt

Leverage Deep Learning to automatically turn a photo of a receipt into a CSV file containing the structured information from the receipt.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_ocr_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_ocr_api_client.ReceiptsApi(cloudmersive_ocr_api_client.ApiClient(configuration))
image_file = '/path/to/file.txt' # file | Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported.

try:
    # Convert a photo of a receipt into a CSV file containing structured information from the receipt
    api_response = api_instance.receipts_photo_to_csv(image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->receipts_photo_to_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **file**| Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

