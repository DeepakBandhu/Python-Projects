class Person:
    def __init__(self, name, age, height):
        self.name = name   
        self._age = age    
        self.__height = height 

p1 = Person("Deepak", 21, 190.5)

print(p1.name)   
print(p1._age)   
print(p1.__height) 
