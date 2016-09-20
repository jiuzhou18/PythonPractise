def normalize(name):
    return name.capitalize()

L1 = ['jack', 'bill', 'rudy']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce

def prod(L):
    def times(x,y):
        return x*y
    return reduce(times, L)
    
def prodnew(L):
    return reduce(lambda x, y: x*y, L)


print('3*5*7*9 =', prod([3,5,7,9]))
print('3*5*7*9 =', prodnew([3,5,7,9]))

def str2float(s):
    def char2num(a):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9} [a]
    int1 = reduce(lambda x,y: x*10+y,  map(char2num, s.replace('.',""))) 
    return int1/10**(len(s)-s.find('.')-1)

print('str2float(\'123.4567\') =', str2float('123.4567'))

