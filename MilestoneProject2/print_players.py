from player import Player
from dealer import Dealer

def ft_print_players(players, dealer, mode):
	nb = len(players)
	if (nb > 0):
		line = "=" * 30
		line += " "
		line *= nb
		print(line)
		s = ""
		for play in players:
			s += f"{play.name:{30}} "
		print(s)
		s = ""
		for play in players:
			s += f"Money: ${play.money : <22} "
		print(s)
		s = ""
		for play in players:
			s += f"Bet  : ${play.bet : <22} "
		print(s)
		s = ""
		size = 0
		for play in players:
			size = max(size, play.size)
		for i in range(size):
			s = ""
			for play in players:
				if play.size > i:
					card = f"{play.cards[i][0] : <2} of {play.cards[i][1] : <2}"
					if i == 0:
						s += f"Hand : {card : <23} "
					else:
						s += f"       {card : <23} "
				else:
					s += " " * 31
			print(s)
		if players[0].size > 0:
			s = ""
			for play in players:
				count = str(play.count)
				s += f"Count: {count : <23} "
			print(s)
		if players[0].result != None:
			s = ""
			for play in players:
				res = str(play.result)
				s += f"Result: {res : <22} "
			print(s)
		print(line)
		if mode == 1:
			dealer.print_dealer1()
		if mode == 2:
			dealer.print_dealer2()
		if mode == 3:
			dealer.print_dealer3()
		if mode == 4:
			dealer.print_dealer4()
		