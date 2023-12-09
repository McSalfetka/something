from __future__ import annotations

from CardSSP import Card


class Hand:
    """ Рука игрока"""
    def __init__(self, cardlist: list[Card] | None = None):
        # print(cardlist)
        self.cards = [] if cardlist is None else cardlist

    def __repr__(self):
        """ crab_b shells_B mermaid_w """
        return ' '.join([str(c) for c in self.cards])

    def __len__(self):
        """ Возвращает размер руки."""
        return len(self.cards)

    def __getitem__(self, item):
        """дает hand[i] и hand[i:j]"""
        return self.cards[item]
#
    def get_playable_cards(self):
        """ Возвращает список пар карт, которые можно было бы сыграть"""
        spis = []
        spisosn1 = self.cards.copy()
        spisosn2 = self.cards.copy()
        for card1 in spisosn1:
            n = spisosn1.index(card1)
            spisosn2.pop(0)
            for card2 in spisosn2:
                if Card.accept(Card.create(str(card1)), Card.create(str(card2))):
                    spis.append((str(card1), str(card2)))
        return spis

    def remove_card(self, card: Card):
        """ Удаляет из руки карту card (чтобы положить ее в отбой)"""
        self.cards.remove(card)

    def add_card(self, card: Card):
        """ Добавляет карту в руку. """
        self.cards.append(card)

    @staticmethod
    def create(text: str):
        return Hand(Card.card_list(text))


# text = 'swimmer_b1 crab_b1 mermaids_w fish_b1 crab_o fish_bl swimmer_B sharks_bl shells_bl shells_lg'
# h = Hand(Card.card_list(text))
# print(h)
# cl = h.get_playable_cards()
# print(cl)
