#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('ABC'.encode('ascii'), "\n", b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'));
print(len('中文'), " " ,chr(25991));
s1 = 72
s2 = 85
r = s2/s1 -1
print('The growth rate is %.1f %%' %( r))