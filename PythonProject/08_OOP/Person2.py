class Person:
    # 속성(property)
    eyes = 2
    nose = 1
    mouth = 1
    ears = 2
    arms = 2
    legs = 2

    # 메소드(method)
    def dat(self):
        print('냠냠냠...')

    def sleep(self):
        print('쿨쿨쿨...')

    def talk(self):
        print('주저리.. 주저리..')

class Student(Person):
    def study(self):
        print('열공.. 열공..')

chan = Student()
print(chan.eyes)
print(chan.nose)
chan.sleep()
chan.study()


