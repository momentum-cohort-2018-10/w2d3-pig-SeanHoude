from pig import Game, Player, Die


def test_play_turn_picks_computer():
    turn_order = 0
    assert play_turn() == 'computer'

def test_play_turn_picks_human():
    turn_order = 1
    assert game.play_turn() == 'human'

def test_random_returns_num():
    game = Game()
    player = Player(0, 0)
    computer = Player(0, 0, True)
    assert game.get_player() in [player, computer]