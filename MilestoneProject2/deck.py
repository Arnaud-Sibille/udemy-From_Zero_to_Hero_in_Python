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
