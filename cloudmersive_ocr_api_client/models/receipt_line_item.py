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


class ReceiptLineItem(object):
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
        'item_description': 'str',
        'item_price': 'float'
    }

    attribute_map = {
        'item_description': 'ItemDescription',
        'item_price': 'ItemPrice'
    }

    def __init__(self, item_description=None, item_price=None):  # noqa: E501
        """ReceiptLineItem - a model defined in Swagger"""  # noqa: E501

        self._item_description = None
        self._item_price = None
        self.discriminator = None

        if item_description is not None:
            self.item_description = item_description
        if item_price is not None:
            self.item_price = item_price

    @property
    def item_description(self):
        """Gets the item_description of this ReceiptLineItem.  # noqa: E501


        :return: The item_description of this ReceiptLineItem.  # noqa: E501
        :rtype: str
        """
        return self._item_description

    @item_description.setter
    def item_description(self, item_description):
        """Sets the item_description of this ReceiptLineItem.


        :param item_description: The item_description of this ReceiptLineItem.  # noqa: E501
        :type: str
        """

        self._item_description = item_description

    @property
    def item_price(self):
        """Gets the item_price of this ReceiptLineItem.  # noqa: E501


        :return: The item_price of this ReceiptLineItem.  # noqa: E501
        :rtype: float
        """
        return self._item_price

    @item_price.setter
    def item_price(self, item_price):
        """Sets the item_price of this ReceiptLineItem.


        :param item_price: The item_price of this ReceiptLineItem.  # noqa: E501
        :type: float
        """

        self._item_price = item_price

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
        if issubclass(ReceiptLineItem, dict):
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
        if not isinstance(other, ReceiptLineItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other