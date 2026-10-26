import random

def draw_start_cards(total_dealer,total_player):
    card_player_1 = random.randint(1,13)
    card_player_2 = random.randint(1,13)
    card_dealer_1 = random.randint(1,13)
    total_player = card_player_2 + card_player_1
    return total_player, card_dealer_1

def hit(total):
    total += random.randint(1,13)
    return total

def end_game(total_player,total_dealer):
    print("Dealers Hand:",total_dealer,"\nYour Hand:",total_player)
    if total_player > 21:
        print("Dealer wins!")
    elif total_dealer > 21:
        print("You win!")
    elif total_dealer == 21:
        print("Dealer wins!")
    elif total_player == 21:
        print("You win!")
    elif total_player > total_dealer:
        print("You win!")
    elif total_dealer > total_player:
        print("Dealer wins!")


def dealer_turn(total_dealer,total_player):
    if total_dealer < 17:
        total_dealer = hit(total_dealer)
        dealer_turn(total_dealer,total_player)
    elif total_dealer >= 17:
        end_game(total_player,total_dealer)

def player_turn(total_player, total_dealer):
    print("Dealers Hand:",total_dealer,"\nYour Hand:",total_player)
    if total_player > 21 or total_dealer > 21:
        end_game(total_player,total_dealer)
        return
    hit_stand = input("Hit or Stand? ")
    if hit_stand.lower() == "hit":
        total_player = hit(total_player)
        if total_player > 21:
            end_game(total_player,total_dealer)
            return
        player_turn(total_player,total_dealer)
    elif hit_stand.lower() == "stand":
        dealer_turn(total_dealer,total_player)

play, deal = draw_start_cards(0,0)
player_turn(play, deal)