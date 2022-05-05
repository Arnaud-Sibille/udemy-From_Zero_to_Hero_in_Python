from dealer import Dealer
from deck import Deck

def ft_dealer_play(dealer, deck):
	dealer.print_dealer3()
	while max(dealer.count) < 17:
		dealer.new_card(deck)
		dealer.print_dealer3()