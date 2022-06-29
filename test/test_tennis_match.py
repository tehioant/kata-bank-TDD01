import pytest

from tennis.match import TennisMatch


def test_init_tennis_match():
    # When
    tennis_match = TennisMatch()
    # Then
    assert tennis_match.get_score_set() == (0, 0)
    assert tennis_match.get_score_game() == ("love", "love")


def test_init_tennis_match_and_player1_wins_the_first_point():
    # Given
    tennis_match = TennisMatch()
    # When
    tennis_match.player_add_point(player_name="player1")
    # Then
    assert tennis_match.get_score_set() == (0, 0)
    assert tennis_match.get_score_game() == ("15", "love")


def test_init_tennis_match_and_player2_wins_the_first_point():
    # Given
    tennis_match = TennisMatch()
    # When
    tennis_match.player_add_point(player_name="player2")
    # Then
    assert tennis_match.get_score_set() == (0, 0)
    assert tennis_match.get_score_game() == ("love", "15")


def test_init_match_and_player1_wins_2_points_versus_1_for_player2():
    # Given
    tennis_match = TennisMatch()
    # When
    tennis_match.player_add_point(player_name="player1")
    tennis_match.player_add_point(player_name="player2")
    tennis_match.player_add_point(player_name="player1")
    # Then
    assert tennis_match.get_score_set() == (0, 0)
    assert tennis_match.get_score_game() == ("30", "15")


def test_init_match_and_player1_wins_1_point_versus_3_for_player2():
    # Given
    tennis_match = TennisMatch()
    # When
    tennis_match.player_add_point(player_name="player1")
    tennis_match.player_add_point(player_name="player2")
    tennis_match.player_add_point(player_name="player2")
    tennis_match.player_add_point(player_name="player2")
    # Then
    assert tennis_match.get_score_set() == (0, 0)
    assert tennis_match.get_score_game() == ("15", "40")


# test init tennis mach and player 1 wins 4 points vs 0 for player 2
def test_init_tennis_match_and_player1_wins_four_points_versus_zero():
    # Given
    tennis_match = TennisMatch()
    # When
    for _ in range(4):
        tennis_match.player_add_point(player_name="player1")
    # Then
    assert tennis_match.get_score_set() == (1, 0)
    assert tennis_match.get_score_game() == ("love", "love")


def test_if_player_name_do_not_exist_then_throw_an_exception():
    # Given
    tennis_match = TennisMatch()
    player_name = "Nadal"
    # When-Then
    with pytest.raises(ValueError) as error:
        tennis_match.player_add_point(player_name=player_name)
    assert error.value.args[0] == f"Player name given {player_name} do not exist"


def test_deuce_when_game_score_is_40_40():
    # Given
    tennis_match = TennisMatch()
    # When
    for _ in range(3):
        tennis_match.player_add_point(player_name="player1")
        tennis_match.player_add_point(player_name="player2")
    # Then
    assert tennis_match.get_score_set() == (0, 0)
    assert tennis_match.get_score_game() == "deuce"


def test_advantage_when_game_score_is_deuce_and_player1_add_point():
    # Given
    tennis_match = TennisMatch()
    # When
    for _ in range(3):
        tennis_match.player_add_point(player_name="player1")
        tennis_match.player_add_point(player_name="player2")
    tennis_match.player_add_point(player_name="player1")
    # Then
    assert tennis_match.get_score_set() == (0, 0)
    assert tennis_match.get_score_game() == "advantage player1"


def test_given_score_3_to_2_with_advantage_player1_when_player1_wins_the_point():
    # Given
    tennis_match = TennisMatch()
    tennis_match.player_set_scores = {"player1": 3, "player2": 2}
    tennis_match.player_game_scores = {"player1": "advantage", "player2": "40"}
    # When
    tennis_match.player_add_point(player_name="player1")
    # Then
    assert tennis_match.get_score_set() == (4, 2)
    assert tennis_match.get_score_game() == ("love", "love")


def test_when_player1_has_advantage_and_player2_wins_the_point_it_should_return_deuce():
    # Given
    tennis_match = TennisMatch()
    tennis_match.player_game_scores = {"player1": "advantage", "player2": "40"}
    # When
    tennis_match.player_add_point(player_name="player2")
    # Then
    assert tennis_match.get_score_set() == (0, 0)
    assert tennis_match.get_score_game() == "deuce"


def test_when_player1_wins_the_match_point():
    # Given
    tennis_match = TennisMatch()
    tennis_match.player_set_scores = {"player1": 5, "player2": 2}
    tennis_match.player_game_scores = {"player1": "40", "player2": "15"}
    # When
    tennis_match.player_add_point(player_name="player1")
    # Then
    assert tennis_match.get_score_set() == "player1 wins the match"


def test_when_score_set_is_5_5_and_player1_wins_the_game():
    # Given
    tennis_match = TennisMatch()
    tennis_match.player_set_scores = {"player1": 5, "player2": 5}
    tennis_match.player_game_scores = {"player1": "40", "player2": "15"}
    # When
    tennis_match.player_add_point(player_name="player1")
    # Then
    assert tennis_match.get_score_set() == (6, 5)
    assert tennis_match.get_score_game() == ("love", "love")
