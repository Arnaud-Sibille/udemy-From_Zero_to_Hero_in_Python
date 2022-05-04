from deck import Deck
from player import Player
from play_a_game import ft_play_a_game

def main():
    players = []
    ft_play_a_game(players)

'''
def main():
    players = []
    while ft_play_a_game(players):
        deck = Deck()
        deck.shuf()
        ft_first_round(players, deck)
        while ft_play_a_round(players, deck) != 0:
            pass
'''
if __name__ == "__main__":
    main()























