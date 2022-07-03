show_instructions = ""
while show_instructions.lower() != "xxx":
    show_instructions = input ("Have you played before?? ").lower()

    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("< Program continues >")

    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("< Display instructions >")

    else:
        print("Please answer yes / no")