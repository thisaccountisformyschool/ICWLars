#Pizza mozarella
import math
import os
import random

def pizza_mozarella():
    kassa = 0

    def bestel_pizza(soort,prijs):
        print("1", soort, "pizza besteld")
        global kassa
        kassa += prijs
        bestel_opniew()


    def bestel_opniew():
        more = input("More? ")
        if more.lower() == "yes":
            soort = input("Welke soort? ")
            prijs = int(input("Hoe duur? "))
            bestel_pizza(soort, prijs)
        else:
            print("We made", kassa, "lira!")

    soort = input("Welke soort? ")
    prijs = int(input("Hoe duur? "))
    bestel_pizza(soort,prijs)

#rekermachiner
def rekermachiner():
    def calc(start):
        total = start
        op = input("op = ")
        if op == "SOLVE":
            print(total)
            exit()
        xn = int(input("xn = "))
        if op == "+":
            total += xn
        elif op == "-":
            total -= xn
        elif op == "*":
            total *= xn
        elif op == "/":
            total /= xn
        else:
            exit("NOT AN OPERAND")

        return total

    def berek(num):
        tot = calc(num)
        berek(tot)

    x1 = int(input("x1 = "))
    berek(x1)


#galgeringeenr

def galgifier():
    # def galgify2(woord,*geraden_letters):
    #     galgified_word = ""
    #     for i in woord:
    #         if i in geraden_letters:
    #             galgified_word = galgified_word.join(i)
    #             print(i)
    #         else:
    #             galgified_word = galgified_word.join("_")
    #             print("_")
    #     return galgified_word
    #
    # print(galgify2("hello","h","l"))

    def galgify(woord,*geraden_letters):
        galgified_word = []
        for i in woord:
            if i in geraden_letters:
                galgified_word.append(i)
                print(i)
            else:
                galgified_word.append("_")
                print("_")
        result = "".join(galgified_word)
        return result

    print(galgify("meervoudigepersoonlijkheidsstoornis","h","l","z","j","o","p","v","m"))

def punten_calc():
    punten = []

    def voeg_punten_toe(punt):
        global punten
        if punt <= 20:
            punten.append(punt)
            return True
        else:
            return False

    def gemmiddelde(lijst):
        total_divising = 0
        if len(lijst) == 0:
            return 0
        else:
            for i in lijst:
                total_divising += i
            average = total_divising / len(lijst)
            return average

    def hoogste(lijst):
        hoogste_nummer = 0
        for i in lijst:
            if i > hoogste_nummer:
                hoogste_nummer = i
        return hoogste_nummer

    def laagste(lijst):
        laagste_nummer = 20
        for i in lijst:
            if i < laagste_nummer:
                laagste_nummer = i
        return laagste_nummer

    def aantal_geslaagd(lijst,grens):
        amount = 0
        for i in lijst:
            if i >= grens:
                amount += 1
        return amount

    def status(lijst,grens):
        if gemmiddelde(lijst) >= grens:
            return "geslaagd"
        else:
            return  "niet geslaagd"


    def menu():
        print("1) punt toevoegen")
        print("2) overzicht tonen")
        print("3) stoppen")
        keuze = int(input(""))
        if keuze == 1:
            punt = int(input("Punt? "))
            if voeg_punten_toe(punt):
                print("Punt toegevoegd")
            elif not voeg_punten_toe(punt):
                print("Punt niet toegevoegd!")
            menu()
        elif keuze == 2:
            print("Aantal punten:", len(punten))
            print("Gemiddelde:", gemmiddelde(punten))
            print("Hoogste punt:", hoogste(punten))
            print("Laagste punt:", laagste(punten))
            print("Aantal geslaagt:", aantal_geslaagd(punten,10))
            print("Status:", status(punten,10))
            menu()
        elif keuze == 3:
            exit("USER EXIT")
    menu()

punten_calc()