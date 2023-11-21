class Card:
        TYPES = 'crab', 'octopus', 'sailors', 'penguins', 'shells', 'swimmer', 'fish', 'ship', \
                'lighthouse', 'SchoolOfFish', 'PenguinColony', 'captain', 'sharks', 'mermaids'

        COLORS = ["Blue", 'blue', 'black', 'yellow', 'light green', 'white', 'purple', 'light gray', 'light orange', 'light rose', 'orange']

        COLOR_LETTERS = {"B": 'Blue', 'b1': 'blue', 'bl': 'black', 'y': 'yellow', 'lg': 'light green', 'w': 'white', 'p': 'purple',
                         'lgr': 'light gray', 'lo': 'light orange', 'lr': 'light rose', 'o': 'orange'}

        def __init__(self, types, color):
                if types in Card.TYPES:
                        self.types = types
                if color in Card.COLORS:
                        self.color = color
                else:
                        raise ValueError(f'Wrong color {color}')

        def __repr__(self):
                keyk = ''
                for k, v in Card.COLOR_LETTERS.items():
                        if v == self.color:
                                keyk = k
                return f'{self.types}_{keyk}'

        def __eq__(self, other):
                return self.color == other.color and self.types == other.types

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
                return Card(types, letter1)

        @staticmethod
        def card_list(text: str):
                """ Из строки вида 'crab_w, fish_b1, ship_B' возвращает список соотв. карт"""
                return [Card.create(word) for word in text.split()]

        @staticmethod
        def all_cards():
                """ Все карты для создания колоды"""
                cards = []
                color = ''
                for j in Card.TYPES:
                        if j == 'mermaids':
                                color = 'white'
                                for i in range(4):
                                        cards.append(Card(j, color))
                        elif j == 'crab':
                                for k in Card.COLORS:
                                        if k == 'Blue' or k == 'blue' or k == 'yellow':
                                                for i in range(2):
                                                        cards.append(Card(j, k))
                                        elif k == 'black' or k == 'light green' or k == 'light gray':
                                                cards.append(Card(j, k))
                        elif j == 'shells':
                                for k in Card.COLORS:
                                        if k == 'Blue' or k == 'blue' or k == 'black' or k == 'light green' or k == 'light gray' or k == 'yellow':
                                                cards.append(Card(j, k))
                        elif j == 'fish':
                                for k in Card.COLORS:
                                        if k == 'black' or k == 'Blue':
                                                        for i in range(2):
                                                                cards.append(Card(j, k))
                                        elif k == 'blue' or k == 'light green' or k == 'yellow':
                                                cards.append(Card(j, k))
                        elif j == 'octopus':
                                for k in Card.COLORS:
                                        if k == 'blue' or k == 'light green' or k == 'light gray' or k == 'purple' or k == 'yellow':
                                                cards.append(Card(j, k))
                        elif j == 'penguin':
                                for k in Card.COLORS:
                                        if k == 'purple' or k == 'light rose' or k == 'light orange':
                                                cards.append(Card(j, k))
                        elif j == 'sailors':
                                cards.append(Card(j, 'light rose'))
                                cards.append(Card(j, 'orange'))
                        elif j == 'ship':
                                for k in Card.COLORS:
                                        if k == 'Blue' or k == 'blue' or k == 'black' or k == 'yellow':
                                                for i in range(2):
                                                        cards.append(Card(j, k))
                        elif j == 'swimmer':
                                for k in Card.COLORS:
                                        if k == 'Blue' or k == 'blue' or k == 'black' or k == 'light green' or k == 'purple':
                                                cards.append(Card(j, k))

                        elif j == 'sharks':
                                for k in Card.COLORS:
                                        if k == 'Blue' or k == 'blue' or k == 'black' or k == 'light orange' or k == 'yellow':
                                                cards.append(Card(j, k))
                        elif j == 'captain':
                                cards.append(Card(j, 'light orange'))
                        elif j == 'lighthouse':
                                cards.append(Card(j, 'purple'))
                        elif j == 'PenguinColony':
                                cards.append(Card(j, 'light green'))
                        elif j == 'SchoolOfFish':
                                cards.append(Card(j, 'light gray'))

                        elif j == 'penguins':
                                for k in Card.COLORS:
                                        if k == 'light rose' or k == 'light orange' or k == 'purple':
                                                cards.append(Card(j, k))

                return cards

        def accept(self, some):
                return self.types == some.types

