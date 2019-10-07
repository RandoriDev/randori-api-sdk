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
q = 'ewogICJjb25kaXRpb24iOiAiQU5EIiwKICAicnVsZXMiOiBbCiAgICB7CiAgICAgICJmaWVsZCI6ICJ0YWJsZS5jb25maWRlbmNlIiwKICAgICAgIm9wZXJhdG9yIjogImdyZWF0ZXJfb3JfZXF1YWwiLAogICAgICAidmFsdWUiOiA2MAogICAgfSwKICAgIHsKICAgICAgImZpZWxkIjogInRhYmxlLnRhcmdldF90ZW1wdGF0aW9uIiwKICAgICAgIm9wZXJhdG9yIjogImdyZWF0ZXJfb3JfZXF1YWwiLAogICAgICAidmFsdWUiOiAxNQogICAgfSwKICAgIHsKICAgICAgImZpZWxkIjogInRhYmxlLnRhZ3MiLAogICAgICAib3BlcmF0b3IiOiAiaGFzX2tleSIsCiAgICAgICJ2YWx1ZSI6ICJJTlRFUkVTVElORytOb0NTUyIKICAgIH0KICBdCn0=' 

try:
    api_response = api_instance.get_target(offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RandoriApi->get_hostname: %s\n" % e)
