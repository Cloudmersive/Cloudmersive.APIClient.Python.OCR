# coding: utf-8

"""
    ocrapi

    The powerful Optical Character Recognition (OCR) APIs let you convert scanned images of pages into recognized text.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.api.preprocessing_api import PreprocessingApi  # noqa: E501
from cloudmersive_ocr_api_client.rest import ApiException


class TestPreprocessingApi(unittest.TestCase):
    """PreprocessingApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_ocr_api_client.api.preprocessing_api.PreprocessingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_preprocessing_unrotate(self):
        """Test case for preprocessing_unrotate

        Detect and unrotate a document image  # noqa: E501
        """
        pass

    def test_preprocessing_unskew(self):
        """Test case for preprocessing_unskew

        Detect and unskew a photo of a document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
