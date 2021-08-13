class InvalidCourseError(Exception):
    def __init__(self, course):
        self.course = course

    def __str__(self):
        return f"Invalid Course --> {self.course}"


class Student:
    # Class attribute or static attribute
    fees = {'python': 6000, 'java': 8000, 'c#': 5000}
    taxrate = 12

    @staticmethod
    def getfee(course):
        base_fee = Student.fees[course]
        tax = base_fee * Student.taxrate / 100
        return base_fee + tax

    # Constructor
    def __init__(self, name, course, feepaid=0):
        # Object Attributes
        self.name = name
        if course not in Student.fees:
            raise InvalidCourseError(course)

        self.course = course
        self.feepaid = feepaid

    # Method
    def payment(self, amount):
        self.feepaid += amount

    def show(self):
        print(f"Name    : {self.name}")
        print(f"Course  : {self.course}")
        print(f"Feepaid : {self.feepaid}")

    def totalfee(self):
        return Student.getfee(self.course)

    def getdue(self):
        return self.totalfee() - self.feepaid

    @property
    def dueamount(self):
        return self.totalfee() - self.feepaid


if __name__ == '__main__':
    s1 = Student("Van", "aws")  # Create object
    s1.payment(3000)
    s1.payment(1000)
    # print(s1.feepaid)
    # s1.course = "java"
    s1.show()

    s2 = Student("Anders", "c#", 3000)
    print(s2.getdue())
    print(s2.dueamount)  # Property

    print(Student.getfee('c#'))
