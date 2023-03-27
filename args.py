# With *args you can create more flexible code that accepts a varied amount of non-keyworded arguments within your function.
# The double asterisk form of **kwargs is used to pass a keyworded, variable-length argument dictionary to a function.


#Using **kwargs provides us with flexibility to use keyword arguments 
# in our program. When we use **kwargs as a parameter, we don’t need to know 
# how many arguments we would eventually like to pass to a function.

#While you can pass a dictionary instead of using **kwargs, 
# using **kwargs can offer more flexibility in terms of how keyword arguments 
# can be passed to a function.

#Always place the **kwargs parameter at the end of the parameter list, or you’ll get an error.

# pass additional keyword arguments that are not in the dictionary.

def test_kwargs(**kwargs):
    print('City first ', kwargs['city'])
    for k, v in kwargs.items():
        print('key is ', k, ' value is ', v)

# test_kwargs(apple=1, banana=2)

dictionary = {'apple': 1, 'banana': 2, 'lemon': 3}
#**my_dict to unpack the dictionary, followed by additional keyword argument city
test_kwargs(**dictionary, city='Astana')

# args

def test_args(*args):
    for n in args:
        print('number is ', n)

def my_function(my_list, arg1, arg2):
    print(my_list)
    print(arg1)
    print(arg2)

my_list = [1, 2, 3]
my_function(my_list, 4, 5)