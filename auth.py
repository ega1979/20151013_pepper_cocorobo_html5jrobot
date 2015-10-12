#!/usr/local/bin/python
# -*- coding: utf-8 -*-
print "Get Auth";

import pycurl
import urllib
import json

option = {"apikey_cocorobo":"apikeyを入力"}

c = pycurl.Curl()
c.setopt(pycurl.URL, 'https://developer.cloudlabs.sharp.co.jp/cloudlabs-api/cocorobo/auth')
c.setopt(pycurl.HTTPHEADER, ['Content-Type : application/json'])
c.setopt(pycurl.POSTFIELDS, json.dumps(option))
c.setopt(pycurl.POST, 1)
c.perform()
c.close()