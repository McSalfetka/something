import pytest

from PlayerSSP import Player
from CardSSP import Card
from HandSSP import Hand



def test_player():
    pl_name = 'Joe'
    pl_cards = 'crab_b1 mermaids_w fish_b1 crab_o'
    pl = Player(pl_name, Card.card_list(pl_cards))
    assert str(pl_name+': '+pl_cards) == str(pl)

#
