## write_employee.py

# file = open("employees.txt", "w")

# employee_id = input("Enter Employee ID: ")
# employee_name = input("Enter Employee Name: ")
# department = input("Enter Department: ")

# file.write("Employee ID: " + employee_id + "\n")
# file.write("Employee Name: " + employee_name + "\n")
# file.write("Department: " + department + "\n")

# file.close()

# print("Employee information saved successfully.")

# # read_employee.py

# file = open("employees.txt", "r")

# content = file.read()

# print("\nEmployee Information")
# print("--------------------")
# print(content)

# file.close()


# append_log.py

# file = open("employees.txt", "a")

# activity = input("Enter Activity: ")

# file.write(activity + "\n")

# file.close()

# print("Activity Saved Successfully")


## Read the data line by line

# file = open("attendance.txt", "r")

# print("Attendance Records")

# for line in file:
#     print(line.strip())

# file.close()
 
# #File Not Available 
# try:

#     file = open("salary_report.txt", "r")

#     print(file.read())

#     file.close()

# except FileNotFoundError:

#     print("Salary report file does not exist.")

# finally:

#     print("File operation completed.")

# try:

#     file = open("attendance.txt", "r")

#     print(file.read())

#     file.close()

# except FileNotFoundError:

#     print("Salary report file does not exist.")

# finally:

#     print("File operation completed.")



import csv

file = open("students.csv", "w", newline="")

writer = csv.writer(file)

writer.writerow([
    "RollNo",
    "Name",
    "Marks"
])

writer.writerow([
    "101",
    "John",
    "85"
])

writer.writerow([
    "102",
    "Mary",
    "92"
])

writer.writerow([
    "103",
    "David",
    "78"
])

file.close()

print("CSV File Created Successfully")




import csv

file = open(
    "students.csv",
    "a",
    newline=""
)

# writer = csv.writer(file)

# roll_no = input("Roll Number: ")
# name = input("Name: ")
# marks = input("Marks: ")

# writer.writerow([
#     roll_no,
#     name,
#     marks
# ])

# file.close()

# print("Student Added Successfully")


# import csv

# file = open("employees.csv", "r")

# reader = csv.DictReader(file)

# for employee in reader:

#     print("\nEmployee Information")

#     print(
#         "ID:",
#         employee["EmployeeID"]
#     )

#     print(
#         "Name:",
#         employee["Name"]
#     )

#     print(
#         "Department:",
#         employee["Department"]
#     )

#     print(
#         "Salary:",
#         employee["Salary"]
#     )

# file.close()

# import csv

# file = open(
#     "students.csv",
#     "r"
# )

# reader = csv.DictReader(file)

# total_marks = 0
# count = 0

# for student in reader:

#     total_marks += int(
#         student["Marks"]
#     )

#     count += 1

# average = total_marks / count

# print("Total Students:", count)

# print("Average Marks:", average)

# file.close()


# import csv

# while True:

#     print("\n========================")
#     print("PAYROLL MANAGEMENT")
#     print("========================")

#     print("1. Add Employee")
#     print("2. View Employees")
#     print("3. Add Payroll Entry")
#     print("4. View Payroll")
#     print("5. Exit")

#     choice = input("Enter Choice: ")

#     if choice == "1":

#         file = open(
#             "employees.txt",
#             "a"
#         )

#         emp_id = input(
#             "Employee ID: "
#         )

#         name = input(
#             "Employee Name: "
#         )

#         department = input(
#             "Department: "
#         )

#         file.write(
#             emp_id + "," +
#             name + "," +
#             department + "\n"
#         )

#         file.close()

#         print(
#             "Employee Added"
#         )

#     elif choice == "2":

#         try:

#             file = open(
#                 "employees.txt",
#                 "r"
#             )

#             print("\nEmployees")

#             print(file.read())

#             file.close()

#         except FileNotFoundError:

#             print(
#                 "Employee File Missing"
#             )

#     elif choice == "3":

#         file = open(
#             "payroll.csv",
#             "a",
#             newline=""
#         )

#         writer = csv.writer(file)

#         emp_id = input(
#             "Employee ID: "
#         )

#         salary = input(
#             "Salary: "
#         )

#         writer.writerow([
#             emp_id,
#             salary
#         ])

#         file.close()

#         print(
#             "Payroll Entry Added"
#         )

#     elif choice == "4":

#         try:

#             file = open(
#                 "payroll.csv",
#                 "r"
#             )

#             reader = csv.reader(file)

#             print("\nPayroll Records")

#             for row in reader:
#                 print(row)

#             file.close()

#         except FileNotFoundError:

#             print(
#                 "Payroll File Missing"
#             )

#     elif choice == "5":

#         print("System Closed")
#         break

#     else:

#         print("Invalid Choice")