import datetime

taken = []

def voeg_taak_toe():
    global taken
    taak = []
    taak_name = input("Wat is de taak? ")
    jaar = int(input("Welke jaar"))
    maand = int(input("Welke maand"))
    dag = int(input("Welke dag"))
    date = datetime.date(jaar,maand,dag)
    taak.append(taak_name)
    taak.append(date)

    taken.append(taak)
    print("Taak toegevoegd")
    print("")
    menu()
    return

def bekijk_taken():
    global taken
    print("Huidige taken:")
    for i,v in enumerate(taken):
        print(str(i+1)+")",v[0],v[1])
    print("")
    menu()
    return


def verwijder_taak():
    global taken
    removal = int(input("Welke taak wil je verwijderen (index)(777 to cancel) "))
    if removal in range(len(taken)):
        print("Taak", taken[removal],"verwijderd!")
        taken.pop(removal)
    elif removal == 777:
        print("Canceled!")
        print("")
        menu()
        return
    else:
        print("Geen taak van die naam bestaat")
        verwijder_taak()
        return
    print("")
    menu()
    return

def search():
    global taken
    search = input("Zoekterm: ")
    for i in taken:
        if search in i:
            print(i)
    print("")
    menu()
    return

def menu():
    print("1) Voeg een taak toe")
    print("2) Bekijk huidige taken")
    print("3) Verwijder een taak")
    print("4) Search voor een taak")
    print("5) Stop de programma")
    task = input()
    if task == "1":
        print("")
        voeg_taak_toe()
        return
    elif task == "2":
        print("")
        bekijk_taken()
        return
    elif task == "3":
        print("")
        verwijder_taak()
        return
    elif task == "4":
        print("")
        search()
        return
    elif task == "5":
        exit()
    else:
        print("Niet an optie!")
        menu()
        return

def datum_printel_dingelmajig(datum,taak):
    if taak.datum == datum:
        print(taak)

def datum_verwij_dongermajong(datum,lijst):
    for i in lijst:
        if i.datum == datum:
            lijst.remove(i)


menu()