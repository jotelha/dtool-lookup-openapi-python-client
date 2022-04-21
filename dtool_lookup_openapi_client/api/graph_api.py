"""
    dtool-lookup-server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from dtool_lookup_openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from dtool_lookup_openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from dtool_lookup_openapi_client.model.dataset_sql_alchemy import DatasetSQLAlchemy
from dtool_lookup_openapi_client.model.dependency_keys import DependencyKeys
from dtool_lookup_openapi_client.model.error import Error
from dtool_lookup_openapi_client.model.pagination_metadata import PaginationMetadata


class GraphApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.graph_config_get_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/graph/config',
                'operation_id': 'graph_config_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.graph_lookup_uuid_get_endpoint = _Endpoint(
            settings={
                'response_type': ([DatasetSQLAlchemy],),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/graph/lookup/{uuid}',
                'operation_id': 'graph_lookup_uuid_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'uuid',
                    'page',
                    'page_size',
                ],
                'required': [
                    'uuid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'uuid',
                    'page',
                    'page_size',
                ]
            },
            root_map={
                'validations': {
                    ('uuid',): {

                        'min_length': 1,
                    },
                    ('page',): {

                        'inclusive_minimum': 1,
                    },
                    ('page_size',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'uuid':
                        (str,),
                    'page':
                        (int,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'uuid': 'uuid',
                    'page': 'page',
                    'page_size': 'page_size',
                },
                'location_map': {
                    'uuid': 'path',
                    'page': 'query',
                    'page_size': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.graph_lookup_uuid_post_endpoint = _Endpoint(
            settings={
                'response_type': ([DatasetSQLAlchemy],),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/graph/lookup/{uuid}',
                'operation_id': 'graph_lookup_uuid_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'uuid',
                    'dependency_keys',
                    'page',
                    'page_size',
                ],
                'required': [
                    'uuid',
                    'dependency_keys',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'uuid',
                    'page',
                    'page_size',
                ]
            },
            root_map={
                'validations': {
                    ('uuid',): {

                        'min_length': 1,
                    },
                    ('page',): {

                        'inclusive_minimum': 1,
                    },
                    ('page_size',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'uuid':
                        (str,),
                    'dependency_keys':
                        (DependencyKeys,),
                    'page':
                        (int,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'uuid': 'uuid',
                    'page': 'page',
                    'page_size': 'page_size',
                },
                'location_map': {
                    'uuid': 'path',
                    'dependency_keys': 'body',
                    'page': 'query',
                    'page_size': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def graph_config_get(
        self,
        **kwargs
    ):
        """Return the JSON-serialized dependency graph plugin configuration.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.graph_config_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.graph_config_get_endpoint.call_with_http_info(**kwargs)

    def graph_lookup_uuid_get(
        self,
        uuid,
        **kwargs
    ):
        """List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.graph_lookup_uuid_get(uuid, async_req=True)
        >>> result = thread.get()

        Args:
            uuid (str):

        Keyword Args:
            page (int): [optional] if omitted the server will use the default value of 1
            page_size (int): [optional] if omitted the server will use the default value of 10
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [DatasetSQLAlchemy]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['uuid'] = \
            uuid
        return self.graph_lookup_uuid_get_endpoint.call_with_http_info(**kwargs)

    def graph_lookup_uuid_post(
        self,
        uuid,
        dependency_keys,
        **kwargs
    ):
        """List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.graph_lookup_uuid_post(uuid, dependency_keys, async_req=True)
        >>> result = thread.get()

        Args:
            uuid (str):
            dependency_keys (DependencyKeys):

        Keyword Args:
            page (int): [optional] if omitted the server will use the default value of 1
            page_size (int): [optional] if omitted the server will use the default value of 10
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [DatasetSQLAlchemy]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['uuid'] = \
            uuid
        kwargs['dependency_keys'] = \
            dependency_keys
        return self.graph_lookup_uuid_post_endpoint.call_with_http_info(**kwargs)
