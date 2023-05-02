#Haushaltsbuch
budget = float(input("Wie viel möchtest du pro Woche maximal für Obst ausgeben? "))

obst = []

print()
woche1 = float(input("Wie viel hast du in der 1. Woche für Obst ausgegeben? "))
obst.append(woche1)
woche2 = float(input("Wie viel hast du in der 2. Woche für Obst ausgegeben? "))
obst.append(woche2)
woche3 = float(input("Wie viel hast du in der 3. Woche für Obst ausgegeben? "))
obst.append(woche3)
woche4 = float(input("Wie viel hast du in der 4. Woche für Obst ausgegeben? "))
obst.append(woche4)

durchschnitt = (sum(obst))/(len(obst))

print("\nDer Wochendurchschnitt für Obst beträgt {0:.2f} EUR.".format(durchschnitt))

print()
if durchschnitt > budget:
    print("Leider wurde mehr als geplant für Obst ausgegeben.")
else:
    print("Das Budget wurde eingehalten!")