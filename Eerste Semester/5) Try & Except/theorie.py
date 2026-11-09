from csv import excel

print(dir(locals()["__builtins__"]))

test = ["dingers","wingers","wing dingers","winds ginds"]

try:
    nummer = int(test)
except TypeError:
    print("hoolllyyy shiiiitttt")

#you know this shit already.

try:
    probleem = int(input("Geef een nummer "))
    print(probleem)
except ValueError:
    print("Stupid faggio")
except OverflowError:
    print("ts does NOT happen bro")
except IndexError:
    print("wtf is this even brochacholingo")

continuing = True
while continuing:
    try:
        probleem = int(input("Geef een nummer "))
        print(probleem)
        continuing = False
    except:
        continuing = True

def vraag_nummer():
    while True:
        try:
            return int(input("Nummer: "))
        except:
            pass


print(vraag_nummer(),"dih up yo ahh")