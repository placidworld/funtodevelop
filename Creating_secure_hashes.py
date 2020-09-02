# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:09:04 2020

@author: heart
"""
import hashlib

# sha1 Digest
hashlib.sha1("Python is fun as I expected.").hexdigest()

# sha224 Digest
hashlib.sha224("Python is fun as I expected.").hexdigest()

# sha256 Digest
hashlib.sha256("Python is fun as I expected.").hexdigest()

# sha384 Digest
hashlib.sha384("Python is fun as I expected.").hexdigest()

# sha512 Digest
hashlib.sha512("Python is fun as I expected.").hexdigest()

# MD5 Digest
hashlib.md5("Python is fun as I expected.").hexdigest()
