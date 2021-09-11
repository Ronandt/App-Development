class Employee:
    def __init__(self, name, id, department, title):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__title = title
    def __str__(self):
        return f"Name: {self.__name}, Id: {self.__id}, Department: {self.__department}, Title: {self.__title}"


print(Employee('John Tee', 'jtee', 'Accounting', 'President'))
