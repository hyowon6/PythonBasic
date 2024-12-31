
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        print("Hello", self.name)
        print("I'm %s years old." % self.age)

p1 = Person('Chan', 28)
print(p1.name, p1.age) # Chan 28
p1.myfun()

# Hello Chan
# I'm 28 years old.