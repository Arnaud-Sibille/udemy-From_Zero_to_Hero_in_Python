from deck import Deck
from player import Player
from dealer import Dealer
from play_a_game import ft_play_a_game
from first_round import ft_first_round
from play_a_round import ft_play_a_round
from dealer_play import ft_dealer_play
from results import ft_results

def main():
    players = []
    while ft_play_a_game(players):
        deck = Deck()
        dealer = Dealer()
        deck.shuf()
        ft_first_round(players, deck, dealer)
        while ft_play_a_round(players, deck, dealer) != 0:
            pass
        ft_dealer_play(dealer, deck)
        ft_results(players, dealer)

if __name__ == "__main__":
    main()























