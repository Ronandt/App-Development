import Person
class Student(Person.Person):
    def __init__(self, name, nric, admin_no):
        self.__admin_no = admin_no
        Person.Person.__init__(self, name, nric)
        while 1:
            try:
                self.__test_mark = float(input("Enter your test mark: "))
                if self.__test_mark >= 0:
                    break
            except ValueError:
                pass
        while 1:
            try:
                self.__exam_mark = float(input("Enter your exam mark: "))
                if self.__exam_mark >= 0:
                    break
            except ValueError:
                pass
    def get_admin_no(self):
        return self.__admin_no
    def set_admin_no(self, admin_no):
        self.__admin_no = admin_no
    def computeFinalMark(self):
        return (self.__test_mark + self.__exam_mark) / 2
    def __str__(self):
        return f"{Person.Person.get_name(self)}, Admin No: {self.__admin_no} final mark is {Student.computeFinalMark(self):.2f}"