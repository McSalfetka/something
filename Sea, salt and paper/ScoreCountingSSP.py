from __future__ import annotations
from CardSSP import Card

class Scoring:
    def __init__(self, cardlist: list[Card] | None = None):
        self.cards = [] if cardlist is None else cardlist
        self.counters = 0

    def __repr__(self):
        # print(len(self.cards))
        return self.counters

    def Score_from_pair(self):
        self.counters += 1

    def max_color(self):
        from collections import Counter
        Ccard = [card.color for card in self.cards]
        Ccard = Counter(Ccard)
        # print(Ccard)
        max_key = max(Ccard, key=Ccard.get)
        self.counters = Ccard[max_key]
        return self.counters

    def Score_count(self):
        tcards = [card.types for card in self.cards]
        mermaids = 0
        sailors = 0
        shells = 0
        penguins = 0
        octopus = 0
        fish = 0
        ships = 0
        # print('2', fcards)
        for i in tcards:
            if i == 'mermaids':
                mermaids += 1
            elif i == 'sailors':
                sailors += 1
            elif i == 'shells':
                shells += 1
            elif i == 'penguins':
                penguins += 1
            elif i == 'octopus':
                octopus += 1
            elif i == 'fish':
                fish += 1
            elif ships == 'ship':
                ships += 1
        if mermaids == 4:
            self.counters = 99999999
            return self.counters
        # for i in range(octopus):
        if octopus > 0:
            self.counters += (octopus-1)*3
        # for i in range(shells):
        if shells > 0:
            self.counters += (shells-1)*2
        # for i in range(sailors):
        if sailors > 0:
            self.counters += (sailors-1)*5
        if 'captain' in tcards:
            self.counters += 3*sailors

        if 'lighthouse' in tcards:
            self.counters += ships
        if 'SchoolOfFish' in tcards:
            self.counters += fish
        if penguins != 0:
            if penguins == 1:
                self.counters += 1
            elif penguins == 2:
                self.counters += 3
            else:
                self.counters += 5
            if 'PenguinColony' in tcards:
                self.counters += penguins*2

        if mermaids != 0:
            from collections import Counter
            Ccard = [card.color for card in self.cards]
            Ccard = Counter(Ccard)
            # print(Ccard)
            for i in range(mermaids):
                if len(Ccard) > 0:
                    max_key = max(Ccard, key=Ccard.get)
                    self.counters += Ccard[max_key]
                    del Ccard[max_key]
        return self.counters


text = 'captain_lo shells_bl sailors_o penguins_lr fish_b1 sailors_lr'
score = Scoring(Card.card_list(text))
print(score.Score_count())
