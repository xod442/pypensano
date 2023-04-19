# pypensano
A mini python binding for Pensando API interaction
```
import requests
from requests.auth import HTTPBasicAuth
from requests.structures import CaseInsensitiveDict
import urllib3
import json
import pypensando

ipaddress = "10.251.1.23"
user = "admin"
password = "Pensando0$"

# Get Token
token = pypensando.getToken(ipaddress, user, password)

url = "/events/v1/events"
url2 = "/configs/network/v1/tenant/default/networks"

# Get events DEMO of GET
response = pypensando.getApi(ipaddress, token, url)
print(json.dumps(response, indent=4))

# Create networks Demo of POST
data = pypensando.getData(filename)
response =pypensando.postApi(ipaddress, token, url2, data)
print(json.dumps(response, indent=4))
```
