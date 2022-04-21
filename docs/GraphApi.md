# dtool_lookup_openapi_client.GraphApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_config_get**](GraphApi.md#graph_config_get) | **GET** /graph/config | Return the JSON-serialized dependency graph plugin configuration.
[**graph_lookup_uuid_get**](GraphApi.md#graph_lookup_uuid_get) | **GET** /graph/lookup/{uuid} | List the datasets within the same dependency graph as &lt;uuid&gt;. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.
[**graph_lookup_uuid_post**](GraphApi.md#graph_lookup_uuid_post) | **POST** /graph/lookup/{uuid} | List the datasets within the same dependency graph as &lt;uuid&gt;. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.


# **graph_config_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} graph_config_get()

Return the JSON-serialized dependency graph plugin configuration.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api import graph_api
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
    api_instance = graph_api.GraphApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Return the JSON-serialized dependency graph plugin configuration.
        api_response = api_instance.graph_config_get()
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling GraphApi->graph_config_get: %s\n" % e)
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

# **graph_lookup_uuid_get**
> [Dataset] graph_lookup_uuid_get(uuid)

List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api import graph_api
from dtool_lookup_openapi_client.model.pagination_metadata import PaginationMetadata
from dtool_lookup_openapi_client.model.dataset import Dataset
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
    api_instance = graph_api.GraphApi(api_client)
    uuid = "uuid_example" # str | 
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 10 # int |  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.
        api_response = api_instance.graph_lookup_uuid_get(uuid)
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling GraphApi->graph_lookup_uuid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.
        api_response = api_instance.graph_lookup_uuid_get(uuid, page=page, page_size=page_size)
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling GraphApi->graph_lookup_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 10

### Return type

[**[Dataset]**](Dataset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Pagination -  <br>  |
**422** | Unprocessable Entity |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_lookup_uuid_post**
> [Dataset] graph_lookup_uuid_post(uuid, dependency_keys)

List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api import graph_api
from dtool_lookup_openapi_client.model.pagination_metadata import PaginationMetadata
from dtool_lookup_openapi_client.model.dataset import Dataset
from dtool_lookup_openapi_client.model.dependency_keys import DependencyKeys
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
    api_instance = graph_api.GraphApi(api_client)
    uuid = "uuid_example" # str | 
    dependency_keys = DependencyKeys(
        dependency_keys=[
            "dependency_keys_example",
        ],
    ) # DependencyKeys | 
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 10 # int |  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.
        api_response = api_instance.graph_lookup_uuid_post(uuid, dependency_keys)
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling GraphApi->graph_lookup_uuid_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.
        api_response = api_instance.graph_lookup_uuid_post(uuid, dependency_keys, page=page, page_size=page_size)
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling GraphApi->graph_lookup_uuid_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **dependency_keys** | [**DependencyKeys**](DependencyKeys.md)|  |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 10

### Return type

[**[Dataset]**](Dataset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | OK |  * X-Pagination -  <br>  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

