my_lucky_number = 42

guess = int(input("Gib eine Zahl ein: "))

if my_lucky_number < guess:
    print("Die Zahl ist zu groß!")
elif my_lucky_number == guess:
    print("Du hast die Zahl erraten!")
else:
    print("Die Zahl ist zu klein!")
