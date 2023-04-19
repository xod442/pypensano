#!/usr/bin/env python3
'''
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

__license__ = "Apache2"
__version__ = "0.1.1"
__maintainer__ = "Rick Kauffman"
__status__ = "Alpha"
-------------------------------------------------------------------------------
'''
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
