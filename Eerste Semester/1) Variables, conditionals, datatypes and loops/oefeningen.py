#1. Even of Oneven
import math

def Even_of_Oneven():
    even_getalen = ["0","2","4","6","8"]
    nummer_input = input("Nummer: ")
    laatste_nummer = nummer_input[-1]

    if laatste_nummer in even_getalen:
        print("Even")
    else:
        print("Oneven")

#2. Leeftijdscontrole
def Leeftijdscontrole():
    leeftijd = int(input("Leeftijd: "))

    if leeftijd < 12:
        print("Kind")
    elif leeftijd >= 12 and leeftijd < 18:
        print("Tiener")
    else:
        print("Volwassene")

#3. Tempratuurconverter
def Tempratuurconverter():
    temp_cel = float(input("Tempratuur in Celsius: "))
    temp_fahr = temp_cel * 1.8 + 32
    print("Tempratuur in Fahrenheit:",temp_fahr)

#4. Eenvoudige Rekenmachine
def Calc():
    getal_1 = int(input("Nummer 1: "))
    getal_2 = int(input("Nummer 2: "))

    print("Som:", getal_1 + getal_2)
    print("Verschil", getal_1 - getal_2)
    print("Product", getal_1 * getal_2)
    print("Quotiënt", getal_1 / getal_2)

#5. TipTop
def TipTop():
    div_3 = [3,6,9,12,15,18,21,24,27,30]
    div_5 = [5,10,15,20,25,30]

    for i in range(31):
        if i in div_5 and i in div_3:
            print("TipTop")
        elif i in div_3:
            print("Tip")
        elif i in div_5:
            print("Top")
        else:
            print(i)

#6. Wachtwoordcontrole
def Wachtwoordcontrole():
    wachtwoord = input("Wachtwoord: ")
    if wachtwoord == "python123":
        print("Toegang Verleend")
    else:
        print("Fout Wachtwoord")

#7. Punten omzetten naar een Score
def Punten_omzetten():
    score = int(input("Score: "))

    if score >= 90:
        print("A")
    elif score <= 89 and score >= 80:
        print("B")
    elif score <= 79 and score >= 70:
        print("C")
    elif score <= 69 and score >= 60:
        print("D")
    elif score < 60:
        print("F")

#8. Tel de Klinkers
def Tel_klinkers():
    klinker = ["a","e","i","o","u"]
    woord = input("Woord: ")
    aantal_klinkers = 0

    for i in range(len(woord)):
        if woord[i] in klinker:
            aantal_klinkers += 1

    print(aantal_klinkers)

#9. Som van Getallen
def som_van_getallen():
    n = int(input("Positief getal n: "))
    result = (n*(n+1))/2
    print(result)

#10. Priemgetal-checker

def priem_checker():
    priem_getal_maybe = int(input("Nummer:"))
    is_prime = True

    for i in range(2,priem_getal_maybe):
        if priem_getal_maybe % i == 0:
            is_prime = False

    if not is_prime:
        print("Not prime")
    elif is_prime:
        print("Prime")




project_number = int(input("Project Number:"))

if project_number == 1:
    Even_of_Oneven()
elif project_number == 2:
    Leeftijdscontrole()
elif project_number == 3:
    Tempratuurconverter()
elif project_number == 4:
    Calc()
elif project_number == 5:
    TipTop()
elif project_number == 6:
    Wachtwoordcontrole()
elif project_number == 7:
    Punten_omzetten()
elif project_number == 8:
    Tel_klinkers()
elif project_number == 9:
    som_van_getallen()
elif project_number == 10:
    priem_checker()