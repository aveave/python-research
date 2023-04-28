class Person:

    age = 10
    # self - ссылка не текущий объект
    def get_age(self):
        print('get age')
        return self.age


test_person = Person()
print('age is ', test_person.get_age())

