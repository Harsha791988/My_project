# user=int(input("Enter the number: "))

# if user<=1:
#     print("Not Prime number")
# else:
#     for i in range(2,int(user**0.5)+1): 
#         if user%i ==0:
#             print("Not Prime number")
#             break     
#     else:
#         print("Prime Number")

#prime number in range
prime=[]
non_prime=[]

for i in range(1,101):
     for j in range(2,int(i**0.5)+1):
            if i%j ==0:
                non_prime.append(i)
     else:
         prime.append(i)

print(prime)
print(non_prime)