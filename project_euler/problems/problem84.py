from project_euler.utils.timeit import timeit
from random import randint


class Monopoly:
    nb_squares = 40
    nb_faces = 4
    ch = [7, 22, 36]
    cc = [2, 17, 33]
    g2j, jail, go = 30, 10, 0
    C1, E3, H2, R1 = 11, 24, 39, 5
    nb_ch_or_cc_cards = 16

    def __init__(self, nb_rolls) -> None:
        self.current_square = 0
        self.nb_doubles = 0
        self.nb_rolls = nb_rolls
        self.nb_visit = [0] * self.nb_squares

    @staticmethod
    def _next_r(current_square) -> int:
        if current_square < 5:  # R1
            return 5
        elif current_square < 15:  # R2
            return 15
        elif current_square < 25:  # R3
            return 25
        elif current_square < 35:  # R4
            return 35
        else:
            return 5

    @staticmethod
    def _next_u(current_square) -> int:
        if current_square < 12:  # U1
            return 12
        elif current_square < 28:  # U2
            return 28
        else:
            return 12

    def _roll_dices(self) -> int:
        d1 = randint(1, self.nb_faces)
        d2 = randint(1, self.nb_faces)
        if d1 == d2:
            self.nb_doubles += 1
        else:
            self.nb_doubles = 0
        return d1 + d2

    def _get_next_square(self, dice_sum) -> int:
        if self.nb_doubles == 3:  # Go to JAIL if you roll 3 times a double
            return self.jail

        next_square = (self.current_square + dice_sum) % self.nb_squares
        if next_square in self.ch:
            # Draw one card from the chance card deck and evaluate what to do
            draw = randint(1, self.nb_ch_or_cc_cards)
            if draw == 1:  # Advance to GO
                next_square = self.go
            elif draw == 2:  # Go to Jail
                next_square = self.jail
            elif draw == 3:  # Go to C1
                next_square = self.C1
            elif draw == 4:  # Go to E3
                next_square = self.E3
            elif draw == 5:  # Go to H2
                next_square = self.H2
            elif draw == 6:  # Go to R1
                next_square = self.R1
            elif draw == 7:  # Go to next R
                next_square = self._next_r(next_square)
            elif draw == 8:  # Go to next R
                next_square = self._next_r(next_square)
            elif draw == 9:  # Go to next U
                next_square = self._next_u(next_square)
            elif draw == 10:  # Go back 3 square
                next_square = (next_square - 3) % self.nb_squares
        elif next_square in self.cc:
            # Draw one card from the community chest card deck
            draw = randint(1, self.nb_ch_or_cc_cards)
            if draw == 1:
                next_square = self.go
            elif draw == 2:
                next_square = self.jail
        elif next_square == self.g2j:
            next_square = self.jail

        return next_square

    def play(self):
        for _ in range(self.nb_rolls):
            dice_sum = self._roll_dices()
            self.current_square = self._get_next_square(dice_sum)
            self.nb_visit[self.current_square] += 1


@timeit
def problem84() -> int:
    """
    Monopoly odds
    Problem 84
    In the game, Monopoly, the standard board is set up in the following way: see https://projecteuler.net/problem=84
    A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they
    advance in a clockwise direction. Without any further rules we would expect to visit each square with equal
    probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this
    distribution.
    In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player
    rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to
    jail.
    At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card
    from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile.
    There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that
    order a movement; any instruction not concerned with movement will be ignored and the player will remain on the
    CC/CH square.
    Community Chest (2/16 cards):
        Advance to GO
        Go to JAIL
    Chance (10/16 cards):
        Advance to GO
        Go to JAIL
        Go to C1
        Go to E3
        Go to H2
        Go to R1
        Go to next R (railway company)
        Go to next R
        Go to next U (utility company)
        Go back 3 squares.
    The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of
    finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which
    the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a
    movement to another square, and it is the final square that the player finishes at on each roll that we are
    interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore
    the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.
    By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to
    produce strings that correspond with sets of squares.
    Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10,
    E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the
    six-digit modal string: 102400.
    If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
    The solution to this problem was to do a monte carlo simulation by doing 1 million rolls
    """
    nb_rolls = int(2e6)
    monopoly = Monopoly(nb_rolls)
    monopoly.play()

    probability_per_square = sorted(
        zip(range(monopoly.nb_squares), monopoly.nb_visit),
        key=lambda x: x[1],
        reverse=True,
    )
    # concat the 3 squares with the highest probability to visit
    return int("".join((str(square) for square, _ in probability_per_square[0:3])))


if __name__ == "__main__":
    problem84()
