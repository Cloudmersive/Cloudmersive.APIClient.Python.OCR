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
from cloudmersive_ocr_api_client.api.pdf_ocr_api import PdfOcrApi  # noqa: E501
from cloudmersive_ocr_api_client.rest import ApiException


class TestPdfOcrApi(unittest.TestCase):
    """PdfOcrApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_ocr_api_client.api.pdf_ocr_api.PdfOcrApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pdf_ocr_post(self):
        """Test case for pdf_ocr_post

        Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
