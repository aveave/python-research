numbers = []
numbers1 = list()

numbers2 = [1, 2, 3, 4]
numbers3 = list([1, 2, 3])
# numbers4 = list(4)
print(numbers2)
print(numbers3)
print('compare arrays', numbers2 == numbers3)
# размер массива
print(len(numbers3))
# обращение к элементу
print('first el is ', numbers3[0])
numbers3[0] = 100
print('first el is ', numbers3[0])

# пройти по списку
for num in numbers3:
    print('num is ', num)

# Operations
numbers5 = []
#Диапазоны или range представляют неизменяемый последовательный набор чисел.
# можно range(10) range(start, stop), range(start, stop, step)
for i in range(10):
    numbers5.append(i)
print(numbers5)
print('min is ', min(numbers5))
print('max is ', max(numbers5))
numbers5.reverse()
print('after reverse ', numbers5)
numbers5.sort()
print('after sorting ', numbers5)

numbers5.remove(5)
print(numbers5)
try:
    numbers5.remove(5)
except ValueError as e:
    print('value not exist ', e)

print('after remove ', numbers5)
del numbers5[2]
print('after del ', numbers5)
# del is used to delete an element from a list by its index
# remove is used to remove the first occurrence of a value from the list

numbers5[0] = 1
print(numbers5)
print('1 count in array is ', numbers5.count(1))
numbers5.clear()
print('after clear', numbers5)

objects = ['a', 'b', 1, 5.4]

for o in objects:
    print(o)