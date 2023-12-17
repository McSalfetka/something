from __future__ import annotations

import json

from CardSSP import Card
from DeckSSP import Deck, Heap
from PlayerSSP import Player
from ScoreCountingSSP import Scoring
from PairEffects import PairsEff

class Game:
    DEFAULT_PLAYER_NAMES = ['Bob', 'Mike']

    def __init__(self, player_names: list[str] | None = None):
        if player_names is None:
            player_names = Game.DEFAULT_PLAYER_NAMES
        self.deck = Deck()
        self.players = [Player(name, Card.card_list(" "), 0, Card.card_list(" ")) for name in player_names]
        self.player_index = 0
        self.heap1 = Heap([self.deck.initialization()])
        self.heap2 = Heap([self.deck.initialization()])

    @staticmethod
    def create(game_dict: dict):
        g = Game([])    # без игроков
        g.deck = Deck.create(game_dict['deck'])
        g.heap1 = Heap.create(game_dict['heaps']['heap1'])
        g.heap2 = Heap.create(game_dict['heaps']['heap2'])
        g.players = [Player(p['name'], Card.card_list(p['hand']), p['points'], Card.card_list(p['played'])) for p in game_dict['players']]
        g.player_index = int(game_dict['player_index'])
        return g

    @staticmethod
    def new_round():
        player_names = Game.DEFAULT_PLAYER_NAMES
        g = Game()
        g.deck = Deck()
        g.heap1 = Heap([g.deck.initialization()])
        g.heap2 = Heap([g.deck.initialization()])
        g.player_index = 0
        g.players = [Player(name, Card.card_list(""), 0, Card.card_list("")) for name in player_names]
        return g

    @property
    def current_player(self):
        return self.players[self.player_index]

    @property
    def else_player(self):
        return self.players[self.player_index+1]

    # Взятие карты в начале хода или дополнительного хода
    def drawing_card(self):
        ''' Взятие карты'''
        print('-'*20)
        print(self.current_player)
        top1 = self.heap1.top()
        top2 = self.heap2.top()
        print('Верхние карты сбросов')
        print(f'Top1: {top1}; Топ2: {top2}')
        print('Откуда берем карту 1: из колоды; 2) из 1 сброса; 3) из 2 сброса')
        Which_to_draw = Deck.choose()
        # Берем карту из колоды или из одной из стопок сброса
        if Which_to_draw == 1:
            card1 = self.deck.show()
            print(f'Карты на выбор {card1}')
            print('Выберите карту 1) первая; 2) вторая')
            card = Deck.draw(card1, Deck.choose())
            print(f'Взяли карту {card}')
            self.current_player.add_card_to_hand(card)
            print('Куда положить вторую карту: 1) первая стопка сброса; 2) вторая стопка сброса')
            Which_Draw = Deck.choose()
            card1 = ''.join(card1)
            if Which_Draw == 1:
                self.heap1.put(Card.create(card1))
            else:
                self.heap2.put(Card.create(card1))

        elif Which_to_draw == 2:
            card = self.heap1.draw()
            print(f'Взяли карту {card}')
            self.current_player.add_card_to_hand(*card)

        elif Which_to_draw == 3:
            card = self.heap2.draw()
            self.current_player.add_card_to_hand(*card)
            print(f'Взяли карту {card}')
        print(self.current_player.hand)

    # Украсть карту оппонента
    def Thief_thing(self):
        import random
        Thiefd_Card = random.choice(self.else_player.hand)
        self.else_player.hand.remove_card(Thiefd_Card)
        return Thiefd_Card

    # Взять карту из одного из 2 сбросов
    def draw_from_heap(self):
        print('-'*20)
        print('Из какого сброса взять карты')
        What_Heap = Deck.choose()
        if What_Heap == 1:
            h = self.heap1
        else:
            h = self.heap2
        print(h)
        print('Какую карту взять?(номер карты)')
        Which_Card = Deck.choose()
        CARD = h.draw_for_crabs(Which_Card-1)
        print(CARD)
        self.current_player.add_card_to_hand(CARD)
        print('-'*20)

    # Взятие карты из
    def run(self):
        print(self.deck)
        # print(type(self.current_player.hand))
        running = True
        while running:
            turn = True
            while turn:
                turn = False
            self.drawing_card()
            # print(type(self.current_player.hand))
            # self.current_player.hand = Card.card_list(self.current_player.hand)
            # конец раунда
            Scores = Scoring(Card.card_list(str(self.current_player.hand)))
            InHandPoints = Scores.Score_count()
            if InHandPoints >= 7:
                print('-'*20)
                print('Закончить раунд? 1) Нет; 2) да; 3) All in')
                End_of_round = Deck.choose()
                # Завершение раунда, подсчет и запись очков
                if End_of_round == 2:
                    self.current_player.add_points(InHandPoints)
                    Else_Scores = Scoring(Card.card_list(str(self.else_player.hand)))
                    ElseInHand = Else_Scores.Score_count()
                    self.else_player.add_points(ElseInHand)
                    return

            # играем пары
            print('-'*20)
            print(self.current_player)
            cards = self.current_player.has_playable_cards()
            while bool(cards):
                cards = self.current_player.has_playable_cards()
                print(f'Доступные карты: {cards}')
                print('Играть пары? 1) Да; 2) Нет')
                PlayPair = Deck.choose()
                if cards and PlayPair == 2:
                    print(f'{self.current_player.name} пасует')
                    break

                print('Какую пару сыграть?(номер пары)')
                WhichPair = Deck.choose()
                if PlayPair > 0 and PlayPair <= len(cards)+1:
                    # print(self.current_player.hand)
                    print('Выбранная пара')
                    # print(cards[WhichPair-1])
                    self.current_player.play_card(Card.create(cards[WhichPair-1][0]))
                    self.current_player.play_card(Card.create(cards[WhichPair-1][1]))
                    Scores.Score_from_pair()
                    Eff = PairsEff(cards[WhichPair-1])
                    Reaction = Eff.pair_react()

                    if Reaction == 'Card_From_Heap':
                        self.draw_from_heap()
                    elif Reaction == 'Addition_turn':
                        self.drawing_card()
                    elif Reaction == 'Card_From_Library':
                        print('-'*20)
                        print('Полученная карта')
                        c = self.deck.draw_for_fish()
                        print(c)
                        self.current_player.add_card_to_hand(c)
                    else:
                        c = self.Thief_thing()
                        print(f'Украденная карта {c}')
                        self.current_player.add_card_to_hand(c)

                    cards.pop(WhichPair-1)
                else:
                    print('Пары с указанным номером нет')
            else:
                print(f'{self.current_player.name} пасует')
            print(self.current_player)

            # проверяем условие победы, если победили, выходим с индексом игрока
            if self.current_player.enough_points():
                return

            self.next_player()

    def next_player(self):
        """ Переходим к следующему игроку. """
        self.player_index = (self.player_index + 1) % len(self.players)

    def congratulations(self):
        print(f'THE END! Winner {self.current_player.name}')




def new_game():
    from random import seed
    seed(7)
    g = Game(['Bob', 'Mike'])
    g.run()
    g.congratulations()

def load_game(filename: str):
    with open(filename) as fin:
        d2 = json.load(fin)
    g = Game.create(d2)
    g.run()
    g.congratulations()


if __name__ == '__main__':
    load_game('data.json')


