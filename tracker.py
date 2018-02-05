#!/usr/bin/env python
#-*-coding:utf-8-*-

try:
    import android
    __android__ = True
except ImportError:
    __android__ = False

if __name__ == '__main__':
    import os
    import os.path
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    from request import webkv_query
    import time
    if __android__:
        droid=android.Android()
        def getLocation(droid=droid):
            res = droid.getLastKnownLocation().result
            res = res['gps']
            if res:
                return (res['latitude'], res['longitude'])
            else:
                raise Exception('No GPS data')
    else:
        from random import random
        from math import floor
        def getLocation():
            lat=51.64+0.1*(random()*2-1)
            lon=39.22+0.1*(random()*2-1)
            return (lat,lon)

    id = 'test1'
    if __android__:
        id = droid.dialogGetInput("Введите ключ webkv", "Введите ключ webkv",
            "test1").result
    host = 'http://webkv.pythonanywhere.com/{id}'
    #host = 'http://127.0.0.1:8080/{id}'

    while id:
        try:
            lat,lon = getLocation()
            print(lat,lon)
            print(webkv_query(host, id, lat=lat, lon=lon,
                ts=int(time.time())))
        except Exception:
            pass
        time.sleep(2)
