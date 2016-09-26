class Student(object):
    type = 'student'
    __slots__ = ('name', '_age')
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('age must be a integer')
        if value < 0 or value >150:
            print('age must between 0 and 150')
        self._age = value
    


s= Student()
s.name = 'Mick'
s.age = 18
# s.score = 90
s.age = -1

class HighStudent(Student):
    pass

hs = HighStudent()
hs.score = 70



class Screen(object):
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be a integer')
        if value < 0:
            print('width must be positive')
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be a integer')
        if value < 0:
            print('height must be positive')
        self._height = value
        
    @property
    def solution(self):
        return self._height*self._width


screen = Screen()
screen.width = 16
screen.height = 20
print(screen.solution)
assert screen.solution == 320
