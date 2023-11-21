import pytest
from HandSSP import Hand
from CardSSP import Card

def test_hand():
    text = 'crab_b1 mermaids_w fish_b1 crab_o fish_lg'
    hand = Hand(Card.card_list(text))
    assert text == str(hand)

def test_gpc():
    c = 'crab_b1 mermaids_w fish_b1 crab_o fish_lg'
    hand = Hand(Card.card_list(c))
    cl = hand.get_playable_cards(Card('fish', 'blue'))
    assert cl == [Card.create('fish_b1'), Card.create('fish_lg')]

def test_remove_card():
    text = 'crab_b1 mermaids_w fish_b1 crab_o'
    hand = Hand(Card.card_list((text)))
    hand.remove_card(Card("crab", 'blue'))
    assert str(hand) == 'mermaids_w fish_b1 crab_o'
    hand.remove_card(Card("crab", 'orange'))
    assert str(hand) == 'mermaids_w fish_b1'

def test_len():
    text = 'crab_b1 mermaids_w fish_b1'
    hand = Hand(Card.card_list(text))
    assert len(hand) == 3

def text_index():
    text = 'crab_b1 mermaids_w fish_b1 crab_o fish_lg'
    hand = Hand(Card.card_list(text))
    assert hand[0] == Card('crab', 'blue')
    assert hand[1] == Card('fish', 'blue')
    assert hand[2] == Card('fish', 'light green')