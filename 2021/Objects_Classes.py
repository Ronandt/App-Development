class Customer:
    def __init__(self, name = None, email = None, mobile_number = None):
        self.__name = name
        self.__email = email
        self.__mobile_number = mobile_number
    def set_name(self, name):
        self.__name = name
    def set_email(self, email):
        self.__email = email
    def set_mobile_number(self, mobile_number):
        self.__mobile_number = mobile_number
    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def get_mobile_number(self):
        return self.__mobile_number
    def get_customer_info(self):
        return f"Name: {self.__name} | Email: {self.__email} | Mobile Number: {self.__mobile_number}"
    def __str__(self):
        return f"Name: {self.__name}\nEmail: {self.__email}\nMobile Number: {self.__mobile_number}"
print(Customer(input("enter your name: "), input("Enter your email: "), input("Enter your mobile number: ")))



class Phone:
    counting = 0
    def __init__(self, make = None, model = None, price = None, phone_id = None):
        self.__make = make
        self.__model = model
        self.__price = Phone.set_price(self, price)
        self.__class__.counting += 1
        self.__id = phone_id
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_price(self):
        return self.__price
    def set_make(self, make):
        self.__make = make
    def set_model(self, model):
        self.__model = model
    def set_price(self, price):
        print("Price should be in numbers." * (not price.isdigit()))
        if price.isdigit():
            self.__price = price
            return self.__price # prevent recursive
        self.__price = "None"
        return "None"
    def get_phone_info(self):
        return f"Ok bruh what is this "
    def __str__(self):
        return f"The price of {self.__make + self.__model} is ${self.__price}. Now has {Phone.counting} phone in total\n" * (Phone.get_price(self).isdigit())


phoni = Phone(input("Enter the make of the phone: "), input("Enter the model of the phone: "), input("Enter the price of the phone: "))
print(phoni)



class SalesPerson:
    def __init__(self, name = "None", commission = 0, phony = None): #whenever you want to use another class and that is inputted from initalization, use None
        self.__name = name
        self.__commission = commission
        self.__phony = phony
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def salesperson_sold(self, phony):
        self.__phony = phony
    def salesperson_commission(self, payment_received):
        self.__payment_received = payment_received * 0.2
        return str(self.__payment_received)

    def __str__(self):
        return f"\nSalesperson {self.__name} sold {self.__phony.get_make() + self.__phony.get_model()} at ${self.__phony.get_price()} and earned a commission of ${float(SalesPerson.salesperson_commission(self, int(self.__phony.get_price()))):.2f}"
print(SalesPerson(input("Enter the salesperson name: "), int(input("Enter paymnet received by salesperson: ")), phoni))




dicts = {}

while 1:
    print("Select the program (1-5) to run:\n1. Search for a phone\n2. Add a new phone\n3. Update phone details\n4. Delete a phone\n5. Quit the program")
    while 1:
        try:
            choice = int(input("Enter your command (1-5): "))
            break
        except ValueError:
            pass
    if choice == 1:
        try:
            print(dicts[input("What is the phone number you want to search: ")])
        except KeyError:
            print("There is no such phone number")
    if choice == 2:
        id = input("Enter phone id: ")
        dicts[id] = Phone(input("Enter the make of the phone: "), input("Enter the model of the phone: "), input("Enter the price of the phone: "), id)
    if choice == 3:
       try:
            dicts[input("Enter phone id to update: ")] = Phone(input("Enter the make of the phone: "), input("Enter the model of the phone: "),
                  input("Enter the price of the phone: "))
       except KeyError:
           print("No such phone id")
    if choice == 4:
        try:
            del dicts[input("Enter phone id to delete: ")]
        except KeyError:
            print("No such phone id to delete")
    if choice == 5:
        break
