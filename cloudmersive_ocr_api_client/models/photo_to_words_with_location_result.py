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


class PhotoToWordsWithLocationResult(object):
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
        'text_elements': 'list[OcrPhotoTextElement]',
        'diagnostic_image': 'str'
    }

    attribute_map = {
        'successful': 'Successful',
        'text_elements': 'TextElements',
        'diagnostic_image': 'DiagnosticImage'
    }

    def __init__(self, successful=None, text_elements=None, diagnostic_image=None):  # noqa: E501
        """PhotoToWordsWithLocationResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._text_elements = None
        self._diagnostic_image = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if text_elements is not None:
            self.text_elements = text_elements
        if diagnostic_image is not None:
            self.diagnostic_image = diagnostic_image

    @property
    def successful(self):
        """Gets the successful of this PhotoToWordsWithLocationResult.  # noqa: E501

        True if successful, false otherwise  # noqa: E501

        :return: The successful of this PhotoToWordsWithLocationResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this PhotoToWordsWithLocationResult.

        True if successful, false otherwise  # noqa: E501

        :param successful: The successful of this PhotoToWordsWithLocationResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def text_elements(self):
        """Gets the text_elements of this PhotoToWordsWithLocationResult.  # noqa: E501

        Word elements in the image  # noqa: E501

        :return: The text_elements of this PhotoToWordsWithLocationResult.  # noqa: E501
        :rtype: list[OcrPhotoTextElement]
        """
        return self._text_elements

    @text_elements.setter
    def text_elements(self, text_elements):
        """Sets the text_elements of this PhotoToWordsWithLocationResult.

        Word elements in the image  # noqa: E501

        :param text_elements: The text_elements of this PhotoToWordsWithLocationResult.  # noqa: E501
        :type: list[OcrPhotoTextElement]
        """

        self._text_elements = text_elements

    @property
    def diagnostic_image(self):
        """Gets the diagnostic_image of this PhotoToWordsWithLocationResult.  # noqa: E501

        Typically null.  To analyze OCR performance, enable diagnostic mode by adding the HTTP header \"DiagnosticMode\" with the value \"true\".  When this is true, a diagnostic image showing the details of the OCR result will be set in PNG format into DiagnosticImage.  # noqa: E501

        :return: The diagnostic_image of this PhotoToWordsWithLocationResult.  # noqa: E501
        :rtype: str
        """
        return self._diagnostic_image

    @diagnostic_image.setter
    def diagnostic_image(self, diagnostic_image):
        """Sets the diagnostic_image of this PhotoToWordsWithLocationResult.

        Typically null.  To analyze OCR performance, enable diagnostic mode by adding the HTTP header \"DiagnosticMode\" with the value \"true\".  When this is true, a diagnostic image showing the details of the OCR result will be set in PNG format into DiagnosticImage.  # noqa: E501

        :param diagnostic_image: The diagnostic_image of this PhotoToWordsWithLocationResult.  # noqa: E501
        :type: str
        """
        if diagnostic_image is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', diagnostic_image):  # noqa: E501
            raise ValueError(r"Invalid value for `diagnostic_image`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._diagnostic_image = diagnostic_image

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
        if issubclass(PhotoToWordsWithLocationResult, dict):
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
        if not isinstance(other, PhotoToWordsWithLocationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
