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

from cloudmersive_ocr_api_client.models.ocr_page_result_with_words_with_location import OcrPageResultWithWordsWithLocation  # noqa: F401,E501


class PdfToWordsWithLocationResult(object):
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
        'ocr_pages': 'list[OcrPageResultWithWordsWithLocation]'
    }

    attribute_map = {
        'successful': 'Successful',
        'ocr_pages': 'OcrPages'
    }

    def __init__(self, successful=None, ocr_pages=None):  # noqa: E501
        """PdfToWordsWithLocationResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._ocr_pages = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if ocr_pages is not None:
            self.ocr_pages = ocr_pages

    @property
    def successful(self):
        """Gets the successful of this PdfToWordsWithLocationResult.  # noqa: E501

        True if successful, false otherwise  # noqa: E501

        :return: The successful of this PdfToWordsWithLocationResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this PdfToWordsWithLocationResult.

        True if successful, false otherwise  # noqa: E501

        :param successful: The successful of this PdfToWordsWithLocationResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def ocr_pages(self):
        """Gets the ocr_pages of this PdfToWordsWithLocationResult.  # noqa: E501

        OCR page results  # noqa: E501

        :return: The ocr_pages of this PdfToWordsWithLocationResult.  # noqa: E501
        :rtype: list[OcrPageResultWithWordsWithLocation]
        """
        return self._ocr_pages

    @ocr_pages.setter
    def ocr_pages(self, ocr_pages):
        """Sets the ocr_pages of this PdfToWordsWithLocationResult.

        OCR page results  # noqa: E501

        :param ocr_pages: The ocr_pages of this PdfToWordsWithLocationResult.  # noqa: E501
        :type: list[OcrPageResultWithWordsWithLocation]
        """

        self._ocr_pages = ocr_pages

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
        if issubclass(PdfToWordsWithLocationResult, dict):
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
        if not isinstance(other, PdfToWordsWithLocationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
