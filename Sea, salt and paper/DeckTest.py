from CardSSP import Card
from DeckSSP import Deck, Heap


def test_deck():
    text = 'crab_b1 mermaids_w fish_b1 crab_o fish_lg'
    card_list = Card.card_list(text)
    deck = Deck(card_list)
    print(type(deck))
    print(deck)
    assert text == str(deck)


def test_draw():
    text = 'crab_b1 mermaids_w fish_b1 crab_o fish_lg'
    deck = Deck(Card.card_list(text))

    taken = deck.show()
    assert ' '.join(taken) == 'crab_b1 mermaids_w'
    assert str(deck.draw(taken, 1)) == 'mermaids_w'
    assert str(deck.draw(taken, 0)) == 'crab_b1'

def test_draw_for_fish():
    text = 'crab_b1 mermaids_w fish_b1 crab_o fish_lg'
    deck = Deck(Card.card_list(text))
    taken = deck.draw_for_fish()
    assert str(taken) == 'crab_b1'
    assert str(deck) == 'mermaids_w fish_b1 crab_o fish_lg'

def test_draw_for_crabs():
    text = 'crab_b1 mermaids_w fish_b1'
    heap = Heap(Card.card_list(text))
    take = heap.draw_for_crabs(1)
    assert str(take) == 'mermaids_w'
    assert str(heap) == 'crab_b1 fish_b1'

def test_heap():
    text = 'ship_B ship_b1 fish_lg fish_bl'
    card_list = Card.card_list(text)
    heap = Heap(card_list)
    assert str(heap) == 'ship_B ship_b1 fish_lg fish_bl'

def test_draw_from_util():
    text = 'ship_B ship_b1 fish_lg fish_bl'
    heap = Heap(Card.card_list(text))
    c = heap.draw()
    c1 = heap.top()
    assert 'ship_B ship_b1 fish_lg' == str(heap)
    assert c == [Card('fish', 'black')]
    assert c1 == Card('fish', 'light green')

def test_chosen_draw():
    text = 'crab_b1 mermaids_w fish_b1 crab_o fish_lg'
    deck = Deck(Card.card_list(text))
    c = Deck.choose(1)
    taken = deck.show()
    print(taken[c])
    assert str(deck.draw(taken, c)) == taken[c]

def test_initialization():
    text = 'crab_b1 mermaids_w fish_b1 crab_o fish_lg'
    deck = Deck(Card.card_list(text))
    card = deck.initialization()
    heap = Heap(Card.card_list(str(card)))
    assert str(card) == 'crab_b1'
    assert str(heap) == 'crab_b1'
    assert str(deck) == 'mermaids_w fish_b1 crab_o fish_lg'
