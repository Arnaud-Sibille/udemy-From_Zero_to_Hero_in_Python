from deck import Deck
from player import Player
from play_a_game import ft_play_a_game

def main():
    player1 = Player("Arnaud", 500)
    player2 = Player("Timmy", 500)
    players = [player1, player2]
    deck = Deck()
    deck.shuf()
    while min(player1.count) < 21:
        player1.new_card(deck)
        player1.print_player()

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























