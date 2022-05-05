from player import Player
from dealer import Dealer
from print_players import ft_print_players

def ft_results(players, dealer):
	deal_res = max(dealer.count)
	for play in players:
		res = play.count[0]
		for item in play.count:
			if item > res and item <= 21:
				res = item
		if res > 21:
			res = "BUST"
		play.result = res
	ft_print_players(players, dealer, 4)
	if deal_res > 21:
		for play in players:
			if play.result == "BUST":
				play.money += play.bet
				print(f"{play.name} get back his bet.")
			else:
				play.money += 2 * play.bet
				print(f"{play.name} won!")
			play.reset_hand()
	elif deal_res == 21:
		for play in players:
			if play.result == 21:
				if len(play.cards) == 2:
					play.money += 2 * play.bet
					print(f"{play.name} won!")
				else:
					play.money += play.bet
					print(f"{play.name} get back his bet.")
			else:
				print(f"{play.name} lost.")
			play.reset_hand()
	else:
		for play in players:
			if play.result == "BUST" or play.result < deal_res:
				print(f"{play.name} lost.")
			elif play.result == deal_res:
				play.money += play.bet
				print(f"{play.name} get back his bet.")
			else:
				play.money += 2 * play.bet
				print(f"{play.name} won!")
			play.reset_hand()