from player import Player

class Dealer(Player):
	def __init__(self):
		Player.__init__(self, "Dealer", 0)

	def print_dealer1(self):
		print("--------------")
		print("Dealer:")
		print(f"{self.cards[0][0]} of {self.cards[0][1]}")
		print("--------------")

	def print_dealer2(self):
		print("--------------")
		print("Dealer:")
		print(f"{self.cards[0][0]} of {self.cards[0][1]}")
		print("Unknown card")
		print("--------------")