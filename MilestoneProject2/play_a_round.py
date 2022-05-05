from deck import Deck
from player import Player
from print_players import ft_print_players

def ft_hit_or_stand(play):
    if play.stand == True:
        return True
    while True:
        ans = input(f"{play.name}, hit or stand? ")
        if ans == "hit":
            return False
        if ans == "stand":
            return True
        print("Please enter a valid answer.")

def ft_play_a_round(players, deck, dealer):
    for item in players:
        item.stand = ft_hit_or_stand(item)
        if not item.stand:
            item.new_card(deck)
            if min(item.count) >= 21:
                item.stand = True
        ft_print_players(players, dealer, 2)
    for item in players:
        if item.stand == False:
            return 1
    return 0