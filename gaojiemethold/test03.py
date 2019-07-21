# -*- coding:utf-8 -*-

import hashlib

m=hashlib.md5()

m.update('itcast')

print m.hexdigest()









