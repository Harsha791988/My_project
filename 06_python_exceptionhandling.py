# print("STUDENT AGE VALIDATION")

# try:

#     age = int(input("Enter Age: "))

#     print("Age Entered:", age)

# except ValueError:

#     print("Invalid Input.")
#     print("Please enter numeric values only.")

# print("Application Ended")

# print("EMPLOYEE SALARY CALCULATOR")


## data type error##

# try:

#     salary = 50000

#     bonus = "5000"

#     total_salary = salary + bonus

#     print("Total Salary:", total_salary)

# except TypeError:

#     print("Cannot perform operation on incompatible data types.")


## Index Error

# orders = [
#     "Laptop",
#     "Mobile",
#     "Printer"
# ]

# try:

#     index = int(
#         input("Enter Order Position: ")
#     )

#     print(
#         "Order:",
#         orders[index]
#     )

# except IndexError:

#     print(
#         "Order position does not exist."
#     )


## FIle handling ##

# try:

#     file = open(
#         "company_report.txt",
#         "r"
#     )

#     content = file.read()

#     print(content)

#     file.close()

# except FileNotFoundError:

#     print(
#         "Report file not found."
#     )


# print("BANKING SYSTEM")

# try:

#     amount = int(
#         input("Enter Amount: ")
#     )

#     result = 10000 / amount

#     print("Result:", result)

# except ZeroDivisionError:

#     print(
#         "Amount cannot be zero."
#     )

# finally:

#     print(
#         "Transaction Closed."
#     )


# try:

#     age = int(
#         input(
#             "Enter Employee Age: "
#         )
#     )

#     if age < 18:
#         raise ValueError(
#             "Employee must be at least 18 years old."
#         )

#     print(
#         "Employee Eligible"
#     )

# except ValueError as error:

#     print(
#         "Error:",
#         error
#     )

# try:

#     number = int(
#         input("Enter Number: ")
#     )

#     values = [10, 20, 30]

#     position = int(
#         input("Enter Position: ")
#     )

#     print(values[position])

# except ValueError:

#     print(
#         "Invalid Numeric Input."
#     )

# except IndexError:

#     print(
#         "Position Not Available."
#     )

# except Exception:

#     print(
#         "Unexpected Error Occurred."
#     )

# products = {
#     "Laptop": 50000,
#     "Mobile": 30000,
#     "Printer": 15000
# }

# try:

#     product = input(
#         "Enter Product Name: "
#     )

#     if product not in products:

#         raise ValueError(
#             "Product Not Available"
#         )

#     quantity = int(
#         input("Quantity: ")
#     )

#     total = (
#         products[product]
#         * quantity
#     )

#     print(
#         "Total Amount:",
#         total
#     )

# except ValueError as e:

#     print("Error:", e)

# except TypeError:

#     print("Invalid Data Type")

# finally:

#     print(
#         "Thank You For Visiting."
#     )
 
employees = {
    101: 50000,
    102: 60000,
    103: 70000
}

while True:

    print("\n========================")
    print("PAYROLL PROCESSING")
    print("========================")

    print("1. View Salary")
    print("2. Read Payroll File")
    print("3. Exit")

    choice = input("Enter Choice: ")

    try:

        if choice == "1":

            emp_id = int(
                input(
                    "Employee ID: "
                )
            )

            if emp_id not in employees:

                raise ValueError(
                    "Employee Not Found"
                )

            print(
                "Salary:",
                employees[emp_id]
            )

        elif choice == "2":

            file = open(
                "payroll.txt",
                "r"
            )

            print(file.read())

            file.close()

        elif choice == "3":

            print(
                "System Closed"
            )

            break

        else:

            raise ValueError(
                "Invalid Menu Option"
            )

    except ValueError as error:

        print(
            "ValueError:",
            error
        )

    except FileNotFoundError:

        print(
            "Payroll File Missing"
        )

    except TypeError:

        print(
            "Data Type Error"
        )

    except IndexError:

        print(
            "Index Error"
        )

    finally:

        print(
            "\nOperation Completed"
        )
 