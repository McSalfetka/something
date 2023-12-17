from HandSSP import Hand
from CardSSP import Card

class PairsEff:
    def __init__(self, pair: tuple):
        p1 = Card.create(pair[0])
        p2 = Card.create(pair[1])
        self.pair = (p1.types, p2.types)

    # def __repr__(self):
    #     return 'ДА'

    def pair_react(self):
        # print('s', self.pair)
        conclussion = ''
        if self.pair[0] == self.pair[1] == 'crab':
            conclussion = 'Card_From_Heap'
        elif self.pair[0] == self.pair[1] == 'fish':
            conclussion = 'Card_From_Library'
        elif self.pair[0] == self.pair[1] == 'ship':
            conclussion = 'Addition_turn'
        elif (self.pair[0] == 'swimmer' and self.pair[1] == 'sharks')\
                or (self.pair[0] == 'sharks' and self.pair[1] == 'swimmer'):
            conclussion = 'Thief_the_Card'
        return conclussion


# text = 'swimmer_b1 crab_b1 mermaids_w fish_b1 crab_o fish_bl swimmer_B sharks_bl shells_bl shells_lg'
# h = Hand(Card.card_list(text))
# print(h)
# cl = h.get_playable_cards()
# print('s', type(Card.create(cl[0][0])))
# print(cl[0])
# print(type(cl[0]))
# p = PairsEff(cl[0])
# print(p.pair_react())
