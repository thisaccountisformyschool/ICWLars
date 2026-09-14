x = 5
#x is a veriable, an integer

z = "EVERYONE GET IN THE CAR WE'RE LEAVING THIS TOWN NOW " #WHAT THE, THIS ISN'T THE CAR!? IMPOSSIBLE! AAHHHHH NOOOOOO AAAAAHHHHH HERMIT PURPLE

y = 3.14
print(x)
print(y)
print(z) #z is a variable btw a string

x = x+5
print(x)
#holy shittings man x is 10 now
x = x * 2

print(x)

x = x / 2

print(x)
x=int(x)

x = x^2

print(x)

z = z + "WHAT THE, THIS ISN'T THE CAR!? IMPOSSIBLE! AAHHHHH NOOOOOO AAAAAHHHHH HERMIT PURPLE!"

print(z)

lijstje = [x,y,z,"oh shittings man"]

lijstje.remove("oh shittings man")
lijstje.remove(y)

print(lijstje)

print(lijstje.pop(0))
lijstje.append("giraffe")

print(lijstje)

lijstje.insert(0,y)

print(lijstje)

listicus2icus = [1,4,862,3,2,33]
print(listicus2icus)

print(lijstje + listicus2icus)

lijstje.append(listicus2icus)
print(listicus2icus)

print(z)
print(len(z))

if len(listicus2icus) < 3:
    print("lijst is kort")
elif len(listicus2icus) < 8:
    print("normaal lijstje")
else:
    print("lange lijst")

#if oh_shittings / 2 == int:
 #   print("wowzers it's divisible by 2s")
#else:
 #   print("kill yourself")

print(lijstje[2])
print(lijstje[0])
print(lijstje[-1])

oh_shittings = input("bank account pwease :3 ")

laatste_nummer = oh_shittings[-1]

even_cijfers = ["0","2","4","6","8"]
if laatste_nummer in even_cijfers:
    print("yayayayay")
else:
    print("not yay")

nummer = int(input("nummer:"))
nummer += 5
print(nummer)