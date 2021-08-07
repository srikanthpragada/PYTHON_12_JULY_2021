class Person:
    def __init__(self, name, mobile):
        self.__name = name
        self.__mobile = mobile


p1 = Person("Abc", "3943938393")
p1.email = "abc@gmail.com"
print(p1.__dict__)
print(p1._Person__mobile)
p1.email = "abc@gmail.com"
