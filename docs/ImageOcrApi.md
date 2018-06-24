# cloudmersive_ocr_api_client.ImageOcrApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_ocr_post**](ImageOcrApi.md#image_ocr_post) | **POST** /ocr/image/toText | Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.


# **image_ocr_post**
> ImageToTextResponse image_ocr_post(image_file)

Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.

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
api_instance = cloudmersive_ocr_api_client.ImageOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration))
image_file = '/path/to/file.txt' # file | Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported.

try:
    # Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.
    api_response = api_instance.image_ocr_post(image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOcrApi->image_ocr_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **file**| Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

[**ImageToTextResponse**](ImageToTextResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

