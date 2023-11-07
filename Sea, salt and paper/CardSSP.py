class Card:
        TYPES = *['crab']*9, *['octopus']*5, *['sailors']*2, *['penguins']*3, *['shells']*6, *['swimmer']*5, *['fish']*7, *['ship']*8, \
                'lighthouse', 'school of fish', 'penguin colony', 'captain', *['sharks']*5, *['mermaids']*4
        COLORS = ["Blue", 'blue', 'black', 'yellow', 'light green', 'white', 'purple', 'light gray', 'light orange', 'light rose', 'orange']
        COLOR_LETTERS = {"B": 'Blue', 'b': 'blue', 'bl': 'black', 'y': 'yellow', 'lg': 'light green', 'w': 'white', 'p': 'purple',
                         'lgr': 'light gray', 'lo': 'light orange', 'lr': 'light rose', 'o': 'orange'}

        def __init__(self, types, color):
                if types in Card.TYPES:
                        self.types = types
                if color in Card.COLORS:
                        self.color = color
                else:
                        raise ValueError(f'Wrong color {color}')

        def __repr__(self):
                return f'{self.types} {self.color}'

        def __eq__(self, other):
                return self.color == other.color and self.types == other.types

        # def accept(self, top_card):
        #         """Возвр. True если можно сыграть пару карт"""
        #         return self.color == top_card.color or self.types == top_card.types

        @staticmethod
        def create(text: str):
                """ По тексту вида 'crab_b' возвращается карта Card('crab', 'blue') """
                letter = ''   # Card.COLOR_LETTERS.get(text[0], None)
                types = ''
                inserting = False
                for i in text:
                        if i == '_':
                                inserting = True
                                continue
                        if not inserting:
                                types += i
                        else:
                                letter += i
                letter1 = Card.COLOR_LETTERS.get(letter, None)
                # print(types, letter)
                return Card(types, letter1)

        @staticmethod
        def card_list(text: str):
                """ Из строки вида 'crab_w, fish_b, ship_B' возвращает список соотв. карт"""
                return [Card.create(word) for word in text.split()]

        @staticmethod
        def all_cards():
                """ Все карты для создания колоды"""
                return [Card(types, color) for color in Card.COLORS for types in Card.TYPES]

#print(Card.create('crab_b'))
