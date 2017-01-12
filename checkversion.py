#!/usr/bin/env python

import requests

print requests.__version__

#response = requests.get("http://google.com")

#print response.text
#print response.status_code

response = requests.get("https://raw.githubusercontent.com/tiegan/CMPUT404/master/checkversion.py")

print response.text