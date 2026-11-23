import json

with open("biodiversity.json","r") as bio:
    data = json.load(bio)

def chooser():
    yn = input("Look at another? (y/n) ")
    if yn == "n":
        exit()
    elif yn == "y":
        the_program()

def the_program():
    entries = []
    didthefagchooseone = False
    while not didthefagchooseone:
        country = input("Country: ")
        country = country.capitalize()
        for entry in data:
            if entry["Entity"] == country:
                print(f"{entry["Year"]}:{entry["Average proportion of Terrestrial Key Biodiversity Areas (KBAs) covered by protected areas (%)"]}%")
                entries.append(entry)
                didthefagchooseone = True
        if not didthefagchooseone:
            print("Country Not Found")

    difference = round(entries[0]["Average proportion of Terrestrial Key Biodiversity Areas (KBAs) covered by protected areas (%)"] - entries[-1]["Average proportion of Terrestrial Key Biodiversity Areas (KBAs) covered by protected areas (%)"],2)

    if difference > 0:
        print(f"The amount of protected area has lowered by {difference}%")
    elif difference < 0:
        print(f"The amount of protected area has raised by {difference * -1}%")
    elif difference == 0:
        print("The amount of protected area has not changed")

    chooser()

the_program()