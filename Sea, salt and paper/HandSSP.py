from __future__ import annotations

from CardSSP import Card


class Hand:
    """ Рука игрока"""
    def __init__(self, cardlist: list[Card] | None = None):
        # print(cardlist)
        self.cards = [] if cardlist is None else cardlist

    def __repr__(self):
        """ r4 y9 b1 b0 """
        return ' '.join([str(c) for c in self.cards])

    def __len__(self):
        """ Возвращает размер руки."""
        return len(self.cards)

    def __getitem__(self, item):
        """дает hand[i] и hand[i:j]"""
        return self.cards[item]

    def get_playable_cards(self, some: Card):
        """ Возвращает список пар карт, которые можно было бы сыграть"""
        return [card for card in self.cards if some.accept(card)]

    def remove_card(self, card: Card):
        """ Удаляет из руки карту card (чтобы положить ее в отбой)"""
        self.cards.remove(card)

    def add_card(self, card: Card):
        """ Добавляет карту в руку. """
        self.cards.append(card)

    @staticmethod
    def create(text: str):
        return Hand(Card.card_list(text))


#
