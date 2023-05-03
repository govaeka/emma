from time import sleep

# defs

def menu():
    
    print("\nDiese Fahrkarten stehen Ihnen zur Auswahl:\nNormal: n\nKurzstrecke: k\nTageskarte: t\nAbbrechen: x")
    antwort = input("\nBitte wählen Sie Ihr Ticket: ")
    if antwort == "n":
        print("Normal: 4,50 EUR")
        kaufen()
    if antwort == "k":
        print("Kurzstrecke: 2,50 EUR")
        kaufen()    
    if antwort == "t":
        print("Tageskarte: 8,00 EUR")
        kaufen()
    if antwort == "x":
        print()
        
def kaufen():
    antwort = input("Ticket kaufen? j/n ")
    if antwort == "j":
        zahlen()
    else:
        menu()

def zahlen():
    antwort = input("Wie möchten Sie zahlen? Bar (b) oder mit Karte (k)? Vorgang abbrechen (x).\n\nBitte treffen Sie Ihren Auswahl: ")
    if antwort == "b":
        print("Bitte werfen Sie die Münzen ein.")
        sleep(2)
        print("\n\nIhre Fahrkarte wird gedruckt. Bitte warten.\n\n")
        sleep(2)
        print("Vielen Dank für Ihren Einkauf.")
    elif antwort == "k":
        print("Bitte folgen Sie die Anweisungen auf dem Terminal.")
        sleep(2)
        print("\n\nIhre Fahrkarte wird gedruckt. Bitte warten.\n\n")
        sleep(2)
        print("Vielen Dank für Ihren Einkauf.\n\n\n")
    elif antwort == "x":
        sleep(2)
        menu()
    else:
        print("\nEingabe ungültig.\n")
        zahlen()

antwort = 0
while antwort == 0:
    eingabe = input("\nBitte drücken Sie s um die Anwendung zu starten. ")
    if eingabe == "s":
        menu()