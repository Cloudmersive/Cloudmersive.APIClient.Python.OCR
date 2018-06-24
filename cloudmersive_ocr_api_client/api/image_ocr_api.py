# coding: utf-8

"""
    ocrapi

    The powerful Optical Character Recognition (OCR) APIs let you convert scanned images of pages into recognized text.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudmersive_ocr_api_client.api_client import ApiClient


class ImageOcrApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def image_ocr_post(self, image_file, **kwargs):  # noqa: E501
        """Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.image_ocr_post(image_file, async=True)
        >>> result = thread.get()

        :param async bool
        :param file image_file: Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported. (required)
        :return: ImageToTextResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.image_ocr_post_with_http_info(image_file, **kwargs)  # noqa: E501
        else:
            (data) = self.image_ocr_post_with_http_info(image_file, **kwargs)  # noqa: E501
            return data

    def image_ocr_post_with_http_info(self, image_file, **kwargs):  # noqa: E501
        """Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.image_ocr_post_with_http_info(image_file, async=True)
        >>> result = thread.get()

        :param async bool
        :param file image_file: Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported. (required)
        :return: ImageToTextResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['image_file']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_ocr_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_file' is set
        if ('image_file' not in params or
                params['image_file'] is None):
            raise ValueError("Missing the required parameter `image_file` when calling `image_ocr_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'image_file' in params:
            local_var_files['imageFile'] = params['image_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/ocr/image/toText', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ImageToTextResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
