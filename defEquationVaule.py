# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):
#     if not isinstance(a, (int,float)):
#         raise TypeError('bad opera type')
#     if not isinstance(b, (int,float)):
#         raise TypeError('bad opera type')
#     if not isinstance(c, (int,float)):
#         raise TypeError('bad opera type')
    delta = b**2+4*a*c 
    if delta>=0:
        x1 = (-b+math.sqrt(delta))/a/2
        x2 = (b+math.sqrt(delta))/a/2
        return x1,x2
    else:
        print('No root')
        pass
    

a = eval(input("input a number for a: "))
b = eval(input("input a number for b: "))
c = eval(input("input a number for c: "))
x1,x2 = quadratic(a, b, c)
print(x1,x2)