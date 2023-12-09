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
    assert text == str(deck)

    taken = deck.show()
    assert ' '.join(taken) == 'crab_b1 mermaids_w'
    assert str(deck.draw(taken, 1)) == 'mermaids_w'
    assert str(deck.draw(taken, 0)) == 'crab_b1'


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
