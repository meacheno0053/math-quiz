import random

secret = random.randint()
print("Spoler Alert", secret, answer)

run = True
while run : 
    user_input = int(input("Enter number: "))
    if user_input == answer :
        print("you won!")
        run = False