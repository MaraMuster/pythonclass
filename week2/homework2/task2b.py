my_num = 42

# questions = int(input("Wie oft möchtest du gefragt werden? "))
your_num = int(input("Nummer? "))


while your_num!=my_num:
    print("Falsch!")
    your_num= int(input("Nummer? "))

    if your_num == my_num:
      print("Richtig geraten!")
