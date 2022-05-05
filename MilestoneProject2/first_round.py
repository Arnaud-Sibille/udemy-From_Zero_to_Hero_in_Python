from deck import Deck
from player import Player
from print_players import ft_print_players

def ft_take_bet(play):
    while True:
        try:
            bet = int(input(f"{play.name} please enter your bet: "))
        except:
            print("Invalid bet")
        if (bet < 2):
            print("Please enter a minimum amount of 2.")
        elif (bet > play.money):
            print("You don't have enough money, please enter a reasonable amount.")
        else:
            play.add_bet(bet)
            play.rem_money(bet)
            break
    
def ft_first_round(players, deck, dealer):
    for item in players:
        ft_take_bet(item)
    print("Alright let's play the first round.")
    for item in players:
        item.new_card(deck)
    dealer.new_card(deck)
    ft_print_players(players, dealer, 1)
    for item in players:
        item.new_card(deck)
    dealer.new_card(deck)
    ft_print_players(players, dealer, 2)