# marks=90

# if marks>=90:
#     grade="A+"
# elif marks >=75:
#     grade="B"

# print(f"Grade :{grade}")

# age=int(input("Enter the age: "))
# citizenship=input("Enter the Country:")
# if age>=18:
#     if citizenship=="India":
#         print("Eligible for the Voting")
#     else:
#         print("Your Not Belong from India not eligible for the Voting")
# else:
#     print("Your age is not eligible for voting")

# fruits=["Apple","Banana","Mango"]
# print(type(fruits))
# for fruit in fruits:
#     print(fruits)

# print(fruits[0])

# total=0
# for num in range(1,6):
#     total +=num
# print(total)

## Ennumerate: give the index and value
 
# fruits=["Apple","Banana","Mango"]

# for index, fruit in enumerate(fruits):
#     print(f"{index} :{fruit}")

## while loop

# count=1
# while count <=5:
#     print(count)
#     count +=1

# print(count)

## break statement
# total=0
# for num in range(1,11):
#     total +=num
#     if total >= 15:
#         print(f"num:{num}")
#         break
# print(f"total:{total}")

## continue Statement

# for num in range(1,6):
#     if num==4:
#         continue
#     print(num)
# print(num)

## pass statement

# for num in range(1,6):
#     if num==4:
#         pass
#     print(num)
# print(num)# Final Number

# total=0
# while total <=5:      
#     if total==3:
#         total +=1
#         continue
#     print(total)
#     total +=1
#     if total >100:
#         break

students = [
    
    {"name": "Amit", "marks": 92},
    {"name": "Riya", "marks": 78},
    {"name": "Karan", "marks": 35},
    {"name": "Neha", "marks": 65},
    {"name": "Stop", "marks": 0}
]

for student in students:

    if student["name"] == "Stop":
        break # stop execution

    marks = student["marks"]

    if marks < 40:
        print(student["name"], "- Failed")
        continue #skip that iterations

    if marks >= 90:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    else:
        grade = "C"

    if grade == "A+":
        print(student["name"], "- Excellent")
    else:
        pass #Nothing 

    print(student["name"], "- Grade:", grade)
 