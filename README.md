# cloudmersive_ocr_api_client
The powerful Optical Character Recognition (OCR) APIs let you convert scanned images of pages into recognized text.

This Python package provides a native API client for [Cloudmersive OCR](https://www.cloudmersive.com/ocr-api)

- API version: v1
- Package version: 4.0.1
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cloudmersive_ocr_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudmersive_ocr_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
language = 'language_example' # str | Optional, language of the input document, default is English (ENG).  Possible values are ENG (English), ARA (Arabic), ZHO (Chinese - Simplified), ZHO-HANT (Chinese - Traditional), ASM (Assamese), AFR (Afrikaans), AMH (Amharic), AZE (Azerbaijani), AZE-CYRL (Azerbaijani - Cyrillic), BEL (Belarusian), BEN (Bengali), BOD (Tibetan), BOS (Bosnian), BUL (Bulgarian), CAT (Catalan; Valencian), CEB (Cebuano), CES (Czech), CHR (Cherokee), CYM (Welsh), DAN (Danish), DEU (German), DZO (Dzongkha), ELL (Greek), ENM (Archaic/Middle English), EPO (Esperanto), EST (Estonian), EUS (Basque), FAS (Persian), FIN (Finnish), FRA (French), FRK (Frankish), FRM (Middle-French), GLE (Irish), GLG (Galician), GRC (Ancient Greek), HAT (Hatian), HEB (Hebrew), HIN (Hindi), HRV (Croatian), HUN (Hungarian), IKU (Inuktitut), IND (Indonesian), ISL (Icelandic), ITA (Italian), ITA-OLD (Old - Italian), JAV (Javanese), JPN (Japanese), KAN (Kannada), KAT (Georgian), KAT-OLD (Old-Georgian), KAZ (Kazakh), KHM (Central Khmer), KIR (Kirghiz), KOR (Korean), KUR (Kurdish), LAO (Lao), LAT (Latin), LAV (Latvian), LIT (Lithuanian), MAL (Malayalam), MAR (Marathi), MKD (Macedonian), MLT (Maltese), MSA (Malay), MYA (Burmese), NEP (Nepali), NLD (Dutch), NOR (Norwegian), ORI (Oriya), PAN (Panjabi), POL (Polish), POR (Portuguese), PUS (Pushto), RON (Romanian), RUS (Russian), SAN (Sanskrit), SIN (Sinhala), SLK (Slovak), SLV (Slovenian), SPA (Spanish), SPA-OLD (Old Spanish), SQI (Albanian), SRP (Serbian), SRP-LAT (Latin Serbian), SWA (Swahili), SWE (Swedish), SYR (Syriac), TAM (Tamil), TEL (Telugu), TGK (Tajik), TGL (Tagalog), THA (Thai), TIR (Tigrinya), TUR (Turkish), UIG (Uighur), UKR (Ukrainian), URD (Urdu), UZB (Uzbek), UZB-CYR (Cyrillic Uzbek), VIE (Vietnamese), YID (Yiddish) (optional)
preprocessing = 'preprocessing_example' # str | Optional, preprocessing mode, default is 'Auto'.  Possible values are None (no preprocessing of the image), and Auto (automatic image enhancement of the image before OCR is applied; this is recommended). (optional)

try:
    # Convert a scanned image into words with location
    api_response = api_instance.image_ocr_image_lines_with_location(image_file, language=language, preprocessing=preprocessing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOcrApi->image_ocr_image_lines_with_location: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ImageOcrApi* | [**image_ocr_image_lines_with_location**](docs/ImageOcrApi.md#image_ocr_image_lines_with_location) | **POST** /ocr/image/to/lines-with-location | Convert a scanned image into words with location
*ImageOcrApi* | [**image_ocr_image_words_with_location**](docs/ImageOcrApi.md#image_ocr_image_words_with_location) | **POST** /ocr/image/to/words-with-location | Convert a scanned image into words with location
*ImageOcrApi* | [**image_ocr_photo_recognize_business_card**](docs/ImageOcrApi.md#image_ocr_photo_recognize_business_card) | **POST** /ocr/photo/recognize/business-card | Recognize a photo of a business card, extract key business information
*ImageOcrApi* | [**image_ocr_photo_recognize_form**](docs/ImageOcrApi.md#image_ocr_photo_recognize_form) | **POST** /ocr/photo/recognize/form | Recognize a photo of a form, extract key fields and business information
*ImageOcrApi* | [**image_ocr_photo_recognize_form_advanced**](docs/ImageOcrApi.md#image_ocr_photo_recognize_form_advanced) | **POST** /ocr/photo/recognize/form/advanced | Recognize a photo of a form, extract key fields using stored templates
*ImageOcrApi* | [**image_ocr_photo_recognize_receipt**](docs/ImageOcrApi.md#image_ocr_photo_recognize_receipt) | **POST** /ocr/photo/recognize/receipt | Recognize a photo of a receipt, extract key business information
*ImageOcrApi* | [**image_ocr_photo_to_text**](docs/ImageOcrApi.md#image_ocr_photo_to_text) | **POST** /ocr/photo/toText | Convert a photo of a document into text
*ImageOcrApi* | [**image_ocr_photo_words_with_location**](docs/ImageOcrApi.md#image_ocr_photo_words_with_location) | **POST** /ocr/photo/to/words-with-location | Convert a photo of a document or receipt into words with location
*ImageOcrApi* | [**image_ocr_post**](docs/ImageOcrApi.md#image_ocr_post) | **POST** /ocr/image/toText | Convert a scanned image into text
*PdfOcrApi* | [**pdf_ocr_get_async_job_status**](docs/PdfOcrApi.md#pdf_ocr_get_async_job_status) | **GET** /ocr/pdf/get-job-status | Returns the result of the Async Job - possible states can be STARTED or COMPLETED
*PdfOcrApi* | [**pdf_ocr_pdf_to_lines_with_location**](docs/PdfOcrApi.md#pdf_ocr_pdf_to_lines_with_location) | **POST** /ocr/pdf/to/lines-with-location | Convert a PDF into text lines with location
*PdfOcrApi* | [**pdf_ocr_pdf_to_words_with_location**](docs/PdfOcrApi.md#pdf_ocr_pdf_to_words_with_location) | **POST** /ocr/pdf/to/words-with-location | Convert a PDF into words with location
*PdfOcrApi* | [**pdf_ocr_post**](docs/PdfOcrApi.md#pdf_ocr_post) | **POST** /ocr/pdf/toText | Converts an uploaded PDF file into text via Optical Character Recognition.
*PreprocessingApi* | [**preprocessing_binarize**](docs/PreprocessingApi.md#preprocessing_binarize) | **POST** /ocr/preprocessing/image/binarize | Convert an image of text into a binarized (light and dark) view
*PreprocessingApi* | [**preprocessing_binarize_advanced**](docs/PreprocessingApi.md#preprocessing_binarize_advanced) | **POST** /ocr/preprocessing/image/binarize/advanced | Convert an image of text into a binary (light and dark) view with ML
*PreprocessingApi* | [**preprocessing_get_page_angle**](docs/PreprocessingApi.md#preprocessing_get_page_angle) | **POST** /ocr/preprocessing/image/get-page-angle | Get the angle of the page / document / receipt
*PreprocessingApi* | [**preprocessing_unrotate**](docs/PreprocessingApi.md#preprocessing_unrotate) | **POST** /ocr/preprocessing/image/unrotate | Detect and unrotate a document image
*PreprocessingApi* | [**preprocessing_unrotate_advanced**](docs/PreprocessingApi.md#preprocessing_unrotate_advanced) | **POST** /ocr/preprocessing/image/unrotate/advanced | Detect and unrotate a document image (advanced)
*PreprocessingApi* | [**preprocessing_unskew**](docs/PreprocessingApi.md#preprocessing_unskew) | **POST** /ocr/preprocessing/image/unskew | Detect and unskew a photo of a document
*ReceiptsApi* | [**receipts_photo_to_csv**](docs/ReceiptsApi.md#receipts_photo_to_csv) | **POST** /ocr/receipts/photo/to/csv | Convert a photo of a receipt into a CSV file containing structured information from the receipt


## Documentation For Models

 - [BusinessCardRecognitionResult](docs/BusinessCardRecognitionResult.md)
 - [FieldResult](docs/FieldResult.md)
 - [FormDefinitionTemplate](docs/FormDefinitionTemplate.md)
 - [FormFieldDefinition](docs/FormFieldDefinition.md)
 - [FormRecognitionResult](docs/FormRecognitionResult.md)
 - [FormTableColumnDefinition](docs/FormTableColumnDefinition.md)
 - [FormTableDefinition](docs/FormTableDefinition.md)
 - [GetPageAngleResult](docs/GetPageAngleResult.md)
 - [ImageToLinesWithLocationResult](docs/ImageToLinesWithLocationResult.md)
 - [ImageToTextResponse](docs/ImageToTextResponse.md)
 - [ImageToWordsWithLocationResult](docs/ImageToWordsWithLocationResult.md)
 - [OcrLineElement](docs/OcrLineElement.md)
 - [OcrPageResult](docs/OcrPageResult.md)
 - [OcrPageResultWithLinesWithLocation](docs/OcrPageResultWithLinesWithLocation.md)
 - [OcrPageResultWithWordsWithLocation](docs/OcrPageResultWithWordsWithLocation.md)
 - [OcrPhotoTextElement](docs/OcrPhotoTextElement.md)
 - [OcrWordElement](docs/OcrWordElement.md)
 - [PdfToLinesWithLocationResult](docs/PdfToLinesWithLocationResult.md)
 - [PdfToTextResponse](docs/PdfToTextResponse.md)
 - [PdfToWordsWithLocationResult](docs/PdfToWordsWithLocationResult.md)
 - [PhotoToWordsWithLocationResult](docs/PhotoToWordsWithLocationResult.md)
 - [Point](docs/Point.md)
 - [ReceiptLineItem](docs/ReceiptLineItem.md)
 - [ReceiptRecognitionResult](docs/ReceiptRecognitionResult.md)
 - [TableCellResult](docs/TableCellResult.md)
 - [TableResult](docs/TableResult.md)
 - [TableRowResult](docs/TableRowResult.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



