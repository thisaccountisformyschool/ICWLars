import math

def som_van_getallen(x,y):
    som = x+y
    return som


print(som_van_getallen(3,9))

def verschil_van_gettalen(x,y):
    return x-y

print(verschil_van_gettalen(3,972))


def verjaardag():
    print("Verjaardag yippeee")

def verjangdag():
    print("verjangday niet yippeee")
    return

verjaardag()
verjangdag()


#zonder haakjes wordt het een object
print(verjangdag)

def maak_een_zin(*woorden):
    zin = ""
    for i in woorden:
        zin += i
        zin +=" "
    return zin

print(maak_een_zin("Hallo","my","name","is","hector"))

def maak_een_zin_met_leesteken(leesteken,*woorden):
    zin = ""
    for i in woorden:
        zin += i
        zin +=" "
    zin+=leesteken
    return zin

print(maak_een_zin_met_leesteken("!","Hallo","my","name","is","hector"))

def factorials(getal):
    result = 1
    for x in range(1,getal+1):
        result *= x
    return result
print(factorials(5))
def factori(getal):
    if getal == 1:
        return 1
    else:
        return getal * factori(getal-1)

print(factori(999))
