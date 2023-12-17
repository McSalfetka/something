from PairEffects import PairsEff
from CardSSP import Card

def test_pair_effect():
    pair = ('crab_b1', 'crab_bl')
    E = PairsEff(pair)
    Reaction = E.pair_react()
    assert Reaction == 'Card_From_Heap'

    pair = ('fish_b1', 'fish_bl')
    E = PairsEff(pair)
    Reaction = E.pair_react()
    assert Reaction == 'Card_From_Library'

    pair = ('ship_b1', 'ship_bl')
    E = PairsEff(pair)
    Reaction = E.pair_react()
    assert Reaction == 'Addition_turn'

    pair = ('swimmer_b1', 'sharks_bl')
    E = PairsEff(pair)
    Reaction = E.pair_react()
    assert Reaction == 'Thief_the_Card'
