from pathlib import Path
from project_euler.utils.timeit import timeit


def get_square_candidates(nb_digits):
    def get_squared(max_n):
        nb_digits_max = len(str(max_n))
        categories = [[] for _ in range(nb_digits_max)]
        n = 1
        while 1:
            n2 = n * n
            if n2 > max_n:
                break
            nb_digits = len(str(n2))
            categories[nb_digits - 1].append(str(n2))
            n += 1
        return categories

    def digit_validate(n, nb_digits):
        n_str = str(n)
        if len(n_str) != nb_digits:
            return False
        mem = [0] * 10
        for c in n_str:
            if mem[int(c)] == 1:
                return False
            else:
                mem[int(c)] += 1
        return True

    squared_candidates = []
    categories = get_squared(10**nb_digits)
    for category in categories:
        for n in category:
            if digit_validate(n, nb_digits):
                squared_candidates.append(n)
    return squared_candidates


def get_anagram_candidates(words):
    def is_anagram(word_a, word_b):
        match = [False] * len(word_b)
        if len(word_a) != len(word_b):
            return False
        if word_a == word_b:  # palindromes are not anagrams
            return False
        for letter_a in word_a:
            # try to find the letter a of word a in word b
            for index, letter_b in enumerate(word_b):
                if letter_b == letter_a and not match[index]:
                    match[index] = True
                    break
            else:
                return False
        return True

    anagrams_candidates = []
    visited = [False] * len(words)
    for index_a, word_a in enumerate(words):
        visited[index_a] = True
        anagrams = [word_a]
        # Out of this loop, we have the anagrams for "word_a"
        for index_b, word_b in enumerate(words):
            if word_a != word_b and not visited[index_b]:
                if is_anagram(word_a, word_b):
                    visited[index_b] = True
                    anagrams.append(word_b)
        if len(anagrams) > 1:
            anagrams_candidates.append(anagrams.copy())
    return anagrams_candidates


def anagram_squared_validate(anagrams, square_a):
    def get_letter_index(anagram, letter):
        for index, char in enumerate(anagram):
            if char == letter:
                return index
        else:
            return -1

    square_b = [0] * len(square_a)
    for index, char in enumerate(anagrams[1]):
        square_b[index] = square_a[get_letter_index(anagrams[0], char)]
    return str("".join(square_b))


@timeit
def problem98() -> int:
    """
    Anagramic squares
    Problem 98

    By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number:
    1296 = 36^2. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a
    square number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair and specify further that leading
    zeroes are not permitted, neither may a different letter have the same digital value as another letter.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
    English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of
    itself).

    What is the largest square number formed by any member of such a pair?

    NOTE: All anagrams formed must be contained in the given text file.
    """
    with open(Path(__file__).parent / "data/problem98.txt") as f:
        words = f.read().split(",")
    max_len = 14
    word_per_nb_letters = [[] for _ in range(max_len)]
    # Store each word by the number of letters because anagrams will be of same length
    for word in words:
        word_without_quotes = word[1 : len(word) - 1]
        nb_letters = len(word_without_quotes)
        word_per_nb_letters[nb_letters - 1].append(word_without_quotes)
    # For each list of words, find those that are anagrams
    largest_square = 0
    for word_list in word_per_nb_letters:
        nb_words = len(word_list)
        if nb_words > 0:
            nb_letters = len(word_list[0])
            anagram_candidates = get_anagram_candidates(word_list)
            if len(anagram_candidates) > 0:
                square_candidates = get_square_candidates(nb_letters)
                for anagrams in anagram_candidates:
                    for candidate_a in square_candidates:
                        candidate_b = anagram_squared_validate(anagrams, candidate_a)
                        if candidate_b in square_candidates:
                            if int(candidate_b) > largest_square:
                                largest_square = int(candidate_b)
    return largest_square


if __name__ == "__main__":
    problem98()
