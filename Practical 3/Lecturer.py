import Person
class Lecturer(Person.Person):
    def __init__(self, name, nric, staff_id):
        super().__init__(name, nric)
        self.__staff_id = staff_id
        self.__total_TeachingHour = int(input("What is your hour: "))
    def computeSalary(self):
        return self.__total_TeachingHour * 90
    def __str__(self):
        return f"{Person.Person.get_name(self)}, Staff Id: {self.__staff_id} earns ${Lecturer.computeSalary(self)}"