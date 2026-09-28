import random

random_number = random.randint(0,10)
new_attempts = 5



def game(attempts):
    while attempts > 0:                                             #ziet of er nog pogingen zijn
        try:
            player_guess = int(input("What is your guess? "))       #vraagt om een gok
            if player_guess > random_number:                        #ziet of de gok juist was en zegt hoger of lager
                print("Too high")
                attempts -= 1
            elif player_guess < random_number:
                print("Too low")
                attempts -= 1
            else:
                print("You win!!!")
                print("You needed", 5-attempts, "attempts to win!")
                game_restart()
        except ValueError:                                          #Stopt de gok als het geen getal is
            print("Not a number IDIOT!!!")
    print("No more attempts!")
    print("It was",random_number)
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


naam = input("What is your name? ")
game(new_attempts)