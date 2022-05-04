from deck import Deck
from player import Player

def ft_take_bet(play):
    while True:
        try:
            bet = int(input(f"{play.name} please enter your bet: "))
        except:
            print("Invalid bet")
        if (bet <= 0):
            print("Please enter a strictly positive number.")
        else:
            play.add_bet(bet)
            break
    
def ft_first_round(players, deck, dealer):
    for item in players:
        ft_take_bet(item)
    print("Alright let's play the first round.")
    for item in players:
        item.new_card(deck)
        item.print_player()
    dealer.new_card(deck)
    dealer.print_dealer1()
    for item in players:
        item.new_card(deck)
        item.print_player()
    dealer.new_card(deck)
    dealer.print_dealer2()