# множество хранит только уникальные элементы
# set is an unordered collection of unique elements.
fruits = {'a', 'e'}
fruits1 = set()

fruits.add('a')
fruits.add('b')
fruits.add('c')
fruits.add('b')

fruits.remove('a')
fruits.discard('x') # discard(), который не будет генерировать исключения при отсутствии элемента
# fruits.remove('x')
print(fruits)
print(len(fruits))
fruit_busket1 = { 'orange', 'lemon', 'apple', 'strawberry', 'melons', 'berries'}

fruit_busket2 = { 'orange', 'lemon', 'apple', 'strawberry', 'cherry'}

print('first busket difference is ', fruit_busket1.difference(fruit_busket2))
print('second busket difference is ', fruit_busket2.difference(fruit_busket1))
print('union ', fruit_busket1.union(fruit_busket2))
print('intersection is ', fruit_busket1.intersection(fruit_busket2))
print('is second busket subset of first ', fruit_busket2.issubset(fruit_busket1))
print('is first busket superset of second ', fruit_busket2.issuperset(fruit_busket1))

print('fruit busket 1 before ', fruit_busket1)
print('fruit busket 2 before ', fruit_busket2)
# intersection_update() заменяет пересеченными элементами первое множество
fruit_busket1.intersection_update(fruit_busket2)

print('fruit busket 1 before ', fruit_busket1)
print('fruit busket 2 before ', fruit_busket2)

#frozenset
my_set = {1, 2, 3}
my_frozenset = frozenset(my_set) # an immutable set
print(my_frozenset) # output: frozenset({1, 2, 3})
#my_frozenset.add(4)  AttributeError: 'frozenset' object has no attribute 'add'
print(my_frozenset)