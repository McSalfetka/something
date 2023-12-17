from __future__ import annotations

from CardSSP import Card
from HandSSP import Hand


class Player:
    def __init__(self, name: str, cards: list[Card], points: int, played: list[Card]):
        self.name = name
        self.hand = Hand(cards)
        self.points = points
        self.played = played

    def __repr__(self):
        p = ' '.join([str(c) for c in self.played])
        return f'{self.name}: \n рука: {self.hand} \n количество очков: {self.points} \n отыграно: {p}'

    def save(self) -> dict:
        return {
            'name': self.name,
            'hand': repr(self.hand),
            'points': repr(self.points),
            'played': repr(self.played)
        }

    def has_playable_cards(self):
        """ Проверяем, есть ли на руке подходящие для игры на top карты. """
        return self.hand.get_playable_cards()

    def play_card(self, card: Card):
        """ Играется карта card с руки."""
        self.hand.remove_card(card)
        self.played.append(card)


    def add_card_to_hand(self, card: Card):
        self.hand.add_card(card)

    def add_points(self, number: int):
        self.points += number

    def enough_points(self) -> bool:
        return self.points >= 40

    # def add_to_played(self, card1: Card, card2: Card):
    #     self.played.append(card1)
    #     self.played.append(card2)

# text = 'swimmer_b1 crab_b1 mermaids_w fish_b1 crab_o fish_bl swimmer_B sharks_bl shells_bl shells_lg'
# h = list(Hand(Card.card_list(text)))
# print(h)
# p = Player('Joe', h)
# print(p)
# cl = p.has_playable_cards()
# print(cl)

