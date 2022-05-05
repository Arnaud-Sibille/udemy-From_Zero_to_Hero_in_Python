from deck import Deck

class Player(Deck):
    def __init__(self, name, money):
        Deck.__init__(self, 0)
        self.name = name
        self.money = money
        self.count = [0]
        self.bet = 0
        self.stand = False
        self.result = None
    
    def add_bet(self, amount):
        self.bet += amount

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
        value = new_card[0]
        new_count = []
        if value >= 10:
            value = 10
        if value != 1:
            for item in self.count:
                new_count.append(item + value)
        else:
            for item in self.count:
                new_count.append(item + 1)
                new_count.append(item + 11)
        self.count = new_count

    def reset_hand(self):
        self.count = [0]
        self.cards = []
        self.size = 0
        self.bet = 0
        self.stand = False
        self.result = None
