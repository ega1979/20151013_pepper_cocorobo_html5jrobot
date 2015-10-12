#!/usr/local/bin/python
# -*- coding: utf-8 -*-
print "Switch Off!";

import pycurl
import urllib
import json

option = {"赤外線情報を入力"}


c = pycurl.Curl()
c.setopt(pycurl.URL, 'http://IP Address/messages')
c.setopt(pycurl.HTTPHEADER, ['X-Requested-With: curl'])
c.setopt(pycurl.POSTFIELDS, json.dumps(option))
c.setopt(pycurl.POST, 1)
c.perform()
c.close()