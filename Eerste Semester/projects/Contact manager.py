contacten = []

def contact_toevoegen(naam,last_name,email,nummer):
    new_contact = {
        "naam":naam,
        "last_naam":last_name,
        "email":email,
        "telefoon":nummer
    }

    contacten.append(new_contact)

def contact_tonen():
    print("")
    for i,contact in enumerate(contacten):
        i = str(i+1)
        print(i+")",contact["naam"])
    choice = input()
    for i,contact in enumerate(contacten):
        i = str(i+1)
        if choice == i:
            print(f"Naam: {contact["naam"]}")
            print(f"Achteraam: {contact["last_naam"]}")
            print(f"Email: {contact["email"]}")
            print(f"Telefoonnummer: {contact["telefoon"]}")

def contact_verwijderen(invoer):
    for i in contacten:
        index = str(contacten.index(i)+1)
        if index == invoer:
            contacten.pop(int(index)-1)
        elif i["naam"] == invoer:
            contacten.remove(i)

def changeling_max(contact):
    changeling = input("Wat wil je veranderen? ")
    if changeling.lower() == "naam":
        nieuwe_waarden = input("Nieuwe waarden: ")
        contact["naam"] = nieuwe_waarden
    elif changeling.lower() == "email":
        nieuwe_waarden = input("Nieuwe waarden: ")
        contact["email"] = nieuwe_waarden
    elif changeling.lower() == "telefoonnummer":
        nieuwe_waarden = input("Nieuwe waarden: ")
        contact["telefoon"] = nieuwe_waarden
    noice = input("Nog iets veranderen? ")
    if noice.lower() == "ja":
        changeling_max(contact)
    elif noice.lower() == "nee":
        return


def contact_aanpassen(invoer):
    for contact in contacten:
        index = str(contacten.index(contact)+1)
        if index == invoer:
            print(f"Naam: {contact["naam"]}")
            print(f"Achteraam: {contact["last_naam"]}")
            print(f"Email: {contact["email"]}")
            print(f"Telefoonnummer: {contact["telefoon"]}")
            changeling_max(contact)
        elif contact["naam"] == invoer:
            print(f"Naam: {contact["naam"]}")
            print(f"Achteraam: {contact["last_naam"]}")
            print(f"Email: {contact["email"]}")
            print(f"Telefoonnummer: {contact["telefoon"]}")
            changeling_max(contact)

def contact_zoeken(zoekterm):
    for contact in contacten:
        if zoekterm in contact["naam"]:
            print(f"Naam: {contact["naam"]}")
            print(f"Achteraam: {contact["last_naam"]}")
            print(f"Email: {contact["email"]}")
            print(f"Telefoonnummer: {contact["telefoon"]}")
        elif zoekterm in contact["email"]:
            print(f"Naam: {contact["naam"]}")
            print(f"Achteraam: {contact["last_naam"]}")
            print(f"Email: {contact["email"]}")
            print(f"Telefoonnummer: {contact["telefoon"]}")
        elif zoekterm in contact["telefoon"]:
            print(f"Naam: {contact["naam"]}")
            print(f"Achteraam: {contact["last_naam"]}")
            print(f"Email: {contact["email"]}")
            print(f"Telefoonnummer: {contact["telefoon"]}")

def menu():
    print("")
    print("1) Contact toevoegen \n2) Toon alle contacten \n3) Contact verwijderen \n4) Contact aanpassen \n5) Contact zoeken")
    choice = input()
    if choice == "1":
        print("")
        naam = input("Naam: ")
        last_name = input("Achternaam: ")
        email = input("Email address: ")
        nummer = input("Telefoonnummer: ")
        contact_toevoegen(naam,last_name,email,nummer)
        menu()
    elif choice == "2":
        contact_tonen()
        menu()
    elif choice == "3":
        invoer = input("Welke contact will je verwijderen? (index of naam) ")
        contact_verwijderen(invoer)
        menu()
    elif choice == "4":
        invoer = input("Welke contact will je aanpassen? (index of naam) ")
        contact_aanpassen(invoer)
        menu()
    elif choice == "5":
        zoekterm = input("Zoekterm: ")
        contact_zoeken(zoekterm)
        menu()
    else:
        menu()

menu()