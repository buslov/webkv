#!/usr/bin/env python
#-*-coding:utf-8-*-

if __name__ == '__main__':
    import os
    import os.path
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    from request import webkv_query
    from time import sleep, clock
    host = 'http://webkv.pythonanywhere.com/{id}'
    host = 'http://127.0.0.1:8080/{id}'
    id = 'test'
    while True:
        print(clock(), webkv_query(host, id))
        sleep(0.5)
