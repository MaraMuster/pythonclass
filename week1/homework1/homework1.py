# 0.1 Aufgabe 1
# Aktivieren Sie Ihre Virtuelle Umgebung und installieren Sie darin das Paket Pandas

#0.2 Aufgabe 2
# Definieren Sie drei Variablen von jeweils unterschiedlichem Typ und wandeln Sie den Typ um
a ="Hello World!"
b = 123456
c = 11.11

str(b) #wandelt 123456 in '123456' um und damit wird int zu str

#0.3 Aufgabe 3
# Welche der folgenden Anweisungen in der Python-Shell sind richtig und welche nicht?
# Erklären Sie im Falle der inkorrekten Anweiseungen, worin das Problem besteht

#valide Anweiseungen
t = (4,7,9)
s = "Die Sonne scheint"
l = [34, 22.1, "777", [3, 4]]
t2 = (4,8, [45,91])
t[0] #gibt den Wert 4 aus
s[4] #gibt 'S' aus
l[3][0] = "h"
l #zeigt liste an
t2[2][0] = 23 # ersetzt 45 durch den Wert 23

#inkorrekte Anweiseungen
t[3] #inkorrekt, weil der Tupel nur 3 Elemente enthält
t(3) #inkorrekt, TypeError.
s[4] = x #inkorrekt. 
l[2][0] = "g" #inkorrekt. 'str' object does not support item assignment

#0.4 Aufgabe 4
# Mit Hilfe der Funktion len können Sie die Länge eines sequentiellen Objekts berechnen.
# Definieren Sie von jedem der Ihnen bekannten sequentiellen Datentypen (String, Liste, Tupel)
# jeweils eine Variable und berechnen Sie Ihre Länge. Wie können Sie die Funktion
# len verwenden, um das letzte Element einer sequentiellen Variable (z.B. einer Liste)
# auszugeben? Zeigen Sie dies an einer der drei zuvor definierten Variablen

a="Hello World"
len(a) #Ausgabe auf der Konsole: 12
a[-1] #mit -1 kann man sich das letzte Element einer sequentiellen Variable ausgeben lassen

li = [12, 13, 14, 15]
len(li) # Ausgabe auf der Konsole: 4 (die Liste enthält 4 Elemente)
li[-1] # Ausgabe 15

tu= (1,2,3,4,5,6,7)
len(tu) # Ausgabe auf der Konsole: 7

#0.5 Aufgabe 5
#Welche zwei Sätze verbergen sich hinter dem folgenden Buchstabensalat?
#"IY otuh ihnakv ei ta ipsr oac endeuwr ef ewaittuhr e1.0 Dpoanr’atm etteelrls
#?a nyyooun epriotb awbalsy amni sascecdi dseonmte..""
sentence = "IY otuh ihnakv ei ta ipsr oac endeuwr ef ewaittuhr e1.0 Dpoanr’atm etteelrls ?a nyyooun epriotb awbalsy amni sascecdi dseonmte.."
len(sentence) #Ausgabe 128
sentence[1:128:2] #'You have ais a new feature. parametll anyone it was missed some.'
sentence[0:128:2] # "I think it procedure with 10Don't ters? you probablyan accident."
