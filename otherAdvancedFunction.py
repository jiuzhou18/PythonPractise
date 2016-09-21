import functools

def lazySquare(n):
    def sum(j):
        def square():
            return j*j
        return square
    fs = []
    for i in range(1,n):
        fs.append(sum(i))
    return fs

f1, f2, f3 = lazySquare(4)
print(f1(), f2(), f3())
# a = [x for x in range(1,4)]
# print(a)

def log(textfun):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if not callable(textfun):
                print (textfun, func._name_)
            print('begin call')
            runfun = func(*args, **kw)
            print('finish call')
            return runfun
        return wrapper
    return decorator(textfun) if callable(textfun) else decorator

@log
def trydecorate():
    print ("This is a small function.")

trydecorate()



            
