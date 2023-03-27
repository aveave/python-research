# отступы важны! регистрозависимый print Print
# Camel case Underscore notation чащу второе
# Python динамическая типизация, переменные не привязаны к типу
# Логические операции and or not in
# как создать функцию def
# 
# if else / if elif 
#
#
# types bool , int, float p=3.14, complex, str
# str можно в многострочный контекст

# loops continue and break exists
# num = 1
# while num < 5:
#     print(num)
#     num += 1
# print('end')

nums = [1, 2, 3, 4, 5]
for number in nums:
    if (number == 3):
        print('break')
        break
    print(number)

# first declare function, then call it
# put_string_inside()

def put_string_inside():
    first = 'str'
    second = 'second'
    print(type(second))
    result = f"first value is {first} and second is {second}"
    print(result)


# default values in functions + pass value by variable name

def test_function(first, second=10):
    print('first', 'second', 'third')
    print('first' + 'second')
    if first < second:
        print('second is bigger ', second)
    elif first > second:
        print('first is bigger', first)
    else:
        print('first equals to second', first, second)
    
test_function(second=3, first=7)

# lambda

def test_lambda(first, second, mode):
    sum = lambda x, y: x + y
    multiply = lambda x, y: x * y

    match mode:
        case 'sum':
            print(sum(first, second))
        case 'multiply':
            print(multiply(first, second))
        case _:
            raise Exception('Unknown mode')

def test_lambda_new(first, second, operation):
    print(operation(first, second))

test_lambda(2, 3, 'sum')
test_lambda(2, 3, 'multiply')
#exception can be custom, but we need to cover class topic to do it
test_lambda(2, 3, 'test')

test_lambda_new(2, 4, lambda x, y: x * y)
test_lambda_new(2, 4, lambda x, y: x + y)

# Преобразование типов int() float() str()
# читаем из файла, разбираем json

def test_type_conversion():
    first = '2'
    second = 3
    print('result ', first + str(second))
    print(second + int(first))

test_type_conversion()

# variables global and local
test = 'HI'
def say1():
    print(test)

def say2():
    print(test)

say1()
say2()