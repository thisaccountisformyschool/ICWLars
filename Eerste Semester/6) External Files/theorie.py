import os
import json
print(dir(os))

#toon current directory
print(os.getcwd())

#change current working directory
os.chdir("C:\\Users\\lars.vandezande\\OneDrive - VTI Leuven\\Bureaublad")
print(os.getcwd())

#mkdir is a dirmaker its makje the deer
#os.mkdir("magcal")
#os.remove("magcal")

os.chdir(".\\magcal")
newbile = open("ding.txt","w")
newbile.close()

os.remove("ding.txt")

# "w" makes a file and "r" reads it
# newkyle = open("omg they fucked kyle.txt","w")
# newkyle.close()
# newkyle = open("omg they fucked kyle.txt","r")
# newkyle.close()

#os.remove('flop.docx')

#write overwrites files
# with open("verhaal.txt","w") as verhaal:
#     verhaal.write("Very well-made story")

with open("verhaal.txt","a") as verhaal:
    verhaal.write("met draken")

print(os.listdir())

with open("verhaal.txt","r") as veb:
    print(veb.read())


try:
    with open("epos.txt","r") as epos:
        print(epos.read())
except FileNotFoundError:
    with open("epos.txt","w") as epos:
        epos.write("hello evernyan, I am a bird")


leerling = {
    "klas":"7ICW",
    "naam":"Zeebe",
    "leeftijd":18,
    "hobbies": ["padel","zwemmen","badminton"]
}

with open("jason.json","w") as jason:
    json.dump(leerling,jason)

with open("jason.json","r") as jason:
    big_leer = json.load(jason)
    print(big_leer)

























