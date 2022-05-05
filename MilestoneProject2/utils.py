def get_ans1():
	while True:
		ans = input("Does a player wants to stop playing? (yes/no): ")
		if ans == "yes":
			return "yes"
		if ans == "no":
			return "no"
		print("Please enter a valid answer.")

def get_ans2():
	while True:
		ans = input("Do you want to add a new player? (yes/no): ")
		if ans == "yes":
			return "yes"
		if ans == "no":
			return "no"
		print("Please enter a valid answer.")

def get_ans3(players):
	while True:
		bol = True
		name = input("Please enter player name: ")
		for item in players:
			if item.name == name:
				print("Already existing name.")
				bol = False  
		if len(name) > 20:
			print("Please no more than 20 characters")
			bol = False
		if bol:
			return name

def get_ans4():
	while True:
		try:
			money = int(input("Please enter the amount of money: "))
			if money >= 2 and money <= 100000:
				return money
			print("Please enter an amount between 2 and 100000")
		except:
			print("Please enter a valid amount.")


