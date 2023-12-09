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


def test_accept():
    t1 = Card.create('fish_b1')
    t2 = Card.create('fish_bl')
    t3 = Card.create('swimmer_b1')
    t4 = Card.create('sharks_bl')
    t5 = Card.create('sharks_B')
    assert Card.accept(t1, t2)
    assert not Card.accept(t2, t3)
    assert not Card.accept(t1, t3)
    assert Card.accept(t3, t4)
    assert Card.accept(t4, t3)
    assert not Card.accept(t4, t5)
