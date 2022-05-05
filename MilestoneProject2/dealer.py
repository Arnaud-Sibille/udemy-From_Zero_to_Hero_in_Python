from player import Player

class Dealer(Player):
	def __init__(self):
		Player.__init__(self, "Dealer", 0)

	def print_dealer1(self):
		line = "=" * 30
		print(line)
		print("Dealer:")
		print(f"        {self.cards[0][0]: <2} of {self.cards[0][1]}")
		print(line)

	def print_dealer2(self):
		line = "=" * 30
		print(line)
		print("Dealer:")
		print(f"        {self.cards[0][0]: <2} of {self.cards[0][1]}")
		print("        Unknown card")
		print(line)

	def print_dealer3(self):
		line = "=" * 30
		print(line)
		print("Dealer:")
		for item in self.cards:
			print(f"        {item[0]: <2} of {item[1]}")
		print(f"Count:  {(self.count)}")
		print(line)

	def print_dealer4(self):
		line = "=" * 30
		print(line)
		print("Dealer:")
		for item in self.cards:
			print(f"        {item[0]: <2} of {item[1]}")
		print(f"Count:  {(self.count)}")
		res = max(self.count)
		if res > 21:
			res = "BUST"
		print(f"Result:  {res}")
		print(line)