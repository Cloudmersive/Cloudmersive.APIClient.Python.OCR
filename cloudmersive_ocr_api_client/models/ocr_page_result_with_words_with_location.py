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


class OcrPageResultWithWordsWithLocation(object):
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
        'page_number': 'int',
        'successful': 'bool',
        'words': 'list[OcrWordElement]'
    }

    attribute_map = {
        'page_number': 'PageNumber',
        'successful': 'Successful',
        'words': 'Words'
    }

    def __init__(self, page_number=None, successful=None, words=None):  # noqa: E501
        """OcrPageResultWithWordsWithLocation - a model defined in Swagger"""  # noqa: E501

        self._page_number = None
        self._successful = None
        self._words = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if successful is not None:
            self.successful = successful
        if words is not None:
            self.words = words

    @property
    def page_number(self):
        """Gets the page_number of this OcrPageResultWithWordsWithLocation.  # noqa: E501

        Page number of the page that was OCR-ed, starting with 1 for the first page in the PDF file  # noqa: E501

        :return: The page_number of this OcrPageResultWithWordsWithLocation.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this OcrPageResultWithWordsWithLocation.

        Page number of the page that was OCR-ed, starting with 1 for the first page in the PDF file  # noqa: E501

        :param page_number: The page_number of this OcrPageResultWithWordsWithLocation.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def successful(self):
        """Gets the successful of this OcrPageResultWithWordsWithLocation.  # noqa: E501

        True if successful, false otherwise  # noqa: E501

        :return: The successful of this OcrPageResultWithWordsWithLocation.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this OcrPageResultWithWordsWithLocation.

        True if successful, false otherwise  # noqa: E501

        :param successful: The successful of this OcrPageResultWithWordsWithLocation.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def words(self):
        """Gets the words of this OcrPageResultWithWordsWithLocation.  # noqa: E501

        Word elements in the image  # noqa: E501

        :return: The words of this OcrPageResultWithWordsWithLocation.  # noqa: E501
        :rtype: list[OcrWordElement]
        """
        return self._words

    @words.setter
    def words(self, words):
        """Sets the words of this OcrPageResultWithWordsWithLocation.

        Word elements in the image  # noqa: E501

        :param words: The words of this OcrPageResultWithWordsWithLocation.  # noqa: E501
        :type: list[OcrWordElement]
        """

        self._words = words

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
        if issubclass(OcrPageResultWithWordsWithLocation, dict):
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
        if not isinstance(other, OcrPageResultWithWordsWithLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
