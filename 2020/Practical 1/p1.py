#

class Pet:
    def __init__(self, name, type, age):
        self.__name = name
        self.__animal_type = type
        self.__age = age
    def change_name(self, name):
        self.__name = name
    def change_type(self, type):
        self.__animal_type = type
    def change_age(self, age):
        self.__age = age
    def age(self):
        return self.__age
    def type(self):
        return self.__animal_type
    def name(self):
        return self.__name
    def __str__(self):
        return f"Pet {self.__name} is a {self.__animal_type} and it is {self.__age} years old"

try:
    print(Pet(input("Enter pet name: "), input("Enter pet type: "), int(input("Enter age of pet: "))))
except ValueError:
    print('Invalid Age!')


def is_valid(id):
    return len(id) == 5 and id[-1].isalpha() and id[0:4].isdigit()


class Customer:
    def __init__(self, customer_id, name):
        self.__customer_id = customer_id
        self.__name = name
    def change_id(self, customer_id):
        self.__customer_id = customer_id
    def change_name(self, name):
        self.__name = name
    def name(self):
        return self.__name
    def customer_id(self):
        return self.__customer_id
    def display_details(self):
        return f"{5 * '=' + 'Customer Details' + 5 * '='}\nCustomer ID: {self.__customer_id}\nCustomer Name: {self.__name}"



while 1:
    id = input("What is the Customers' ID: ")
    if is_valid(id):
        Customer(id, input("What is the Customers' name: "))
        break
    else:
        print("Invalid ID! Try again.")


class BankAccount:
    def __init__(self, account_number, balance = 0, interest_rate = 0.0):
        self.__account_number = account_number
        self.__balance = balance
        self.__interest_rate = interest_rate
    def get_interest_rate(self):
        return self.__interest_rate
    def get_interest(self):
        return self.__balance * (1 + self.__interest_rate/12)**12
    def deposit(self):
        self.__balance += float(input("How much do you want to deposit? "))
    def withdraw(self):
        if self.__balance == 0:
            return "You have insufficient amount to withdraw!"
        withdrawal = float(input("How much do you want to withdraw?"))
        if withdrawal > self.__balance:
            return "You have insufficient amount to withdraw"
        else:
            self.__balance -= withdrawal
            return "ok"
    def get_account_balance(self):
        return self.__balance
    def get_account_number(self):
        return self.__account_number
class SavingsAccount(BankAccount):
    def __init__(self, account_number):
        super().__init__(account_number, 0, 0.01)
class CurrentAccount(BankAccount):
    def __init__(self, account_number):
        super().__init__(account_number, 0, 0.005)
x = input("Enter account number: ")
if len(x) == 11 and x[2] == "-" and x[8] == '-' and x[0] in ['1','0'] and x.replace("-", "").isdigit():
    if x[0] == '1':
        o = SavingsAccount(x)
        o.withdraw()
        o.deposit()
    elif x[0] == '0':
        o = CurrentAccount(x)
    print(f"Your account number is {o.get_account_number()}\n{o.withdraw()}\nAccount Balance: {o.get_account_balance()}\nAccount interest rate is {o.get_interest_rate()}\nThe interest rate earned is {o.get_interest()}")
else:
    print("Invalid!")
