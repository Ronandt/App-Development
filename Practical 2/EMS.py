record ={}
class Employee:
    def __init__(self, name, id, department, title):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__title = title
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_department(self):
        return self.__department
    def get_title(self):
        return self.__title
    def set_name(self, name):
        self.__name = name
    def set_id(self, id):
        self.__id = id
    def set_department(self, department):
        self.__department = department
    def set_title(self, title):
        self.__title = title
    def __str__(self):
        return f"Name: {self.__name}, Id: {self.__id}, Department: {self.__department}, Title: {self.__title}"
while 1:
    print("Select the program (1-5) to run:\n1. Search for an employee\n2. Add new employee\n3. Update employee details\n 4. Delete an employee\n5. Quit the program")
    command = int(input("Enter your command (1-5)"))
    if command == 1:
        try:
            print(record[input("Enter employee ID: ")])
        except KeyError:
            print("Invalid ID!")
    if command == 2:
        id = input("What is the new employee ID: ")
        record[id] = Employee(input("Wat is the new employee name: "), id, input("What is the new employee department: "), input("What is the new employee title: "))
    if command == 3:
        try:
            id = input("What is the employee you want to edit (ID): ")
            record[id] = Employee(input("Edit name: "), id, input("Edit department: "), input("Edit title: "))
        except KeyError:
            print("Invalid ID!")
    if command == 4:
        del record[input("What employee would you like to delete (ID): ")]
    if command == 5:
        break
