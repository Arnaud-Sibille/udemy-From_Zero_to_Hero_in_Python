from deck import Deck
from player import Player
from dealer import Dealer
from play_a_game import ft_play_a_game
from first_round import ft_first_round

def main():
    player1 = Player("Arnaud", 500)
    player2 = Player("Timmy", 500)
    players = [player1, player2]
    deck = Deck()
    dealer = Dealer()
    deck.shuf()
    ft_first_round(players, deck, dealer)

'''
def main():
    players = []
    while ft_play_a_game(players):
        deck = Deck()
        dealer = Dealer()
        deck.shuf()
        ft_first_round(players, deck, dealer)
        while ft_play_a_round(players, deck, dealer) != 0:
            pass
'''
if __name__ == "__main__":
    main()























