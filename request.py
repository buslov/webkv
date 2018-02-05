#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
A client for webkv
"""

from __future__ import print_function

import json
import sys
if sys.version_info[0]==2:
    from urllib import urlencode, urlopen
elif sys.version_info[0]==3:
    from urllib.parse import urlencode
    from urllib.request import urlopen
else:
    raise Exception('Unsupported version of Python')

def webkv_query(host, id, **kv):
    params=urlencode(kv)
    url=host.format(id=id)+'?'+urlencode(kv)
    return json.loads(urlopen(url).read())

if __name__ == '__main__':
    from timeit import timeit
    webkvserv='http://127.0.0.1:8080/{id}'
    number=10
    dt=timeit('webkv_query(webkvserv, "test", x=1231)',
              setup='from __main__ import webkv_query, webkvserv',
              number=number)
    print('timings:', dt/number)

