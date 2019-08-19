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

from cloudmersive_ocr_api_client.models.form_field_definition import FormFieldDefinition  # noqa: F401,E501


class FormDefinitionTemplate(object):
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
        'field_definitions': 'list[FormFieldDefinition]'
    }

    attribute_map = {
        'field_definitions': 'FieldDefinitions'
    }

    def __init__(self, field_definitions=None):  # noqa: E501
        """FormDefinitionTemplate - a model defined in Swagger"""  # noqa: E501

        self._field_definitions = None
        self.discriminator = None

        if field_definitions is not None:
            self.field_definitions = field_definitions

    @property
    def field_definitions(self):
        """Gets the field_definitions of this FormDefinitionTemplate.  # noqa: E501


        :return: The field_definitions of this FormDefinitionTemplate.  # noqa: E501
        :rtype: list[FormFieldDefinition]
        """
        return self._field_definitions

    @field_definitions.setter
    def field_definitions(self, field_definitions):
        """Sets the field_definitions of this FormDefinitionTemplate.


        :param field_definitions: The field_definitions of this FormDefinitionTemplate.  # noqa: E501
        :type: list[FormFieldDefinition]
        """

        self._field_definitions = field_definitions

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
        if issubclass(FormDefinitionTemplate, dict):
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
        if not isinstance(other, FormDefinitionTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other