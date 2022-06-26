import random

mathquiz_list = ["5 x 6 = ", "8 x 12 = ", "12 - 15 =", "-51 - 25 =", "144 / 2 = ", "xxx"]

for item in range (0,20):
    comp_choice = random.choice(mathquiz_list[:-1])

print(comp_choice, end="\t")