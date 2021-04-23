from 클래스만들기.사람모듈 import *

class Student(Person):
    
    def study(self):
        print('공부')
    
    def __init__(self, name, age):
        Person.__init__(self, name, age)

class Worker(Person):

    def work(self):
        print('일')

    def __init__(self, name, age):
        Person.__init__(self, name, age)

if __name__ == '__main__':
    student_man = Student('name1',26)
    student_man.study()
    print(student_man)

    work_man = Worker('name2', 29)
    work_man.work()
    print(work_man)