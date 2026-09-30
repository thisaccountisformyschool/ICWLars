#Pizza mozarella
from idlelib.debugobj_r import remote_object_tree_item


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




