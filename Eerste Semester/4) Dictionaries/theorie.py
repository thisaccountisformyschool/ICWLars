#Dictionary: lijst van Key:Value pairs.
dictionary = {"Aantal leerlingen":8,
              "Mainlokaal":"B303",
              "grootste leerkracht":"Mr. Spruyt",
              "namen":["Melyvn","Lars","Kobe","Arjuno","Graham","Noah","Nora"]
              }
print(dictionary["Aantal leerlingen"])
print(dictionary.get("namen"))

#met .update() voeg je tegelijk een of meerdere key:value pairs toe
dictionary.update({"favouriete_eten":"pritt"})
#ook op de volgende manier kan je een key:value pair toevoegen
dictionary["leeftijd"] = 16
print(dictionary)

#een item toevoegen == een item aanpassen
dictionary.update({"leeftijd":17})
dictionary["leeftijd"] = 18
dictionary["leeftijd"] += 1

#printen en aanpassen van elementen in een dict
dictionary["namen"].append("Björn")
print(dictionary["namen"][2])

print(dictionary.keys())
print(dictionary.values())

if "Mainlokaal" in dictionary:
    print("gottteeee")
if "B303" in dictionary:
    print("goyteeee")