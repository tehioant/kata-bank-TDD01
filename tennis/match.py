from typing import Tuple, Union


class TennisMatch:
    def __init__(self):
        self.player_game_scores = {"player1": "love", "player2": "love"}
        self.player_set_scores = {"player1": 0, "player2": 0}

    def player_add_point(self, player_name: str) -> None:
        if player_name not in self.player_game_scores.keys():
            raise ValueError(f"Player name given {player_name} do not exist")
        player_score = self.player_game_scores[player_name]
        if player_score == "love":
            self.player_game_scores[player_name] = "15"
        elif player_score == "15":
            self.player_game_scores[player_name] = "30"
        elif player_score == "30":
            self.player_game_scores[player_name] = "40"
        elif player_score == "40":
            self.update_player_score_when_score_is_40(player_name)
        elif player_score == "advantage":
            self.player_add_game(player_name)

    def player_add_game(self, player_name):
        self.player_game_scores = {"player1": "love", "player2": "love"}
        self.player_set_scores[player_name] += 1

    def update_player_score_when_score_is_40(self, player_name):
        opponent_player_name = [name for name in self.player_game_scores.keys() if name != player_name][0]
        opponent_score = self.player_game_scores[opponent_player_name]
        if opponent_score == "advantage":
            self.player_game_scores[opponent_player_name] = "40"
        elif opponent_score == "40":
            self.player_game_scores[player_name] = "advantage"
        else:
            self.player_add_game(player_name)

    def get_score_game(self) -> Union[Tuple, str]:
        score_player_1, score_player_2 = self.player_game_scores["player1"], self.player_game_scores["player2"]
        if (score_player_1 == "40") and (score_player_2 == "40"):
            return "deuce"
        elif score_player_1 == "advantage":
            return "advantage player1"
        elif score_player_2 == "advantage":
            return "advantage player2"
        else:
            return score_player_1, score_player_2

    def get_score_set(self) -> Union[Tuple, str]:
        game_difference = abs(self.player_set_scores["player1"] - self.player_set_scores["player2"])
        if (self.player_set_scores["player1"] == 6) and (game_difference >= 2):
            return "player1 wins the match"
        if (self.player_set_scores["player2"] == 6) and (game_difference >= 2):
            return "player2 wins the match"
        else:
            return self.player_set_scores["player1"], self.player_set_scores["player2"]

