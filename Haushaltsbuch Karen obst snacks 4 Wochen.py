#Author govaeka
#28 April 2023
#erster Upload
#Budgets
BudObst = float(0)
BudSna = float(0)
BudGesamt = BudObst + BudSna

#Ausgaben für 4 Wochen
AusObst1 = float(0)
AusObst2 = float(0)
AusObst3 = float(0)
AusObst4 = float(0)
AusSna1 = float(0)
AusSna2 = float(0)
AusSna3 = float(0)
AusSna4 = float(0)

#Total Ausgaben
AusObstGesamt = AusObst1 + AusObst2 + AusObst3 + AusObst4
AusSnaGesamt = AusSna1 + AusSna2 + AusSna3 + AusSna4
AusGesamt = AusObstGesamt + AusSnaGesamt




while True:
    print("Auswahl-Menü\nFür welche Kategorie möchtest du einen Eintrag vornehmen?")
    print("1 - Ausgaben")
    print("2 - Budget")
    print("0 - Übersicht Haushaltsbuch")
    print("X - Abbruch")

    eingabe = input("Treffe deine Auswahl: ")
    #Budgets
    if eingabe == "2":
        print("Für welche Kategorie möchtest du das Budget eintragen?")
        print("1 - Obst")
        print("2 - Snacks")
        eingabe = 0
        antwort = input("Treffe deine Auswahl: ")
        if antwort == "1":
            print("Du hast Obst gewählt.")
            BudObst = float(input("Gebe den Betrag ein: "))
            antwort = 0
            frage = input("Alles klar! Möchtest du noch etwas eingeben? j/n ")
            if frage == "j":
                print()
            if frage == "n":
                break
        if antwort == "2":
            print("Du hast Snacks gewählt.")
            BudSna = float(input("Gebe den Betrag ein: "))
            antwort = 0
            frage = input("Alles klar! Möchtest du noch etwas eingeben? j/n ")
            if frage == "j":
                print()
            if frage == "n":
                break

    #Ausgaben
    if eingabe == "1":
        print("Für welche Kategorie möchtest du die Ausgaben eintragen?")
        print("1 - Obst")
        print("2 - Snacks")
        #Obst
        antwort = input("Treffe deine Auswahl: ")
        if antwort == "1":
            print("Du hast Obst gewählt.\nFür welche Woche möchtest du einen Eintrag vornehmen?")
            print("1 - Woche 1")
            print("2 - Woche 2")
            print("3 - Woche 3")
            print("4 - Woche 4")
            antwort = input("Treffe deine Auswahl: ")
            if antwort == "1":
                print("Du hast Woche 1 gewählt.")
                AusObst1 = float(input("Gebe den Betrag ein: "))
                frage = input("Alles klar! Möchtest du noch etwas eingeben? j/n ")
                if frage == "j":
                    print()
                if frage == "n":
                    break
            if antwort == "2":
                print("Du hast Woche 2 gewählt.")
                AusObst2 = float(input("Gebe den Betrag ein: "))
                frage = input("Alles klar! Möchtest du noch etwas eingeben? j/n ")
                if frage == "j":
                    print()
                if frage == "n":
                    break
            if antwort == "3":
                print("Du hast Woche 3 gewählt.")
                AusObst3 = float(input("Gebe den Betrag ein: "))
                frage = input("Alles klar! Möchtest du noch etwas eingeben? j/n ")
                if frage == "j":
                    print()
                if frage == "n":
                    break
            if antwort == "4":
                print("Du hast Woche 4 gewählt.")
                AusObst4 = float(input("Gebe den Betrag ein: "))
                frage = input("Alles klar! Möchtest du noch etwas eingeben? j/n ")
                if frage == "j":
                    print()
                if frage == "n":
                    break
        #Snacks
        if antwort == "2":
            print("Du hast Snacks gewählt.\nFür welche Kategorie möchtest du einen Eintrag vornehmen?")
            print("1 - Woche 1")
            print("2 - Woche 2")
            print("3 - Woche 3")
            print("4 - Woche 4")
            antwort = input("Treffe deine Auswahl: ")
            if antwort == "1":
                print("Du hast Woche 1 gewählt.")
                AusSna1 = float(input("Gebe den Betrag ein: "))
                frage = input("Alles klar! Möchtest du noch etwas eingeben? j/n ")
                if frage == "j":
                    print()
                if frage == "n":
                    break
            if antwort == "2":
                print("Du hast Woche 2 gewählt.")
                AusSna2 = float(input("Gebe den Betrag ein: "))
                frage = input("Alles klar! Möchtest du noch etwas eingeben? j/n ")
                if frage == "j":
                    print()
                if frage == "n":
                    break
            if antwort == "3":
                print("Du hast Woche 3 gewählt.")
                AusSna3 = float(input("Gebe den Betrag ein: "))
                frage = input("Alles klar! Möchtest du noch etwas eingeben? j/n ")
                if frage == "j":
                    print()
                if frage == "n":
                    break
            if antwort == "4":
                print("Du hast Woche 4 gewählt.")
                AusSna4 = float(input("Gebe den Betrag ein: "))
                frage = input("Alles klar! Möchtest du noch etwas eingeben? j/n ")
                if frage == "j":
                    print()
                if frage == "n":
                    break

    if eingabe == "X":
        break
    if eingabe == "x":
        break
    
#Übersicht Haushaltsbuch: Gesamtbudget, Gesamtausgaben 
    if eingabe == "0":
        print("\nÜbersicht Haushaltsbuch\n")
        print("Budget für Obst: ",BudObst)
        print("Budget für Snacks: ",BudSna)
        print("Budget insgesamt: ", BudGesamt)
        print()
        print("Ausgaben für Obst")
        print("Woche 1: ",AusObst1)
        print("Woche 2: ",AusObst2)
        print("Woche 3: ",AusObst3)
        print("Woche 4: ",AusObst4)
        print("Ausgaben für Obst insgesamt: ",AusObstGesamt)
        print()
        print("Ausgaben für Snacks")
        print("Woche 1: ",AusSna1)
        print("Woche 2: ",AusSna2)
        print("Woche 3: ",AusSna3)
        print("Woche 4: ",AusSna4)
        print("Ausgaben für Snacks insgesamt: ",AusSnaGesamt)
        print()
        print("Ausgaben insgesamt: ",AusGesamt)
        print()
        if AusObstGesamt > BudGesamt:
            print("\nDas Budget wurde um {0:.2f} EUR überschritten".format(AusObstGesamt-BudGesamt))
            frage = input("\nMöchtest du noch etwas eingeben? j/n ")
            if frage == "j":
                print()
            if frage == "n":
                break
        else:
            print("\nDu hast noch {0:.2f} EUR übrig!".format(BudGesamt-AusObstGesamt))
            frage = input("\nMöchtest du noch etwas eingeben? j/n ")
            if frage == "j":
                print()
            if frage == "n":
                break
        
        

        
        






