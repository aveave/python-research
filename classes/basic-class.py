class Person:
    # first define this
    # age = 0
    # name = ''
    
    # we can omit these definition if we use constructor
    # age = 0
    # name = ''


    # constructor function
    # cannot have multiple constructors with the same name
    # def __init__(self, age, name):
    #     self.age = age
    #     self.name = name

    # constructor with None params
    def __init__(self, age = None, name = None):
        self.age = age
        self.name = name

person1 = Person(5, 'Ivan')
person2 = Person(100)

person3 = Person(name = 'Kek')

print(person1.age)
print(person1.name)

print('person2 age = ', person2.age)
print('person3 name = ', person3.name, 'person3 age = ', person3.age)
person1.age = 10
person1.name = 'test'

print(person1.age)
print(person1.name)

# we can create multiple objects

# self is a reference to the instance of a class that a method is being called on. 
# It allows you to access the attributes and methods of that instance within the method definition.

# self parameter in the method definition is automatically set to the object on which method was called