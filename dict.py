# a dictionary is a collection of key-value pairs.
dictionary = {}
dictionary1 = dict()

print(dictionary)
print(dictionary1)

dictionary = {1 : 'Apple', 2 : 'Orange', 3 : 'Banana'}
print(dictionary)
# обращение по ключу | KeyError: 0 if key doesn't exist
print('Value by key 1 is ', dictionary[1])
dictionary[1] = 'Lemon'
dictionary[4] = 'Strawberry'
print(dictionary)

# delete
#The main difference between del and pop is that del simply removes 
# the key-value pair from the dictionary, without returning any value, 
# while pop removes the key-value pair and returns the value that was 
# associated with the key.

del dictionary[1]
print('remove element by key 2 ', dictionary.pop(2))
print('After deleting element with 1 and keys ', dictionary)
# Put all keys of `dictionary` in a list and returns the list
print(dictionary.keys())
# Put all values saved in `dictionary` in a list and returns the list
print(dictionary.values())

# two same keys

dic = {'apple' : 10, 'orange': 20, 'lemon': 30, 'apple': 40}
print('with two apple keys', dic)

# перебор элементов 2 способа
for key, value in dictionary.items(): # items() возвращает набор кортежей
    print('key is ', key, ' value is ', value)
for key in dictionary:
    print('key is ', key, ' value is ', dictionary[key])


# dictionary comprehension
# Dictionary comprehension is a powerful concept and can be used to substitute for loops and lambda functions. 
newdic = {key : value * 2 for (key, value) in dic.items()}
print(newdic)

# conditions can be added
newdic = {key:value * 2 for (key, value) in dic.items() if value > 20}
print(newdic)

fruits = ['apple', 'lemon', 'orange']
fruit_dic = {fruit: len(fruit) for fruit in fruits}
print(fruit_dic)