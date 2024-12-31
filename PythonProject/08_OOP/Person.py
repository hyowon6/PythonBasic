class Person:
    # 적어두는 게 참조할 때 편함
    fname = ''
    lname = ''

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname, year):
        # Person에 있는 것 끌어와서 사용
        # Person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        # 속성 추가
        self.graduationyear = year

    def welcome(self):
        print('Welcome to My Server - %s %s(%d)' % (self.lname, self.fname, self.graduationyear) )


xman = Student('SeoungChan', 'Baik', 2019)
xman.printname()

print(xman.graduationyear)
xman.welcome()

