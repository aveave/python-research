class Shape:
    # parent class attribute
    name = 'shape'

    # parent class method
    # self - takes 0 positional arguments but 1 was given
    def print_name(self):
        print(f"Name is {self.name}")

    def print_letters_in_name(self):
        print('letters count in Shape is ', len(self.name))

# inherit from Shape
class Triangle(Shape):
    
    # name = 'triangle'
    
    # new method only in subclass
    def print_angles(self):
        print('triangle has 3 angles')
    
    # override print_letters_in_name in Shape class
    def print_letters_in_name(self):
        # super().print_letters_in_name()
        print('letters count in Triangle is ', len(self.name))

class Square(Shape):
    pass

# The pass statement is a placeholder that tells Python to do nothing. 
# This is useful when you need to define a code block that does not contain any statements, like an empty class.

triangle = Triangle()
triangle.name = 'triangle'
triangle.print_name()
triangle.print_angles()
triangle.print_letters_in_name()

square = Square()
square.name = 'square'
# use method from Shape class
square.print_letters_in_name()