import random
rand_int=random.randint(1,100)

counter=0

while True:
    user_input=int(input("Enter the guessing number 1 to 100: "))
    counter +=1    
    if user_input==rand_int:
        print(f"Congrats!, you have guess the number correctly in {counter} tries")
        break    
    elif user_input<rand_int:
        print("You entered a number below random number.Try Again ")
    elif user_input>rand_int:
        print("You entered a number above random number.Try Again")
    else:
        print("You are enter the ")