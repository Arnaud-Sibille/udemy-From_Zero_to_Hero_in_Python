import random

class Deck:
    def __init__(self, size = 52):
        self.cards = []
        self.size = size
        if (size != 0):
            for i in range(1, 14):
                self.cards.append((i, "Hearts"))
            for i in range(1, 14):
                self.cards.append((i, "Clubs"))
            for i in range(1, 14):
                self.cards.append((i, "Diamonds"))
            for i in range(1, 14):
                self.cards.append((i, "Spades"))

    def __str__(self):
        s = ""
        for i in self.cards:
            s += str(i[0]) + " of " + str(i[1]) + "\n"
        s = s[:-1]
        return s

    def shuf(self):
        random.shuffle(self.cards)

    def draw_a_card(self):
        if (self.size > 0):
            self.size -= 1
            return self.cards.pop(0)
        return None

class Player(Deck):
    def __init__(self, name, money):
        Deck.__init__(self, 0)
        self.name = name
        self.money = money
        self.count = [0]

    def add_money(self, amount):
        self.money += amount

    def rem_money(self, amount):
        self.money -= amount

    def new_card(self, deck):
        new_card = deck.draw_a_card()
        if new_card != None:
            self.size += 1
            self.cards.append(new_card)
            self.add_count(new_card)
            return new_card
        print("No more cards in the deck.")

    def add_count(self, new_card):
        pass

    def reset_hand(self):
        self.count = [0]
        self.cards = []
        self.size = 0

    def print_player(self):
        print(f"Name: {self.name}")
        print(f"Money: {self.money}$")
        print("Hand:")
        print(self)
        print("Count:")
        print(self.count)

def ft_add_player(players):
    while True:
        bol = True
        name = input("Please enter player name: ")
        for item in players:
            if (item.name == name):
                print("Already existing name.")
                bol = False
        if bol:
            break
    while True:
        try:
            money = int(input("Please enter the amount of money: "))
            break
        except:
            print("Please enter a valid amount.")
    play = Player(name, money)
    players.append(play)

def ft_rem_player(players):
    name = input("Please enter player name: ")
    for item in players:
        if (item.name == name):
            if (item.money >= 0):
                print(f"The casino owes {name} {item.money}$.")
            else:
                print(f"{name} owes the casino {item.money}$.")
            print(f"{name} left the game.")
            return 0
    print(f"Failed to remove {name}.")

def ft_play_a_game(players):
    print("Hello everyone, who's up for a Blackjack game?")
    del_player = True
    while del_player:
        print(f"Currently there are {len(players)} players: ")
        for item in players:
            print(f"{item.name} : {item.money}$")
        while True:
            ans = input("Does a player wants to stop playing? (yes/no): ")
            if ans == "yes":
                ft_rem_player(players)
                break
            if ans == "no":
                del_player = False
                break
            print("Please enter a valid answer. ")
    new_player = True
    while new_player:
        print(f"Currently there are {len(players)} players: ")
        for item in players:
            print(f"{item.name} : {item.money}$")
        if len(players) >= 9:
            print("The max number of player is reached, no more player can be added.")
            new_player = False
            break
        while True:
            ans = input("Do you want to add a new player? (yes/no): ")
            if ans == "yes":
                ft_add_player(players)
                break
            if ans == "no":
                new_player = False
                break
            print("Please enter a valid answer. ")
    if len(players) > 0:
        print("Okay, let's start the game! ")
        return 1
    print("No more players, thank you for playing! ")
    return 0

def ft_first_round(players, deck):
    pass

def ft_play_a_round():
    pass

def main():
    pass

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























