import random

alphabet2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet = {
    "a" : 0,
    "b" : 1,
    "c":2,
    "d":3,
    "e":4,
    "f":5,
    "g":6,
    "h":7,
    "i":8,
    "j":9,
    "k":10,
    "l":11,
    "m":12,
    "n":13,
    "o":14,
    "p":15,
    "q":16,
    "r":17,
    "s" :18,
    "t" :19,
    "u" :20,
    "v" :21,
    "w" :22,
    "x" :23,
    "y" :24,
    "z" :25,
}
random_number = random.randint(0,25)
random_letter = alphabet2[random_number]


def game(attemps):
    while attemps > 0:
        guess = input("What is your guess? ")
        if guess in alphabet2:
            if alphabet[guess] > random_number:
                print("Further down!")
                attemps -= 1
            elif alphabet[guess] < random_number:
                print("Further up!")
                attemps -= 1
            else:
                print("Correct!!!")
                print("You needed", 12 - attemps, "attempts to win!")
        else:
            print("That's not in the alphabet!!!")
    print("No more attempts!!!")
    print("It was", random_letter)
    game_restart()

def game_restart():                                                 #ziet of de speler wil herstarten
    restart = input("Do you want to play again? (yes or no) ")
    if restart.lower() == "yes":
        game(5)
    elif restart.lower() == "no":
        print("Toodles")
        exit()
    else:                                                           #vraagt opniew als de speler een onbekend antwoord ingeeft
        print("I don't understand")
        game_restart()

input("What is your name? ")
game(12)
