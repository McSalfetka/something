from CardSSP import Card
from DeckSSP import Deck, Heap

def test_deck():
    text = 'crab_b1 mermaids_w fish_b1 crab_o fish_lg'
    card_list = Card.card_list(text)
    deck = Deck(card_list)
    assert text == str(deck)

def test_draw():
    text = 'crab_b1 mermaids_w fish_b1 crab_o fish_lg'
    deck = Deck(Card.card_list(text))
    assert text == str(deck)

    c = deck.draw()
    assert 'crab_b1 mermaids_w fish_b1' == str(deck)
    assert c == [Card('crab', 'orange'), Card('fish', 'light green')]

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
    print(*c)
    assert 'ship_B ship_b1 fish_lg' == str(heap)
    assert c == [Card('fish', 'black')]
    assert c1 == Card('fish', 'light green')
