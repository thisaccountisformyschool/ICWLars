# De initiële lijst met binaire codes. Pas deze niet aan!
binary_codes = [
    "00100001",
    "10100001",
    "11001100",
    "01100110",
    "11001100",
    "11110000",
    "01101100",
    "10110100",
    "01100011",
    "10110100",
    "01110100",
    "11100000",
    "01100100",
]

# Hieronder plaats je alle code om de binary_codes aan te passen

binary_codes2 = []

binary_codes.remove("11110000")
binary_codes.pop(1)
binary_codes.append("01000111")
binary_codes.insert(9,"11001100")
binary_codes.insert(9,"11001100")
print(binary_codes)
last = binary_codes[len(binary_codes)-1]
first = binary_codes[0]
binary_codes.pop(len(binary_codes)-1)
binary_codes.pop(0)
binary_codes.append(first)
binary_codes.insert(0,last)

print(binary_codes)

for i in binary_codes:
    if i == "11001100":
        binary_codes2.append("01100101")
    elif i == "10110100":
        binary_codes2.append("01101001")
    elif i == "11100000":
        binary_codes2.append("01110010")
    else:
        binary_codes2.append(i)


# De code hieronder vertaalt je huidige binaire code naar ascii-karacters.
decoded_text = ''.join(chr(int(b, 2)) for b in binary_codes2)
print(decoded_text)

