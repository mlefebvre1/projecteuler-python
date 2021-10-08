from pathlib import Path
from ..utils import poker
from ..utils.timeit import timeit


@timeit
def problem54():
    with open(f"{Path(__file__).parent}/data/problem54.txt", "r") as fp:
        games = fp.read().splitlines()
        fp.close()

    nb_win_player1 = 0
    for game in games:
        game = game.split(" ")
        hand_player1, hand_player2 = game[0:5], game[5:]
        if poker.is_player1_winner(hand_player1, hand_player2):
            nb_win_player1 += 1
    return nb_win_player1


if __name__ == "__main__":
    problem54()
