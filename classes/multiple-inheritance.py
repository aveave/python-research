class SuperClass1:
    def test_method(self):
        print('First super class')

class SuperClass2:
    def another_test_method(self):
        print('Second super class')
    # def test_method(self):
    #     print('Second super class')

class SubClass(SuperClass1, SuperClass2):
    pass

subclass = SubClass()
subclass.test_method()
subclass.another_test_method()

# show example when two super classes have same methods, change the order SuperClass2, SuperClass1

# show example when two super classes have same methods, change the order SuperClass2, SuperClass1

#if two superclasses have the same method name and the derived class calls that method, 
#Python uses the MethodResolutionOrder to search for the right method to call

# Python doesn't have a built-in keyword or syntax for defining interfaces like some other programming languages do. 