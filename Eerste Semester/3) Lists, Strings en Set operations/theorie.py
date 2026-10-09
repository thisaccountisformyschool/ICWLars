klas = ["Bert","Benjamin","Boris","Bart","Brian"]


#derde element van een lijst halen:
derde = klas[2]
print(derde)

#plek van var in lijst met .index(...)
plekvanbart = klas.index("Bart")

laatste = klas[-1]

#slicing: DEEL van lijst
midden = klas[1:-1]
print(midden)

#tellen van een element
aantalborisen = klas.count("Boris")
print(aantalborisen)


#len werkt nier zoals count en index
#len heeft de list als parameter nodig
print(len(klas))

appel = ["a","p","p","e","l"]
#appel.append("s")
appel += "s"
print(appel)

#als we een string += doen bij een lijst is dat niet hetzelfde als append
#result: ['a', 'p', 'p', 'e', 'l', 's', 'p', 'e', 'e', 'r']
appel += "peer"
print(appel)

woord = "container"
woord = woord.upper()
print(woord)

klein = woord.lower()
print(klein)

#fly high java_ver </3

woord = woord.lower().replace("n","v",1)
print(woord)

#replace: verander deel van een string
zin = "Berend Brokkenpap heeft de soep aangebrand. Hoe dom."
zin = zin.replace("soep","tomatensaus",1)
print(zin)

#find: vindt een deel IN een string: geeft de eerste index
print(zin.find("de"))
print(zin.find(" "))

#tel hoeveel "e" in een de zin
print(zin.count("e"))

#split() = split(" ")
woordenlijst = zin.split()
woordenlijst = zin.split(" ")
print(woordenlijst)

#splitsen rond een woord
tweedeling = zin.split('tomatensaus')
print(tweedeling)

#splitsen van een string in zinnen.
zindeling = zin.split(".")
print(zindeling)

print(zin.isnumeric())
nummers = "18748932787"
print(nummers.isnumeric())