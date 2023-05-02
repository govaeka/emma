noten = []

deutsch = float(input("Bitte gebe deine Note für Deutsch ein: "))
noten.append(deutsch)
englisch = float(input("Bitte gebe deine Note für Englisch ein: "))
noten.append(englisch)
mathe = float(input("Bitte gebe deine Note für Mathe ein: "))
noten.append(mathe)

'''Dit
is ook
een commentaar
'''

#Notendurchschnitt:
anzahl = len(noten)
durchschnitt = ((sum(noten))/(anzahl))
print("{0:.2f}".format(durchschnitt))

if durchschnitt > 4:
    print("Die Abiturprüfung muss wiederholt werden.")
else:
    print("Die Abiturprüfung wurde bestanden.")