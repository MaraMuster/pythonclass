names = ["Dina", "Dana","Dora"]

for i in names:
    print(i)

print(" ")

for i in [0,1,2]:
    print(names[i])

print(" ")
### was ist bei n Elementen in einer Liste?

for i in range(len(names)):
    print(names[i])

print(" ")

geo = ["Bamberg", "Nürnberg", "Saarbrücken", "Bremen", "Stuttgart", "Berlin", "Dresden", "Köln", "Hamburg"]
for i in range(len(geo)):
    print(geo[i])

print(" ")

for i, name in enumerate(geo, start=1):
    print(f"Location {i}: {name}")

print(" ")

presidents =["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams"]
for i in range(len(presidents)):
    print(f"President {i + 1}: {presidents[i]}")
    #f-Strings können erst ab Python3.7 genutzt werden!
print(" ")

for i, name in enumerate(presidents, start=1):
    print(f"President {i}: {name}")
