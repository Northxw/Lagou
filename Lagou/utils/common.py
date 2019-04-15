# -*- coding:utf-8 -*-

import hashlib
import math

def get_md5(url):
    # md5
    if isinstance(url, str):
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

def get_avg_salary(value):
    a,b = value.replace('k','').split('-')
    return str(math.ceil((int(a)+int(b))/2))

if __name__ == '__main__':
    pass