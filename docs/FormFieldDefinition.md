# FormFieldDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **str** | The identifier of the field; use this to identify which field is being referenced | [optional] 
**left_anchor** | **str** | Optional - the left-hand anchor of the field | [optional] 
**top_anchor** | **str** | Optional - the top anchor of the field | [optional] 
**anchor_mode** | **str** | Optional - the matching mode for the anchor.  Possible values are Complete (requires the entire anchor to match) and Partial (allows only part of the anchor to match).  Default is Partial. | [optional] 
**data_type** | **str** | The data type of the field; possible values are INTEGER (Integer value), STRING (Arbitrary string value, spaces are permitted), DATE (Date in a structured format), DECIMAL (Decimal number), ALPHANUMERIC (Continuous alphanumeric string with no spaces), STRINGNOWHITESPACE (A string that contains no whitespace characters), SERIALNUMBER (A serial-number style string that contains letters and numbers, and certain symbols; must contain at least one number), ALPHAONLY (Alphabet characters only, no numbers or symbols or whitespace) | [optional] 
**target_digit_count** | **int** | Optional - the target number of digits in the field; useful for fixed-length fields | [optional] 
**minimum_character_count** | **int** | Optional - the target number of digits in the field; useful for fixed-length fields | [optional] 
**allow_numeric_digits** | **bool** | Optional - set to false to block values that contain numeric digits, set to true to allow numeric digits | [optional] 
**vertical_alignment_type** | **str** | Vertical alignment of target value area relative to the field anchor; Possible values are VCenter, Top, Bottom | [optional] 
**horizontal_alignment_type** | **str** | Horizontal alignment of target value area relative to the field anchor; Possible values are Left, Right | [optional] 
**target_field_width_relative** | **float** | Optional - scale factor for target field width - relative to width of field title; a value of 1.0 indicates the target value area has the same width as the field value as occurring in the image; a value of 2.0 would indicate that the target value area has 2 times the width of the field value as occurring in the image. | [optional] 
**target_field_height_relative** | **float** | Optional - scale factor for target field height - relative to height of field title | [optional] 
**ignore** | **list[str]** | Optional - Ignore any result items that contain a partial or complete match with these text strings | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


