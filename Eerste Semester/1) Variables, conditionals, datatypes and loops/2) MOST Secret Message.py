# De initiële lijst met binaire codes. Pas deze niet aan!
import random
from os import remove

binary_codes = ['10010100', '10101000', '10111100', '00111',
                '10100110', '10100000', '10110110', '11110101',
                '10010101', '10111001', '0100110011', '10100100',
                '10100001', '1111001', '10101010', '11111001',
                '11100101', '10100110', '10100000', '0010101110',
                '10110001', '11100101', '10111000', '10100100',
                '10110010', '10101100', '10100110', '11100101',
                '10110100', '10101000', '0111110010', '10111100',
                '10100110', '110000', '10110100', '11100101', '10100011',
                '10100000', '10100111', '001110', '01011', '0010100110',
                '0110111', '10101100', '1001111', '10100001', '10100100',
                '110011', '10100110', '1101110010']


# Zet je code om de lijst te repareren hieronder:
binary_codes_cool = []

for i in binary_codes:
    if len(i) == 8:
        binary_codes_cool.append(i)

for i,k in enumerate(binary_codes_cool):
   for j in k:
       j = list(j)
       j.pop(0)
       j.insert(0,"0")
       j = "".join(j)
       k = list(k)
       k[0] = j
       k = "".join(k)
       binary_codes_cool[i] = k


print(binary_codes_cool)

for i,j in enumerate(binary_codes_cool):
    ic = i+1
    if ic % 2 == 0:
        print(j)
        j = list(j)
        if j[3] == "0":
            j[3] = "1"
            print(j[3])
        elif j[3] == "1":
            j[3] = "0"
            print(j[3])
        j = "".join(j)
        print(j)
    binary_codes_cool[i] = j
print(binary_codes_cool)

for i in binary_codes_cool:
    for j, k in enumerate(i):
        if j % 2 == 0:
            if k == "0":
                pass

# De code hieronder vertaalt je huidige binaire code naar ascii-karacters.
decoded_text = ''.join(chr(int(b, 2)) for b in binary_codes_cool)
print(decoded_text)