from ScoreCountingSSP import Scoring
from CardSSP import Card

def test_Score_count():
    text = 'crab_b1 mermaids_w fish_b1 crab_o'
    scores = Scoring(Card.card_list(text))
    counted = scores.Score_count()
    assert counted == 2

    text = 'penguins_lgr penguins_lg PenguinColony_lgr shells_b1'
    scores = Scoring(Card.card_list(text))
    counted = scores.Score_count()
    assert counted == 7

    text = 'penguins_lgr mermaids_w penguins_lg PenguinColony_lgr shells_b1 mermaids_w'
    scores = Scoring(Card.card_list(text))
    counted = scores.Score_count()
    assert counted == 11

