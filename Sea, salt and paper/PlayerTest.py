import pytest

from PlayerSSP import Player
from CardSSP import Card



def test_player():
    pl_name = 'Joe'
    pl_cards = 'crab_b1 mermaids_w fish_b1 crab_o'
    pl = Player(pl_name, Card.card_list(pl_cards), 8, Card.card_list('crab_b1 crab_bl'))
    assert str(pl_name+': '+pl_cards+'; points:8; played:crab_b1 crab_bl') == str(pl)

def test_add_points():
    pl = Player('Joe', Card.card_list('crab_b1 mermaids_w fish_b1 crab_o'), 8, Card.card_list('crab_b1 crab_bl'))
    pl.add_points(8)
    assert pl.points == 16

def test_play_card():
    pl = Player('Joe', Card.card_list('crab_b1 mermaids_w fish_b1 crab_o'), 8, Card.card_list(''))
    card = pl.has_playable_cards()
    pl.play_card(Card.create(card[0][0]))
    pl.play_card(Card.create(card[0][1]))
    assert str(pl.hand) == 'mermaids_w fish_b1' and pl.played == Card.card_list('crab_b1 crab_o')

def test_enough_points():
    pl = Player('Joe', Card.card_list('crab_b1 mermaids_w fish_b1 crab_o'), 32, Card.card_list(''))
    assert not pl.enough_points()
    pl.add_points(8)
    assert pl.enough_points()
