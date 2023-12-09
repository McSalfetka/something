from __future__ import annotations

from CardSSP import Card
from HandSSP import Hand


class Player:
    def __init__(self, name: str, cards: list[Card]):
        self.name = name
        self.hand = Hand(cards)

    def __repr__(self):
        return f'{self.name}: {self.hand}'

    def save(self) -> dict:
        return {
            'name': self.name,
            'hand': repr(self.hand)
        }

    def has_playable_cards(self):
        """ Проверяем, есть ли на руке подходящие для игры на top карты. """
        return self.hand.get_playable_cards()

    def play_card(self, card: Card):
        """ Играется карта card с руки."""
        self.hand.remove_card(card)

    def add_card_to_hand(self, card: Card):
        self.hand.add_card(card)


# text = 'crab_b1 mermaids_w fish_b1 crab_o fish_lg'
# h = list(Hand(Card.card_list(text)))
# print(h)
# p = Player('Joe', h)
# print(p)
# cl = p.has_playable_cards()
# print(cl)
