#!/usr/local/bin/python
# -*- coding: utf-8 -*-
print "Let's Speech!";

import pycurl
import urllib
import json

option = { "apikey_cocorobo": "apikeyを入力", "message":"だまってろ、ボケ" }

c = pycurl.Curl()
c.setopt(pycurl.URL, 'https://developer.cloudlabs.sharp.co.jp/cloudlabs-api/cocorobo/speech')
c.setopt(pycurl.HTTPHEADER, ['Content-Type : application/json'])
c.setopt(pycurl.POSTFIELDS, json.dumps(option))
c.setopt(pycurl.POST, 1)
c.perform()
c.close()
