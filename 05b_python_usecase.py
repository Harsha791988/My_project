import math
import random
from datetime import datetime

employees = []

while True:

    print("\n=================================")
    print("EMPLOYEE REWARD MANAGEMENT")
    print("=================================")

    print("1. Register Employee")
    print("2. Calculate Bonus")
    print("3. Mark Attendance")
    print("4. Lucky Draw Winner")
    print("5. Exit")

    choice = input("Select Option: ")

    if choice == "1":

        name = input("Employee Name: ")

        employees.append(name)

        print("Employee Registered")

    elif choice == "2":

        salary = float(
            input("Enter Salary: ")
        )

        bonus_percentage = 15

        bonus = math.ceil(
            salary * bonus_percentage / 100
        )

        print("Bonus Amount =", bonus)

    elif choice == "3":

        employee = input(
            "Employee Name: "
        )

        attendance = datetime.now()

        print(employee)
        print("Attendance Marked At")
        print(attendance)

    elif choice == "4":

        if len(employees) > 0:

            winner = random.choice(
                employees
            )

            prize_number = random.randint(
                1000,
                9999
            )

            print("\nWinner =", winner)
            print(
                "Prize Number =",
                prize_number
            )

        else:

            print(
                "No employees registered"
            )

    elif choice == "5":

        print("System Closed")
        break

    else:

        print("Invalid Choice")