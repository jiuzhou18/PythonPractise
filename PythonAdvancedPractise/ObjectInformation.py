
print(type(123))
print(type("ABC"))

print(isinstance(123, int))
print(isinstance("ABC", str))

print(dir('ABC'))

class Animal(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def run(self):
        print("The", self.__name, "is running.")

animal = Animal('kitty', 4)
print(hasattr(animal, '_Animal__age'))

