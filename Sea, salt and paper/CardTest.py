import pytest
from CardSSP import Card


def test_card():
    c = Card('crab', 'blue')
    assert c.types == 'crab'
    assert c.color == 'blue'


def test_create():
    c = Card.create('crab_b1')
    assert c == Card('crab', 'blue')
    assert str(c) == 'crab_b1'
    assert c.types == 'crab'
    assert c.color == 'blue'


def test_create_card_list():
    text = 'crab_w fish_b1 ship_B'
    assert Card.card_list(text) == [Card("crab", 'white'), Card("fish", 'blue'), Card("ship", 'Blue')]


def test_create_wrong_color():
    with pytest.raises(ValueError):
        c = Card.create('crab_n')

