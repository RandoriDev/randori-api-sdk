from __future__ import print_function
import os
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint
configuration = randori_api.Configuration()

# Get the Randori Recon API token from environment variables
api_token = os.getenv("RANDORI_API_KEY")


if api_token is None:
    print("Missing environment variable RANDORI_API_KEY.")
    print("Please export RANDORI_API_KEY=$RANDORI_API_TOKEN first.")
    exit(1)
elif len(api_token) < 100:
    print("This token appears too short. Please ensure the entire token"
          "added as an environment variable.")
    exit(1)

configuration.access_token = api_token

# Defining host is optional and default to https://alpha.randori.io
configuration.host = "https://alpha.randori.io"

# Create an instance of the API class
api_instance = randori_api.RandoriApi(randori_api.ApiClient(configuration))


offset = 0 # int | offset into avilable records after filtering (optional)
limit = 200 # int | maximum number of records to return (optional)
sort = ['-target_temptation'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)

# str | base64 encoded jquery querybuilder complex search field (optional)
q = 'eyJjb25kaXRpb24iOiJBTkQiLCJydWxlcyI6W3sidWlfaWQiOiJ0YWdzIiwiaWQiOiJ0YWJsZS50YWdzIiwiZmllbGQiOiJ0YWJsZS50YWdzIiwiaW5wdXQiOiJ0ZXh0IiwidHlwZSI6InN0cmluZyIsIm9wZXJhdG9yIjoiaGFzX2tleSIsInZhbHVlIjoiSU5URVJFU1RJTkcrTm9DU1MifV19' 

try:
    api_response = api_instance.get_hostname(offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RandoriApi->get_hostname: %s\n" % e)
