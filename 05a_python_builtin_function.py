# scientific_calculator.py

# import math

# while True:

#     print("\n==============================")
#     print("SCIENTIFIC CALCULATOR")
#     print("==============================")

#     print("1. Square Root")
#     print("2. Power")
#     print("3. Factorial")
#     print("4. Ceiling Value")
#     print("5. Floor Value")
#     print("6. Sine Value")
#     print("7. Logarithm")
#     print("8. Exit")

#     choice = input("Enter Choice: ")

#     if choice == "1":

#         number = float(input("Enter Number: "))
#         result = math.sqrt(number)

#         print("Square Root =", result)

#     elif choice == "2":

#         number = float(input("Enter Number: "))
#         power = float(input("Enter Power: "))

#         result = math.pow(number, power)

#         print("Result =", result)

#     elif choice == "3":

#         number = int(input("Enter Number: "))
#         result = math.factorial(number)

#         print("Factorial =", result)

#     elif choice == "4":

#         number = float(input("Enter Decimal Number: "))
#         result = math.ceil(number)

#         print("Ceiling Value =", result)

#     elif choice == "5":

#         number = float(input("Enter Decimal Number: "))
#         result = math.floor(number)

#         print("Floor Value =", result)

#     elif choice == "6":

#         angle = float(input("Enter Angle in Degrees: "))
#         radians = math.radians(angle)

#         print("Sine Value =", math.sin(radians))

#     elif choice == "7":

#         number = float(input("Enter Number: "))
#         print("Log Value =", math.log(number))

#     elif choice == "8":
#         print("Calculator Closed")
#         break

#     else:
#         print("Invalid Choice")



# lottery_system.py

# import random

# participants = [
#     "John",
#     "Mary",
#     "David",
#     "Sophia",
#     "Alex",
#     "Robert"
# ]

# while True:

#     print("\n=======================")
#     print("ONLINE LOTTERY SYSTEM")
#     print("=======================")

#     print("1. Generate Lucky Number")
#     print("2. Select Random Winner")
#     print("3. Generate OTP")
#     print("4. Shuffle Participants")
#     print("5. Exit")

#     option = input("Enter Choice: ")

#     if option == "1":

#         lucky_number = random.randint(1, 100)

#         print("Lucky Number =", lucky_number)

#     elif option == "2":

#         winner = random.choice(participants)

#         print("Winner =", winner)

#     elif option == "3":

#         otp = random.randint(100000, 999999)

#         print("OTP =", otp)

#     elif option == "4":

#         random.shuffle(participants)

#         print("\nParticipants Order")

#         for p in participants:
#             print(p)

#     elif option == "5":

#         print("Lottery Closed")
#         break

#     else:

#         print("Invalid Selection")
 
# attendance_system.py

# from datetime import datetime

# while True:

#     print("\n=========================")
#     print("EMPLOYEE ATTENDANCE SYSTEM")
#     print("=========================")

#     print("1. Current Date")
#     print("2. Current Time")
#     print("3. Current DateTime")
#     print("4. Mark Attendance")
#     print("5. Calculate Days")
#     print("6. Age Calculator")
#     print("7. Exit")

#     choice = input("Enter Choice: ")

#     if choice == "1":

#         today = datetime.now()

#         print("Date =", today.date())

#     elif choice == "2":

#         now = datetime.now()

#         print("Time =", now.time())

#     elif choice == "3":

#         now = datetime.now()

#         print("Date and Time =", now)

#     elif choice == "4":

#         employee = input("Employee Name: ")

#         login_time = datetime.now()

#         print(employee, "Login Time")
#         print(login_time)

#     elif choice == "5":

#         start_date = input(
#             "Enter Start Date (YYYY-MM-DD): "
#         )

#         end_date = input(
#             "Enter End Date (YYYY-MM-DD): "
#         )

#         d1 = datetime.strptime(
#             start_date,
#             "%Y-%m-%d"
#         )

#         d2 = datetime.strptime(
#             end_date,
#             "%Y-%m-%d"
#         )

#         difference = d2 - d1

#         print("Days =", difference.days)

#     elif choice == "6":

#         birth_date = input(
#             "Enter Birth Date (YYYY-MM-DD): "
#         )

#         dob = datetime.strptime(
#             birth_date,
#             "%Y-%m-%d"
#         )

#         today = datetime.now()

#         age = today.year - dob.year

#         print("Age =", age)

#     elif choice == "7":

#         print("Application Closed")
#         break

#     else:
#         print("Invalid Choice")
 