# dtool_lookup_openapi_client.WebhookApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_config_get**](WebhookApi.md#webhook_config_get) | **GET** /webhook/config | Return the JSON-serialized plugin configuration.
[**webhook_notify_path_post**](WebhookApi.md#webhook_notify_path_post) | **POST** /webhook/notify/{path} | Notify the lookup server about creation, modification or deletion of a dataset.
[**webhook_notify_post**](WebhookApi.md#webhook_notify_post) | **POST** /webhook/notify | Notify the lookup server about creation, modification or deletion of a dataset.


# **webhook_config_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} webhook_config_get()

Return the JSON-serialized plugin configuration.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api import webhook_api
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
    api_instance = webhook_api.WebhookApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Return the JSON-serialized plugin configuration.
        api_response = api_instance.webhook_config_get()
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling WebhookApi->webhook_config_get: %s\n" % e)
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

# **webhook_notify_path_post**
> webhook_notify_path_post(path)

Notify the lookup server about creation, modification or deletion of a dataset.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api import webhook_api
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
    api_instance = webhook_api.WebhookApi(api_client)
    path = "path_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Notify the lookup server about creation, modification or deletion of a dataset.
        api_instance.webhook_notify_path_post(path)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling WebhookApi->webhook_notify_path_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |

### Return type

void (empty response body)

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

# **webhook_notify_post**
> webhook_notify_post()

Notify the lookup server about creation, modification or deletion of a dataset.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api import webhook_api
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
    api_instance = webhook_api.WebhookApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Notify the lookup server about creation, modification or deletion of a dataset.
        api_instance.webhook_notify_post()
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling WebhookApi->webhook_notify_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

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

