from __future__ import annotations

import json

from CardSSP import Card
from DeckSSP import Deck, Heap
from PlayerSSP import Player
from ScoreCountingSSP import Scoring
from PairEffects import PairsEff
from HandSSP import Hand

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

    def start_round(self):
        self.deck = Deck()
        self.heap1 = Card.card_list('')
        self.heap2 = Card.card_list('')
        self.heap1 = Heap([self.deck.initialization()])
        self.heap2 = Heap([self.deck.initialization()])
        self.player_index = 0
        pointeses = {str(self.else_player.name): self.else_player.points, str(self.current_player.name): self.current_player.points}
        self.players = [Player(name, Card.card_list(''), pointeses.get(name), Card.card_list('')) for name in self.DEFAULT_PLAYER_NAMES]

    @property
    def current_player(self):
        return self.players[self.player_index]

    @property
    def else_player(self):
        return self.players[(self.player_index+1) % 2]

    # Взятие карты в начале хода или дополнительного хода
    def drawing_card(self):
        ''' Взятие карты'''
        print('-'*20)
        print(self.current_player)
        print('-'*20)
        top1 = self.heap1.top()
        top2 = self.heap2.top()
        print('Верхние карты сбросов')
        print(f'Top1: {top1}; Топ2: {top2}')
        print('-'*20)
        print('Откуда берем карту 1: из колоды; 2) из 1 сброса; 3) из 2 сброса')
        Which_to_draw = Deck.choose()
        print('-'*20)
        # Берем карту из колоды или из одной из стопок сброса
        if Which_to_draw == 1:
            card1 = self.deck.show()
            print(f'Карты на выбор {card1}')
            print('Выберите карту 1) первая; 2) вторая')
            card = Deck.draw(card1, Deck.choose())
            print('-'*20)
            print(f'Взяли карту {card}')
            print('-'*20)
            self.current_player.add_card_to_hand(Card.create(card))
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
        print('-'*20)
        print(self.current_player.hand)

    def PLAY_PAIRS(self, protection: bool | None = None):
        if protection is None:
            protection = False

        cards = self.current_player.has_playable_cards()
        if protection:
            for i in cards:
                c1 = Card.create(i[0])
                c2 = Card.create(i[1])
                cart = (c1.types, c2.types)
                if cart == ('sharks', 'swimmer') or cart == ('swimmer', 'sharks'):
                    cards.remove(i)

        while bool(cards):
            print(f'Доступные карты: {cards}')
            print('Играть пары? 1) Да; 2) Нет')
            PlayPair = Deck.choose()
            if cards and PlayPair == 2:
                print('-'*20)
                print(f'{self.current_player.name} пасует')
                print('-'*20)
                break

            print('Какую пару сыграть?(номер пары)')
            WhichPair = Deck.choose()
            if WhichPair > 0 and WhichPair <= len(cards)+1:
                print('Выбранная пара')
                print(*cards[WhichPair-1])
                self.current_player.play_card(Card.create(cards[WhichPair-1][0]))
                self.current_player.play_card(Card.create(cards[WhichPair-1][1]))
                # InHandPoints+=1
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
                print('-'*20)

                cards = self.current_player.has_playable_cards()
                if protection:
                    for i in cards:
                        cart = (i[0].types, i[1].types)
                        if cart == ('sharks', 'swimmer') and cart == ('swimmer', 'sharks'):
                            cards.remove(i)
                # cards.pop(WhichPair-1)

            else:
                print('Пары с указанным номером нет')
        else:
            print('-'*20)
            print(f'{self.current_player.name} пасует')
            print('-'*20)
        print(self.current_player)

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
        running = True
        self.start_round()
        while running:

            # Берем карту
            self.drawing_card()

            # конец раунда
            Scores = Scoring(Card.card_list(str(self.current_player.hand)))
            InHandPoints = Scores.Score_count()
            cards = self.current_player.has_playable_cards()
            InHandPoints += len(self.current_player.played)//2+len(cards)
            # print('-'*20)
            # print(self.current_player.name, InHandPoints)
            # print('-'*20)
            if InHandPoints >= 7:
                print('-'*20)
                print('Закончить раунд? 1) Нет; 2) Да; 3) Последний шанс')
                End_of_round = Deck.choose()
                # Завершение раунда, подсчет и запись очков
                if End_of_round == 2:
                    print(f'Игрок {self.current_player.name} объявляет Конец Раунда')
                    self.current_player.add_points(InHandPoints)
                    Else_Scores = Scoring(Card.card_list(str(self.else_player.hand)))
                    cards_else_player = len(self.else_player.has_playable_cards())
                    ElseInHand = Else_Scores.Score_count() + len(self.else_player.played)//2 + cards_else_player
                    self.else_player.add_points(ElseInHand)
                    print('-'*20)
                    print(f'Игрок {self.current_player.name} получил {InHandPoints} очков')
                    print(f'Игрок {self.else_player.name} получил {ElseInHand} очков')
                    print('-'*20)
                    print('новый раунд')
                    self.start_round()
                    continue
                if End_of_round == 3:
                    print(f'Игрок {self.current_player.name} объявляет Последний шанс')
                    addition_points = Scores.max_color()
                    print(f'Игрок {self.current_player.name} имеет {InHandPoints} очков, дополнительно он получит {addition_points}')

                    self.next_player()
                    print(f'Ходит {self.current_player.name}')
                    self.drawing_card()
                    self.PLAY_PAIRS(True)
                    S = Scoring(self.current_player.hand)
                    addition_points1 = S.max_color()
                    InHandPoints1 = S.Score_count() + len(self.current_player.played)//2+len(cards)
                    print(f'Игрок {self.current_player.name} имеет {InHandPoints1} очков')
                    # Если у первого игрока больше очков
                    if InHandPoints > InHandPoints1:
                        print(f'Игрок {self.else_player.name} получает {InHandPoints} + {addition_points} очков')
                        self.else_player.add_points(InHandPoints+addition_points)
                        print('-'*20)
                        print(f'Игрок {self.current_player.name} получает {addition_points1} очков за цвет')
                        self.current_player.add_points(addition_points1)
                    # Если у второго игрока больше очков
                    else:
                        print(f'Игрок {self.current_player.name} получает {InHandPoints1} очков')
                        print('-'*20)
                        self.current_player.add_points(InHandPoints1)
                        print(f'Игрок {self.else_player.name} получает {addition_points} очков за цвет')
                        self.else_player.add_points(addition_points)
                    self.start_round()
                    continue

            # играем пары
            self.PLAY_PAIRS()

            # проверяем условие победы, если победили, выходим с индексом игрока
            if self.current_player.enough_points() or self.else_player.enough_points():
                running = False

            self.next_player()
            print('-'*20)
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
    g = Game()
    g.run()
    g.congratulations()


if __name__ == '__main__':
    load_game('data.json')


