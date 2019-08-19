# coding: utf-8

"""
    ocrapi

    The powerful Optical Character Recognition (OCR) APIs let you convert scanned images of pages into recognized text.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cloudmersive_ocr_api_client.models.field_result import FieldResult  # noqa: F401,E501


class FormRecognitionResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'successful': 'bool',
        'field_value_extraction_result': 'list[FieldResult]'
    }

    attribute_map = {
        'successful': 'Successful',
        'field_value_extraction_result': 'FieldValueExtractionResult'
    }

    def __init__(self, successful=None, field_value_extraction_result=None):  # noqa: E501
        """FormRecognitionResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._field_value_extraction_result = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if field_value_extraction_result is not None:
            self.field_value_extraction_result = field_value_extraction_result

    @property
    def successful(self):
        """Gets the successful of this FormRecognitionResult.  # noqa: E501


        :return: The successful of this FormRecognitionResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this FormRecognitionResult.


        :param successful: The successful of this FormRecognitionResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def field_value_extraction_result(self):
        """Gets the field_value_extraction_result of this FormRecognitionResult.  # noqa: E501


        :return: The field_value_extraction_result of this FormRecognitionResult.  # noqa: E501
        :rtype: list[FieldResult]
        """
        return self._field_value_extraction_result

    @field_value_extraction_result.setter
    def field_value_extraction_result(self, field_value_extraction_result):
        """Sets the field_value_extraction_result of this FormRecognitionResult.


        :param field_value_extraction_result: The field_value_extraction_result of this FormRecognitionResult.  # noqa: E501
        :type: list[FieldResult]
        """

        self._field_value_extraction_result = field_value_extraction_result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FormRecognitionResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FormRecognitionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other