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

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getToken(ipaddress, user, password):
    response = {}
    try:
        url = "https://"+ ipaddress +"/v1/login"
        credentials = {"username":user, "password":password, "tenant":"default"}
        headers = {}
        headers["Content-Type"] = "application/json"
        response = requests.post(url, headers=headers,data=json.dumps(credentials), verify=False, timeout = 5)
        headers = response.headers
        return headers["Set-Cookie"]
    except ConnectionError:
        response.update({"message":"Connection error, no response from PSM"})
        return response
    except Exception as err:
        response.update({"message":"Failed to establishg a connection to the PSM"})
        return response

def getApi(ipaddress, token, url):
    headers = makeHeaders(token)
    url = "https://{}{}".format(ipaddress, url)
    response = requests.get(url, headers=headers, verify=False)
    return response.json()

def deleteApi(ipaddress, token, url):
    headers = makeHeaders(token)
    url = "https://{}{}".format(ipaddress, url)
    response = requests.delete(url, headers=headers, verify=False)
    return response.status_code

def postApi(ipaddress, token, url, json_data):
    headers = makeHeaders(token)
    url = "https://{}{}".format(ipaddress, url)
    response = requests.post(url, headers=headers, data=json.dumps(json_data), verify=False)
    return response.json()

def putApi(ipaddress, token, url, json_data):
    headers = makeHeaders(token)
    url = "https://{}{}".format(ipaddress, url)
    response = requests.get(url, headers=headers, data=json.dumps(json_data), verify=False)
    return response.json()

def makeHeaders(token):
    headers = {}
    headers["Content-Type"] = "application/json"
    headers["accept"] = "application/json; version=1.0"
    headers['cookie'] = token
    return headers

def getData(file_data):
    with open(file_data, 'r') as file:
        data = file.read().replace('\n', '')
        data = data.replace(" ","")
    return json.loads(data)
