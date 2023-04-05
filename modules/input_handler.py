# Module is a file that contains code to perform a specific task.

# import calculator
# from calculator import multiply_nums, add_nums
from somefolder.anotherfolder.test import test_func
from calculator import *

def main():
    first = input('Enter first number ')
    second = input('Enter second number ')
    print('add_nums ', add_nums(first, second))
    print('multiply_nums', multiply_nums(first, second))
    test_func()
main()


# Adding a directory to sys.path is not recommended in all cases, 
# especially if the directory contains untrusted code or if you are working with a large codebase. 
# In those cases, it is better to use virtual environments or package management tools like pip to manage your dependencies.