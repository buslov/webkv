#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Web storage for key-value data
"""

import shelve
from bottle import Bottle, debug, request, HTTPError

application = Bottle()

__author__ = 'user'
__version__ = '0.1.0'
__license__ = 'MIT'

@application.route('/')
def index():
    return """
write: GET /{id}?key_1=value_1&...&key_n=value_n<br/>
read: GET /{id}
"""

@application.route('/<id>')
def api(id):
    global _storage
    if request.GET:
        _storage[id] = dict(request.GET)
        _storage.sync()
    if id in _storage:
        return _storage[id]
    else:
        raise HTTPError(status=404)

_storage = shelve.open('storage', writeback=True)

if __name__ == '__main__':
    try:
        debug(True)
        application.run(host='0.0.0.0', port='8080')
    except Exception as ex:
        print('Exception: %s' % repr(ex))
