from typing import List, Tuple, Iterable, Any

_NUMBER_DECODING = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def decode_hand(hand: List[str]) -> Iterable[Tuple[int, str]]:
    for number, color in hand:
        yield _NUMBER_DECODING[number], color


def make_number_occurrences(hand: List[Tuple[int, str]]) -> List[int]:
    occurrences = [0] * (14 + 1)
    for number, _ in hand:
        occurrences[number] += 1
    return occurrences


def is_straight(hand: List[Tuple[int, str]]) -> Tuple[bool, int]:
    first_number, _ = hand[0]
    for i, (number, _) in enumerate(hand[1:]):
        if number != (first_number + i + 1):
            return False, 0
    else:
        return True, first_number


def is_flush(hand: List[Tuple[int, str]]) -> Tuple[bool, int]:
    _, first_color = hand[0]
    for _, color in hand[1:]:
        if color != first_color:
            return False, 0
    else:
        return True, 0


def is_royal_flush(hand: List[Tuple[int, str]]) -> Tuple[bool, int]:
    is_straight_hand, straight_starting_value = is_straight(hand)
    if is_flush(hand) and is_straight_hand and straight_starting_value == 10:
        return True, 0
    else:
        return False, 0


def is_straight_flush(hand: List[Tuple[int, str]]) -> Tuple[bool, int]:
    is_straight_hand, straight_starting_value = is_straight(hand)
    if is_flush(hand) and is_straight_hand:
        return True, straight_starting_value
    else:
        return False, 0


def is_four_of_a_kind(hand: List[Tuple[int, str]]) -> Tuple[bool, int]:
    occurrences = make_number_occurrences(hand)
    for value, number in enumerate(occurrences):
        if number == 4:
            return True, value
    return False, 0


def is_three_of_a_kind(hand: List[Tuple[int, str]]) -> Tuple[bool, int]:
    occurrences = make_number_occurrences(hand)
    for value, number in enumerate(occurrences):
        if number == 3:
            return True, value
    return False, 0


def is_a_pair(hand: List[Tuple[int, str]]) -> Tuple[bool, int]:
    occurrences = make_number_occurrences(hand)
    for value, number in enumerate(occurrences):
        if number == 2:
            return True, value
    return False, 0


def is_a_two_pair(hand: List[Tuple[int, str]]) -> Tuple[bool, List[int]]:
    occurrences = make_number_occurrences(hand)
    pairs = []
    for value, number in enumerate(occurrences):
        if number == 2:
            pairs.append(value)

    if len(pairs) == 2:
        return True, pairs
    else:
        return False, []


def is_full_house(hand: List[Tuple[int, str]]) -> Tuple[bool, List[int]]:
    is_three, three_value = is_three_of_a_kind(hand)
    is_pair, pair_value = is_a_pair(hand)
    if is_pair and is_three:
        return True, [three_value, pair_value]
    else:
        return False, []


def highest_card_duel(hand1: List[Tuple[int, str]], hand2: List[Tuple[int, str]]) -> bool:
    """
    Determine the highest card between player 1 and player 2, in case both player have the same highest card,
    look at the second highest, etc. until we found which player has the highest card

    Returns:
        bool: True if the player 1 wins, False if the player 2 wins
    """
    game = list(zip(hand1, hand2))
    for h1, h2 in reversed(game):
        number1, _ = h1
        number2, _ = h2
        if number1 > number2:
            return True
        elif number2 > number1:
            return False


def get_hand_value(hand: List[Tuple[int, str]]) -> Tuple[int, Any]:
    """
    Determine a hand value giving its rank and rank value

    Parameters:
        hand (list): Card hand of the player

    Returns:
        rank (int): Rank of the card hand with the following definition
                    (0)  2       (1) 3       (2)  4       (3)  5
                    (4)  6       (5) 7       (6)  8       (7)  9
                    (8)  T       (9) J       (10) Q       (11) K
                    (12) A

        val  (int): Value of the rank (for example if a player as a Queen pair, it will return 10 for Queen
    """
    results = [
        is_royal_flush(hand),
        is_straight_flush(hand),
        is_four_of_a_kind(hand),
        is_full_house(hand),
        is_flush(hand),
        is_straight(hand),
        is_three_of_a_kind(hand),
        is_a_two_pair(hand),
        is_a_pair(hand),
    ]
    for rank, (is_current_rank, value) in enumerate(results):
        if is_current_rank:
            return rank, value
    else:
        return len(results), 0  # worst rank


def is_player1_winner(hand_player1: List[str], hand_player2: List[str]) -> bool:
    """
    Determine which hand between hand_1 and hand_2 wins the poker round

    Parameters:
        hand_player1 (list): Card hand of the player 1
        hand_player2 (list : Card hand of the player 2

    Returns:
        bool: True if the player 1 wins, False if the player 2 wins
    """
    hand_player1 = sorted(decode_hand(hand_player1))
    hand_player2 = sorted(decode_hand(hand_player2))
    rank1, value1 = get_hand_value(hand_player1)
    rank2, value2 = get_hand_value(hand_player2)
    if rank1 == rank2:
        if value1 == value2:
            return highest_card_duel(hand_player1, hand_player2)
        elif value1 > value2:
            return True
        else:
            return False
    elif rank1 < rank2:
        return True
    else:
        return False
