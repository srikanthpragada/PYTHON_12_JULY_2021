class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __int__(self):
        return self.age


p1 = Player("Ronaldo", 34)
p2 = Player("Ronaldo", 34)
p3 = Player("Messi", 32)

print(p1)  # str(p1) ->  p1.__str__()
print(p1 == p2)  # p1.__eq__(p2)
print(p1 > p3)   # p1.__gt__(p3)

print(int(p1) + int(p3))