class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student %s is here' % self.name
    __repr__ = __str__
    def __getattr__(self, attr):
        if attr =='score':
            return -1
        if attr == 'id':
            return lambda: "unknown"
        raise AttributeError('\'Student\' object has no this attribute \'%s\'' %attr)
    def __call__(self):
        print('My name is %s' %self.name)
        
       
    

s1 = Student('Mick')
print(s1)
print("The score is", s1.score, ". The id is", s1.id())
print(s1())


class Fibonacci(object):
    def __init__(self):
        self.a, self.b = 0 , 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a> 100:
            raise StopIteration()
        return self.a
    def __getitem__(self,n):
        if isinstance(n, int):
            a, b =1, 1
            for x in range(n):
                a, b = b, a+b
            return a 
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L
    
    

for n in Fibonacci():
    print("%d, "%n, end="")
print()

f = Fibonacci()
print("The sixth element is %d." %f[5])
print("The fourth to seventh elements are %s" %f[3:6])






