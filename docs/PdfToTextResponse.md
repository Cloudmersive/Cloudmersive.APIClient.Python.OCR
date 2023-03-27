# PdfToTextResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | **bool** | True if successful, false otherwise | [optional] 
**ocr_pages** | [**list[OcrPageResult]**](OcrPageResult.md) | Page OCR results | [optional] 
**async_job_id** | **str** | When the job exceeds 25 pages, an Async Job ID is returned.  Use the CheckPdfOcrJobStatus API to check on the status of this job using the AsyncJobID and get the result when it finishes | [optional] 
**async_job_status** | **str** | Returns the job status of the Async Job, if applicable.  Possible states are STARTED and COMPLETED | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


