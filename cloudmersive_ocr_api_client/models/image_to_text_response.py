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


class ImageToTextResponse(object):
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
        'mean_confidence_level': 'float',
        'text_result': 'str'
    }

    attribute_map = {
        'mean_confidence_level': 'MeanConfidenceLevel',
        'text_result': 'TextResult'
    }

    def __init__(self, mean_confidence_level=None, text_result=None):  # noqa: E501
        """ImageToTextResponse - a model defined in Swagger"""  # noqa: E501

        self._mean_confidence_level = None
        self._text_result = None
        self.discriminator = None

        if mean_confidence_level is not None:
            self.mean_confidence_level = mean_confidence_level
        if text_result is not None:
            self.text_result = text_result

    @property
    def mean_confidence_level(self):
        """Gets the mean_confidence_level of this ImageToTextResponse.  # noqa: E501

        Confidence level rating of the OCR operation; ratings above 80% are strong.  # noqa: E501

        :return: The mean_confidence_level of this ImageToTextResponse.  # noqa: E501
        :rtype: float
        """
        return self._mean_confidence_level

    @mean_confidence_level.setter
    def mean_confidence_level(self, mean_confidence_level):
        """Sets the mean_confidence_level of this ImageToTextResponse.

        Confidence level rating of the OCR operation; ratings above 80% are strong.  # noqa: E501

        :param mean_confidence_level: The mean_confidence_level of this ImageToTextResponse.  # noqa: E501
        :type: float
        """

        self._mean_confidence_level = mean_confidence_level

    @property
    def text_result(self):
        """Gets the text_result of this ImageToTextResponse.  # noqa: E501

        Converted text string from the image input.  # noqa: E501

        :return: The text_result of this ImageToTextResponse.  # noqa: E501
        :rtype: str
        """
        return self._text_result

    @text_result.setter
    def text_result(self, text_result):
        """Sets the text_result of this ImageToTextResponse.

        Converted text string from the image input.  # noqa: E501

        :param text_result: The text_result of this ImageToTextResponse.  # noqa: E501
        :type: str
        """

        self._text_result = text_result

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
        if issubclass(ImageToTextResponse, dict):
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
        if not isinstance(other, ImageToTextResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
