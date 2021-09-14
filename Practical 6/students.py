class Student:
    def __init__(self, name, math, chinese, english, science):
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english
        self.science = science
        self.choices = ['SchoolA', 'SchoolB', 'SchoolC', 'None']
        self.allocation = ""
    def get_score(self):
        return (self.math + self.chinese + self.english + self.science) / 4
    def __str__(self):
        return f"({self.name})"
    def __repr__(self):
        return f"{self.name} scores {self.get_score}"
def load_result():
    students = []
    try:
        file_stuff = open('results.txt', "r")
        for x in file_stuff:
            p = x.strip("\n").split(",")
            students.append(Student(p[0], int(p[1]), int(p[2]), int(p[3]), int(p[4])))

    except IOError:
        print("File not found")
    return students

def main():
    students = load_result()
    m = sorted(students, key=lambda x: x.get_score(), reverse=True)
    for s in range(len(students)):
        m[s].allocation = m[s].choices[min(s//5, 3)]
        print(f"{m[s].name} scores {m[s].get_score()} and allocated {m[s].allocation}")

        #print(f"{s.name} scores {s.get_score()}, the choices are {', '.join(s.choices)}")



main()

import shelve


record ={}
db = shelve.open('storage.db', 'c')

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
    def __repr__(self):
        return f"Name: {self.__name}, Id: {self.__id}, Department: {self.__department}, Title: {self.__title}"
while 1:
    print("Select the program (1-6) to run:\n1. Search for an employee\n2. Add new employee\n3. Update employee details\n4. Delete an employee\n5. Display all employees \n6. Quit the program")
    while 1:
        try:
            command = int(input("Enter your command (1-6)"))
            break
        except ValueError:
            print("Invalid Choice!")


    if command == 1:
        try:
            print(record[input("Enter employee ID: ")])
        except KeyError:
            print("Invalid ID!")

    if command == 2:
        id = input("What is the new employee ID: ")
        record[id] = Employee(input("What is the new employee name: "), id, input("What is the new employee department: "), input("What is the new employee title: "))
        db['Info'] = record
    if command == 3:
        try:
            id = input("Enter employee id to change: ")
            yes = record[id]
            sets =  [input("What is the new name:(Leave empty to remain unchange): "), input("What is the new department (Leave empty to remain unchange: "), input("What is the new title? (Leave empty to remain unchage): ")]
            if sets[0] != "":
                record[id].set_name(sets[0])
            if sets[1] != "":
                record[id].set_department(sets[1])
            if sets[2] != "":
                record[id].set_title(sets[2])
            db['Info'] = record
            print(f"Employee: {record[id].get_id()} title updated")
        except KeyError:
            print("Invalid ID!")
    if command == 4:
        try:
            del record[input("What employee would you like to delete (ID): ")]
            db['Info'] = record
        except KeyError:
            print("Invalid Employee!")
        
    if command == 5:
        record = db['Info']
        for x in record:
            print(f"{record[x].get_name()} (id={record[x].get_id()}) is a {record[x].get_title()} from {record[x].get_department()} department")

    if command == 6:
        break
record = db['Info']
print(record)

db.close()

