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

from cloudmersive_ocr_api_client.models.ocr_word_element import OcrWordElement  # noqa: F401,E501


class OcrLineElement(object):
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
        'line_text': 'str',
        'words': 'list[OcrWordElement]'
    }

    attribute_map = {
        'line_text': 'LineText',
        'words': 'Words'
    }

    def __init__(self, line_text=None, words=None):  # noqa: E501
        """OcrLineElement - a model defined in Swagger"""  # noqa: E501

        self._line_text = None
        self._words = None
        self.discriminator = None

        if line_text is not None:
            self.line_text = line_text
        if words is not None:
            self.words = words

    @property
    def line_text(self):
        """Gets the line_text of this OcrLineElement.  # noqa: E501

        Text of the line  # noqa: E501

        :return: The line_text of this OcrLineElement.  # noqa: E501
        :rtype: str
        """
        return self._line_text

    @line_text.setter
    def line_text(self, line_text):
        """Sets the line_text of this OcrLineElement.

        Text of the line  # noqa: E501

        :param line_text: The line_text of this OcrLineElement.  # noqa: E501
        :type: str
        """

        self._line_text = line_text

    @property
    def words(self):
        """Gets the words of this OcrLineElement.  # noqa: E501

        Word objects in the line  # noqa: E501

        :return: The words of this OcrLineElement.  # noqa: E501
        :rtype: list[OcrWordElement]
        """
        return self._words

    @words.setter
    def words(self, words):
        """Sets the words of this OcrLineElement.

        Word objects in the line  # noqa: E501

        :param words: The words of this OcrLineElement.  # noqa: E501
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OcrLineElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
