import json


class Student:
    # Constructor
    def __init__(self, name, course):
        # Object Attributes
        self.name = name
        self.course = course


s1 = Student("Van", "aws")  # Create object
print(s1.__dict__)
print(json.dumps(s1.__dict__))
