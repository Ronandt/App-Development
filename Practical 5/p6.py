#1a) If someone inputs a string or a float to the input (count/num), there will be a ValueError and the program will crash
import sys
try:
    count = int(input("How many numbers do you want to capture?"))
    numList = []
    for i in range(count):
        msg = 'Enter number #' + str(i + 1)
        num = int(input(msg))
        numList.append(num)
    print("The lowest number in the list:'", min(numList))
    print("The highest number in the list:", max(numList))
    print("The total of the number in the list:", sum(numList))
    print("The average of the number in the list:", sum(numList)/len(numList))
except ValueError:
    print("Please input the correct data type in the input!")
except:
    print("Oops something unexpected happened")\

#2)
while True:
    name = input("Enter name: ")
    while 1:
        try:
            weight = float(input("Enter weight(kg): "))
            if weight <= 0:
                print("Weight cannot be negative!")
            break
        except ValueError:
            print("Input the correct data type!")
    while 1:
        try:
            height = float(input("Enter height (m): "))
            if height <= 0:
                print("Height cannot be negative!")
            break
        except ValueError:
            print("Input the correct data type!")
    try:
        bmi = weight/height**2
        print(bmi)
    except ZeroDivisionError:
        print("Cannot be divded by zero!")
        sys.exit()

    command = input("Store your bmi to file? (Y/N): ").upper().strip()
    try:
        if command == "Y":
            bmi_File = open("bmi.txt", 'a')
            bmi_File.write(name + ',' + str(bmi) + '\n')
            bmi_File.close()

        command = input("Do you want to continue? (Y/N): ")
        if command.upper() == "N":
            break
        command = input("Do you want to view BMI record in file? (Y/N): ").upper().strip()
        if command == "Y":
            bmi_File = open('bmi.txt','r')
            contents = bmi_File.read()
            print(contents)
            bmi_File.close()
            print("End of program")
    except IOError:
        print("An error has occured attempting to reaD")