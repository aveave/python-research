# In Python, a decorator is a design pattern that allows you to modify the functionality of a function 
# by wrapping it in another function.

# The outer function is called the decorator, which takes the original function as an argument 
# and returns a modified version of it.

# everything in Python is an object, even functions are objects.

# Basically, a decorator takes in a function, adds some functionality and returns it.

def outer_func():
    # print('inside outer')
    def inner_func():
        print('inside inner func')
    return inner_func
outer = outer_func()
outer()

# def before_after(inner_func):
    
#     def before_after():
#         print('before')
#         inner_func()
#         print('after')
#     return before_after

# @before_after
# def test_func():
#     print('main logic')

# test_func()