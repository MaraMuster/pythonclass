#bundesland = input("Bundesland? ")
#if bundesland == "Berlin" :
#    print("Die Hauptstadt ist Berlin")
#if bundesland == "Brandenburg":
#    print("Die Hauptstadt ist Potsdam")

# bei if werden alle Bedingungen geprüft, auch wenn diese sich gegenseitig ausschließen!
# Die Lösung, um diesem Problem aus dem Weg zu gehen: elif benutzen (else if)

# Ein weiterer Nachteil ist das Nichtreagieren auf unerwartete Eingaben.
# Lösung: else

bundesland = input("Bundesland? ")
if bundesland == "Berlin" :
    print("Die Hauptstadt ist Berlin")
elif bundesland == "Brandenburg":
    print("Die Hauptstadt ist Potsdam")
elif bundesland == "Niedersachsen":
    print("Hannover")
else:
    print("Dieses Bundesland kenne ich nicht (falls es überhaupt eins ist)")
