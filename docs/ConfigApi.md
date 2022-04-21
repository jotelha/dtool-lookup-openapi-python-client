# dtool_lookup_openapi_client.ConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_info_get**](ConfigApi.md#config_info_get) | **GET** /config/info | Return the JSON-serialized server configuration.


# **config_info_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} config_info_get()

Return the JSON-serialized server configuration.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api import config_api
from dtool_lookup_openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dtool_lookup_openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dtool_lookup_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with dtool_lookup_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = config_api.ConfigApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Return the JSON-serialized server configuration.
        api_response = api_instance.config_info_get()
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling ConfigApi->config_info_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

