#01- Day

print("Hello World!")

"""
Creating the user define simple arthamitic operations
"""

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
action=input("Enter action (Add/minus/multi/divide): ")

if action=="add":
    print(f"add of {a} and {b} is : {a+b}")
elif action=="minus":
    print(f"add of {a} and {b} is : {a-b}")
elif action=="multi":
    print(f"add of {a} and {b} is : {a*b}")
elif action=="divide":
        if b==0:
            print("Zero is not dividable option, Please enter valid numebr")
            b=int(input("Enter the second number: "))
            print(f"add of {a} and {b} is : {a/b}")
else:
    print("Please enter the correct action (Add/minus/multi/divide) ")

