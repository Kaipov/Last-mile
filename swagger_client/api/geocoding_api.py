# coding: utf-8

"""
    GraphHopper Directions API

    You use the GraphHopper Directions API to add route planning, navigation and route optimization to your software. E.g. the Routing API has turn instructions and elevation data and the Route Optimization API solves your logistic problems and supports various constraints like time window and capacity restrictions. Also it is possible to get all distances between all locations with our fast Matrix API.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class GeocodingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def geocode_get(self, key, **kwargs):  # noqa: E501
        """Execute a Geocoding request  # noqa: E501

        This endpoint provides forward and reverse geocoding. For more details, review the official documentation at: https://graphhopper.com/api/1/docs/geocoding/   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.geocode_get(key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str key: Get your key at graphhopper.com (required)
        :param str q: If you do forward geocoding, then this would be a textual description of the address you are looking for
        :param str locale: Display the search results for the specified locale. Currently French (fr), English (en), German (de) and Italian (it) are supported. If the locale wasn't found the default (en) is used.
        :param int limit: Specify the maximum number of returned results
        :param bool reverse: Set to true to do a reverse Geocoding request, see point parameter
        :param str point: The location bias in the format 'latitude,longitude' e.g. point=45.93272,11.58803
        :param str provider: Can be either, default, nominatim, opencagedata
        :return: GeocodingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.geocode_get_with_http_info(key, **kwargs)  # noqa: E501
        else:
            (data) = self.geocode_get_with_http_info(key, **kwargs)  # noqa: E501
            return data

    def geocode_get_with_http_info(self, key, **kwargs):  # noqa: E501
        """Execute a Geocoding request  # noqa: E501

        This endpoint provides forward and reverse geocoding. For more details, review the official documentation at: https://graphhopper.com/api/1/docs/geocoding/   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.geocode_get_with_http_info(key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str key: Get your key at graphhopper.com (required)
        :param str q: If you do forward geocoding, then this would be a textual description of the address you are looking for
        :param str locale: Display the search results for the specified locale. Currently French (fr), English (en), German (de) and Italian (it) are supported. If the locale wasn't found the default (en) is used.
        :param int limit: Specify the maximum number of returned results
        :param bool reverse: Set to true to do a reverse Geocoding request, see point parameter
        :param str point: The location bias in the format 'latitude,longitude' e.g. point=45.93272,11.58803
        :param str provider: Can be either, default, nominatim, opencagedata
        :return: GeocodingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'q', 'locale', 'limit', 'reverse', 'point', 'provider']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method geocode_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if ('key' not in params or
                params['key'] is None):
            raise ValueError("Missing the required parameter `key` when calling `geocode_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'locale' in params:
            query_params.append(('locale', params['locale']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'reverse' in params:
            query_params.append(('reverse', params['reverse']))  # noqa: E501
        if 'point' in params:
            query_params.append(('point', params['point']))  # noqa: E501
        if 'provider' in params:
            query_params.append(('provider', params['provider']))  # noqa: E501
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/geocode', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GeocodingResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
