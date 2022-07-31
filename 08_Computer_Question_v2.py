import random

first = random.randint(1, 100)
second = random.randint(1, 100)
answer = first + second

question = "{} + {} = ".format(first, second)
print(question)

run = True
while run :
    user_input = int(input("Enter number: "))
    if user_input == answer:
        print("correct!")
        print("Program continues")
        run = False
    elif user_input < answer:
        print("Incorrect! The correct answer is:", answer)
