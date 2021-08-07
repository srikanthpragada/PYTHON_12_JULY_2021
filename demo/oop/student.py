class Student:
    # Constructor
    def __init__(self, name, course, feepaid=0):
        # Object Attributes
        self.name = name
        self.course = course
        self.feepaid = feepaid

    # Method
    def payment(self, amount):
        self.feepaid += amount

    def show(self):
        print(f"Name    : {self.name}")
        print(f"Course  : {self.course}")
        print(f"Feepaid : {self.feepaid}")

    def getdue(self):
        pass


if __name__ == '__main__':
    s1 = Student("Van", "python")  # Create object
    s1.payment(3000)
    s1.payment(1000)
    # print(s1.feepaid)
    # s1.course = "java"
    s1.show()

    s2 = Student("Anders", "c#", 3000)
