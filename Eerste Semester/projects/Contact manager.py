contacten = []

def more_adder(new_contact):
    con_choice = input("Meer contactinformatie toevoegen? (y/n) ")
    if con_choice.lower() == "y":
        key = input("Soort: ")
        value = input("Informatie: ")
        new_contact.update({key:value})
        more_adder(new_contact)
    elif con_choice.lower() == "n":
        contacten.append(new_contact)

def contact_toevoegen(naam,last_name,email,nummer):
    print("")
    new_contact = {
        "naam":naam,
        "achternaam":last_name,
        "email":email,
        "telefoon":nummer
    }
    more_adder(new_contact)

def print_contact(contact):
    for info in contact:
        print(f"{info.capitalize()}: {contact[info]}")

    # print(f"Naam: {contact["naam"]}")
    # print(f"Achteraam: {contact["last_naam"]}")
    # print(f"Email: {contact["email"]}")
    # print(f"Telefoonnummer: {contact["telefoon"]}")

def sort_key_name(contact):
    return contact["naam"]

def sort_key_last_name(contact):
    return contact["achternaam"]

def contact_tonen():
    print("")
    sort_choice = input("Will je sorteren op naam of achternaam? ")
    if sort_choice.lower() == "naam":
        contacten.sort(key=sort_key_name)
    elif sort_choice.lower() == "achternaam":
        contacten.sort(key=sort_key_last_name)
    for i,contact in enumerate(contacten):
        i = str(i+1)
        print(i+")",contact["naam"],contact["achternaam"])
    choice = input()
    for i,contact in enumerate(contacten):
        i = str(i+1)
        if choice == i:
            print_contact(contact)
            input("Druk enter om door te gaan")

def contact_verwijderen(invoer):
    print("")
    for i in contacten:
        index = str(contacten.index(i)+1)
        if index == invoer:
            contacten.pop(int(index)-1)
            print("Contact verwijderd!")
            input("Druk enter om door te gaan")
        elif i["naam"] == invoer:
            contacten.remove(i)
            print("Contact verwijderd!")
            input("Druk enter om door te gaan")

def changeling_max(contact):
    changeling = input("Wat wil je veranderen? ")
    if changeling.lower() == "naam":
        nieuwe_waarden = input("Nieuwe waarden: ")
        contact["naam"] = nieuwe_waarden
    if changeling.lower() == "achternaam":
        nieuwe_waarden = input("Nieuwe waarden: ")
        contact["last_naam"] = nieuwe_waarden
    elif changeling.lower() == "email":
        nieuwe_waarden = input("Nieuwe waarden: ")
        contact["email"] = nieuwe_waarden
    elif changeling.lower() == "telefoonnummer":
        nieuwe_waarden = input("Nieuwe waarden: ")
        contact["telefoon"] = nieuwe_waarden
    noice = input("Nog iets veranderen? (y/n) ")
    if noice.lower() == "y":
        changeling_max(contact)
    elif noice.lower() == "n":
        return


def contact_aanpassen(invoer):
    for contact in contacten:
        index = str(contacten.index(contact)+1)
        if index == invoer:
            print_contact(contact)
            changeling_max(contact)
        elif contact["naam"] == invoer:
            print_contact(contact)
            changeling_max(contact)


def contact_zoeken(zoekterm):
    for contact in contacten:
        if zoekterm in contact["naam"]:
            print_contact(contact)
            input("Druk enter om door te gaan")
        elif zoekterm in contact["last_naam"]:
            print_contact(contact)
            input("Druk enter om door te gaan")
        elif zoekterm in contact["email"]:
            print_contact(contact)
            input("Druk enter om door te gaan")
        elif zoekterm in contact["telefoon"]:
            print_contact(contact)
            input("Druk enter om door te gaan")

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