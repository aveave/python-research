# https://pynative.com/python-mysql-execute-parameterized-query-using-prepared-statement/
# кортеж - неизменяемая последовательность элементов
# To return multiple values from a function
# When you want to guarantee that the contents of a sequence cannot be changed

#A tuple is a collection of immutable (unchangeable) objects that are ordered and indexed. Here are some things you should know about tuples in Python:

#Tuples are created using parentheses ()
#Tuples can contain elements of different types
t = ('test', 1)

print(t)

arr = list(['test', 1, 1.0])
t = tuple(arr)

print(t)
print(t[0]) # index
#Tuples are immutable, meaning that you cannot change the elements of a tuple once it has been created
#t[0] = 'new' # TypeError: 'tuple' object does not support item assignment
print(t)

for item in t:
    print('item is ', item)
if 'test' in t:
    print('tuple contains test')

my_dict = {('apple', 1): 'red', ('banana', 2): 'yellow', ('orange', 3): 'orange'}

# Accessing values using tuple keys
print(my_dict[('apple', 1)])  # Output: red
print(my_dict[('banana', 2)])  # Output: yellow
print(my_dict[('orange', 3)])  # Output: orange

def get_person_info():
    name = 'John'
    age = 10
    number = '8900'
    return (name, age, number)

(name, age, number) = get_person_info()
print('name is ', name)
print('age is ', age)

person_tuple = get_person_info()
(name1, age1, number1) = person_tuple
print('name1 is ', name1)
print('number1 is ', number1)


my_tuple = (1, 2, 3)
# a, b = my_tuple   # ValueError: too many values to unpack 
a, b, c = my_tuple  # Fine
print('b is ', b)
a = my_tuple  # Fine, assigns the whole tuple
print('a is ', a)