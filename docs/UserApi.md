# dtool_lookup_openapi_client.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_info_username_get**](UserApi.md#user_info_username_get) | **GET** /user/info/{username} | Return a user&#39;s information.


# **user_info_username_get**
> UserResponse user_info_username_get(username)

Return a user's information.

A user can see his/her own profile. An admin user can see other user's profiles.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api import user_api
from dtool_lookup_openapi_client.model.user_response import UserResponse
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
    api_instance = user_api.UserApi(api_client)
    username = "username_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Return a user's information.
        api_response = api_instance.user_info_username_get(username)
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_info_username_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |

### Return type

[**UserResponse**](UserResponse.md)

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

