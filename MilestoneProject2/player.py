from deck import Deck

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
