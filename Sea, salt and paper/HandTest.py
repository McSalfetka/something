import pytest
from HandSSP import Hand
from CardSSP import Card

def test_hand():
    text = 'crab_b mermaids_w fish_b crab_o fish_lg'
    hand = Hand(Card.card_list(text))
    assert text == str(hand)

def test_gpc():
    c = 'crab_b mermaids_w fish_b crab_o fish_lg'
    hand = Hand(Card.card_list(c))
    cl = hand.get_playable_cards(Card('fish', 'blue'))
    assert cl == [Card.create('fish_b'), Card.create('fish_lg')]
