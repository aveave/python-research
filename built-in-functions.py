# zip(): The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it. (combine)

fruits = ['apple', 'orange', 'lemon']
prices = [100, 200, 300]

result = zip(fruits, prices)
print(list(result))

# unzip
data = [('apple', 100), ('orange', 200), ('lemon', 300)]

fruits1, prices1 = zip(*data)
print(f"fruits1 {fruits1}")
print(f"prices1 {prices1}")


# If we use a different number of variables and values in a tuple unpacking operation, 
# then we'll get a ValueError. That's because Python needs to unambiguously know what value goes into what variable, 
# so it can do the assignment accordingly.



# enumerate(): Used to loop over a sequence and keep track of the index.

# all(): Used to check if all elements in a sequence are True.

# any(): Used to check if at least one element in a sequence is True.