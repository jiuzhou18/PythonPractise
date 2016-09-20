# -*- coding: utf-8 -*-

def triangles():
    a = [1]
    while(1):
        n = len(a)-1
        while n>0:
            a[n] = a[n] +a[n-1]
            n -= 1
        a.append(1)
        yield a

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break    
     
