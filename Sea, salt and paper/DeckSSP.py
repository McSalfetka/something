from __future__ import annotations

import random

from CardSSP import Card


class Deck:
    """ Колода карт"""

    def __init__(self, cards: list[Card] | None = None):
        if cards is None:
            self.cards = Card.all_cards()
            random.shuffle(self.cards)
        else:
            self.cards = cards

    def __repr__(self):
        """ crab_b1 mermaids_w fish_b1 crab_o fish_lg """
        return ' '.join([str(c) for c in self.cards])

    def show(self):
        """ Взяли из колоды 1 карту и вернули ее."""
        cards = self.cards[:2]
        self.cards = self.cards[2:]
        return [str(c) for c in cards]

    @staticmethod
    def draw(spisok: list, Wth: int):
        cards = spisok
        if Wth == 0:
            card = cards[0]
        else:
            card = cards[1]
        return card

    @staticmethod
    def create(text: str):
        return Deck(Card.card_list(text))


class Heap:
    def __init__(self, cards=None):
        self.cards = [] if cards is None else cards

    def __repr__(self):
        return ' '.join([str(c) for c in self.cards]) # repr(self.top()) if self.cards else 'Empty heap' # это выведет первую карту

    def top(self) -> Card:
        """ Верхняя карта сброса. """
        return self.cards[-1] if self.cards else None

    def put(self, card: Card):
        self.cards.append(card)

    def draw(self):
        card = self.cards[-1:]
        self.cards = self.cards[:-1]
        return card

    @staticmethod
    def create(text: str):
        return Heap(Card.card_list(text))


text = 'crab_b1 mermaids_w fish_b1 crab_o fish_lg'
deck = Deck(Card.card_list(text))
print(deck)
drawn = deck.show()
print(*drawn)
print(deck.draw(drawn, 1))
