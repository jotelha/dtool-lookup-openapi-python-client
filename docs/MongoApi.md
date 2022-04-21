# dtool_lookup_openapi_client.MongoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mongo_aggregate_post**](MongoApi.md#mongo_aggregate_post) | **POST** /mongo/aggregate | Aggregate the datasets a user has access to.
[**mongo_config_get**](MongoApi.md#mongo_config_get) | **GET** /mongo/config | Return the JSON-serialized plugin configuration.
[**mongo_query_post**](MongoApi.md#mongo_query_post) | **POST** /mongo/query | Query datasets a user has access to.


# **mongo_aggregate_post**
> [DatasetSQLAlchemy] mongo_aggregate_post(body)

Aggregate the datasets a user has access to.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api import mongo_api
from dtool_lookup_openapi_client.model.pagination_metadata import PaginationMetadata
from dtool_lookup_openapi_client.model.dataset_sql_alchemy import DatasetSQLAlchemy
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
    api_instance = mongo_api.MongoApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 10 # int |  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Aggregate the datasets a user has access to.
        api_response = api_instance.mongo_aggregate_post(body)
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling MongoApi->mongo_aggregate_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Aggregate the datasets a user has access to.
        api_response = api_instance.mongo_aggregate_post(body, page=page, page_size=page_size)
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling MongoApi->mongo_aggregate_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 10

### Return type

[**[DatasetSQLAlchemy]**](DatasetSQLAlchemy.md)

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

# **mongo_config_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} mongo_config_get()

Return the JSON-serialized plugin configuration.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api import mongo_api
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
    api_instance = mongo_api.MongoApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Return the JSON-serialized plugin configuration.
        api_response = api_instance.mongo_config_get()
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling MongoApi->mongo_config_get: %s\n" % e)
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

# **mongo_query_post**
> [DatasetSQLAlchemy] mongo_query_post(body)

Query datasets a user has access to.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api import mongo_api
from dtool_lookup_openapi_client.model.pagination_metadata import PaginationMetadata
from dtool_lookup_openapi_client.model.dataset_sql_alchemy import DatasetSQLAlchemy
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
    api_instance = mongo_api.MongoApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 10 # int |  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Query datasets a user has access to.
        api_response = api_instance.mongo_query_post(body)
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling MongoApi->mongo_query_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Query datasets a user has access to.
        api_response = api_instance.mongo_query_post(body, page=page, page_size=page_size)
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling MongoApi->mongo_query_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 10

### Return type

[**[DatasetSQLAlchemy]**](DatasetSQLAlchemy.md)

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

