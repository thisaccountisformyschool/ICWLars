vowels = ["a","o","i","u","e"]
consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
def tel_lettergrepen(string):
    words = string.split()
    slyb_count = 0
    for word in words:
        slyb = False
        for letter in word:
            if letter in vowels:
                slyb = True
            elif letter in consonants:
                if slyb:
                    slyb = False
                    slyb_count += 1
            if letter == word[-1]:
                if slyb:
                    slyb = False
                    slyb_count += 1
    return slyb_count

def tel_woorden(string):
    words = string.split()
    aantal = len(words)
    return aantal+1

def alfabethicalizer(string):
    words = string.split()
    words.sort()
    return words

def palindromer(string):
    words = string.split()
    for word in words:
        reversed_letters = word.split()
        reversed_letters.sort(reverse=True)
        print(reversed_letters)
        reversed_word = "".join(reversed_letters)
        print(reversed_word)

def zinner(string):
    zin_tal = 0
    zin_tal += string.count(".")
    zin_tal += string.count("!")
    zin_tal += string.count("?")
    return zin_tal

def sentence_bot(string):
    print("Aantal lettergrepen:",tel_lettergrepen(string))
    print("Aantal woorden:",tel_woorden(string))
    print("Alfabetisch gerangschikt:",alfabethicalizer(string))
    print(palindromer(string))
    print("Aantal zinnen:",zinner(string))

string = input("Sentence: ")
sentence_bot(string)