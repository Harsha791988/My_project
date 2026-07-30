# without list comprehension

# nums=[1,2,3,4,5]
# sqrs=[]
# for num in nums:
#     sqrs.append(num**2)
# print(sqrs)

# Using list comprehension

# nums=[1,2,3,4,5]
# sqrs=[num ** 2 for num in nums]
# print(sqrs)

# names=["harsha","Raju","Ravi"]
# upper_name=[name.upper() for name in names]
# print(upper_name)

# numbers=range(1,11)
# even_number=[n for n in numbers if n%2==0]
# print(even_number)
# odd_number=[n for n in numbers if n%2 !=0]
# print(odd_number)

# numbers = [1, 2, 3, 4, 5]

# result = ["Even" if n % 2 == 0 else "Odd" for n in numbers]

# print(result)

# numbers=[10,-5,20,-8,30]
# results=[n if n >=0 else 0 for n in numbers]
# print(results)

# l1=["a","b","c"]
# l2=[1,2,3]
# new_list=[]
# for n in l1:
#     for i in l2:
#         new_list.append(f"{n},{i}")
# print(new_list)

# pairs=[(i,j) for i in l1 for j in l2]
# print(pairs)

# word="python"
# chars=[ch for ch in word]
# print(chars)

word="programs"

chars=[ch for ch in word if ch.lower() in ("a","e","i","o","u")]
print(chars)

files = ["report.pdf", "image.jpg", "data.xlsx", "notes.pdf"];
pdf_files = [file for file in files if file.endswith(".pdf")];
print(pdf_files);

students = [
    {"name": "Amit", "marks": 92},
    {"name": "Riya", "marks": 78},
    {"name": "Karan", "marks": 35},
    {"name": "Neha", "marks": 65}
];

results = [
    f"{student['name']} - Pass"
    if student["marks"] >= 40
    else f"{student['name']} - Fail"
    for student in students
];

print(results);
