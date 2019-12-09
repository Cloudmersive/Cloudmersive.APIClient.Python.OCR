# FormRecognitionResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | **bool** | True if the operation was successful, false otherwise | [optional] 
**field_value_extraction_result** | [**list[FieldResult]**](FieldResult.md) | Result of form field OCR data extraction | [optional] 
**table_value_extraction_results** | [**list[TableResult]**](TableResult.md) | Result of form table OCR data extraction | [optional] 
**diagnostics** | **list[str]** | Diagnostic images - default is null, enable diagnostics&#x3D;true to populate this parameter with one image per field | [optional] 
**best_match_form_setting_name** | **str** | Optional; populated when using photo/recognize/form/advanced with the Setting Name of the best-matching highest-relevance form | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


