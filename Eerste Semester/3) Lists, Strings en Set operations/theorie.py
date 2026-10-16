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

#tupel: zelfde als een lijst, maar items kunnen niet aangepast worden
mijnTuple = (1,2,3)
print(mijnTuple)


#set: verzameling van elementen, zonder volgorde
huisdieren = {"kat","hond","krokodil","papegaai","rat","otter"}
print(huisdieren)

#in een set komt elk element maar 1 keer voor
huisdieren2 = {"kat","hond","krokodil","papegaai","rat","otter","hond","krokodil","kat"}
print(huisdieren2)

#element toevoegen in set
huisdieren.add("hamster")
#element verwijderen
huisdieren.remove("krokodil")
huisdieren.discard("hond")

nummers2 = {1,2,3,4,5}
print(max(nummers2))
print(min(nummers2))
print(sum(nummers2))

huisdieren.update({"boa constrictor","Sjorje"})
huisdieren.update({"micheal"})
print(huisdieren)
print(huisdieren2)

#alles dat maar in een van de twee sets voorkomt
print(huisdieren ^ huisdieren2)
#wat bijde sets gelijk hebben
print(huisdieren.intersection(huisdieren2))

#bijde sets bij elkaar
print(huisdieren.union(huisdieren2))
print(huisdieren | huisdieren2)

#subset is deel van een set
#superset is het omgekeerde
huisdieren3 ={"boa constrictor","Sjorje"}
print(huisdieren3.issubset(huisdieren))
print(huisdieren.issuperset(huisdieren3))

#disjoint: twee sets hebben niks samen
huisdieren4 = {"yodeler"}
print(huisdieren4.isdisjoint(huisdieren))

#sorted heeft de gesorteerde lijst terug
huisdierlijst = sorted(huisdieren)
print(huisdierlijst)

#lijst naar set
huisdierenset = set(huisdierlijst)