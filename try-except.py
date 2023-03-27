first = input('Write a first number ')
second = input('Write a second number ')

try:
    print(int(first) + int(second))
# except ValueError:
except ValueError as er:
    print('User provided wrong numbers', er)