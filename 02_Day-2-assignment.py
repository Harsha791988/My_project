##	Area calculator (Rectangle, Circle, Triangle)

# print("Find out the area Rectangle ,Circle ,Triangle ")
# print("1.Rectangle")
# print("2.Circle")
# print("3.Triangle")

# action=input("Enter the shape to calculate area: ")

# if action=="Rectangle":
#     length=int(input("Enter the length: "))
#     width=int(input("Enter the width: "))
#     print(f"Rectangle area length {length} and width {width} : {length*width}")
# elif action=='Triangle':
#     base=int(input("Enter the Base: "))
#     height=int(input("Enter the Height: "))
#     print(f"Triangle area Base {base} and height{height}: {12*base*height}")
# elif action=="Circle":
#     r=int(input("Enter the r: "))
#     print(f"Circle area : {3.14159*(r**2)}")
# else:
#     print("Enter the invalid action!")

# # Currency converter ($ -> ₹, ₹ -> $)
# print("Currency converter ($ -> ₹, ₹ -> $)")
# print("1. Dollar to Rupee")
# print("2. Rupee to Dollar")

# action=input("Enter Currency Type : ")

# if action=="1":
#     dollar=int(input("Enter the dollars : "))
#     print(f"Dollar {dollar} convert to Rupees: {dollar*96}")
# elif action=="2":
#     rupee=int(input("Enter the rupees: "))
#     print(f"{rupee} rupees covert to Dollars: {rupee/96}")
# else:
#     print("Invalid Action1")

## Employee Salary Calculator

Employee_Name=input("Enter the Employee Name: ")
Basic_Salary=float(input("Enter the Basic Salary: "))
Bonus_Amount=float(input("Enter the Bonus Amount: "))
Total_Salary=Basic_Salary+Bonus_Amount
if Total_Salary >=10000:
    High_Earner =True
else: 
    High_Earner =False
print(f"Employee Name {Employee_Name} ,\nBasic Salary: {Basic_Salary} , \nBonus amoun: {Bonus_Amount} , \nTotal Salary:{Total_Salary} ,\nHigh Earner : {High_Earner}")