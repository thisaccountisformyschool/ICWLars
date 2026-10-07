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
    voltooid = False
    taak.append(taak_name)
    taak.append(date)
    taak.append(voltooid)

    taken.append(taak)
    print("Taak toegevoegd")
    print("")
    menu()
    return

def bekijk_taken(taak_parameters):
    global taken
    print("Huidige taken:")
    if taak_parameters == "XO":
        for i,v in enumerate(taken):
            if not v[2]:
                print(str(i+1)+")","[O]",v[0],v[1])
            if v[2]:
                print(str(i+1)+")","[X]",v[0],v[1])
    if taak_parameters == "O":
        for i,v in enumerate(taken):
            if not v[2]:
                print(str(i+1)+")","[O]",v[0],v[1])
    if taak_parameters == "X":
        for i,v in enumerate(taken):
            if v[2]:
                print(str(i+1)+")","[X]",v[0],v[1])
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

def markeer_als_voltooid(nummer):
    global taken
    print(taken)
    if not taken[nummer][2]:
        taken[nummer][2] = True
        print("Gemarkeert!")
    else:
        print("Is al gedaan")
    menu()


def menu():
    print("1) Voeg een taak toe")
    print("2) Bekijk huidige taken")
    print("3) Verwijder een taak")
    print("4) Search voor een taak")
    print("5) Markeer een taak als compleet")
    print("6) Stop de programma")
    task = input()
    if task == "1":
        print("")
        voeg_taak_toe()
        return
    elif task == "2":
        print("")
        parameters = input("Parameters (X,O,XO): ")
        bekijk_taken(parameters)
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
        print("")
        task_to_mark = int(input("Welke taak? (Index) "))
        markeer_als_voltooid(task_to_mark)
        return
    elif task == "6":
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