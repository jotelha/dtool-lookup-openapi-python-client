"""
    dtool-lookup-server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api.base_uri_api import BaseUriApi  # noqa: E501


class TestBaseUriApi(unittest.TestCase):
    """BaseUriApi unit test stubs"""

    def setUp(self):
        self.api = BaseUriApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_base_uri_list_get(self):
        """Test case for admin_base_uri_list_get

        List all base_uris.  # noqa: E501
        """
        pass

    def test_admin_base_uri_register_post(self):
        """Test case for admin_base_uri_register_post

        Register a base URI.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
