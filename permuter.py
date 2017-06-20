import math
from collections import defaultdict
from typing import DefaultDict
from typing import Set

from util import AppException


class Permutator:
    """
    class that finds possible permutations of a word

    """
    def __init__(self, word: str):
        self._word = word
        if word is None or len(word) < 1 :
            raise AppException("Word to permutate is None or 0-length")
        self._char_counts = find_repeats(self._word)

    def number_of_permutations(self) -> int:
        """
        calculate number of possible permutations by formula

        :return:  the number of possible permutations
        """
        perms = math.factorial(len(self._word))
        for v in self._char_counts.values():
            if v > 1:
                perms /= math.factorial(v)
        return perms

    @staticmethod
    def permutations(char_counts: DefaultDict[str, int])->Set[str]:
        total_char = sum(char_counts.values())
        variations = set()
        if len(char_counts) == 1:
            word_1 = ""
            for k, v in char_counts.items():
                for i in range(v):
                    word_1 += k
            variations.add(word_1)
            return variations
        elif total_char == 2:
            word_1 = "".join(char_counts.keys())
            word_2 = word_1[::-1]
            variations.add(word_1)
            variations.add(word_2)
            return variations
        else:
            for k, v in char_counts.items():
                copied_char_counts = char_counts.copy()
                if v == 1:
                    del copied_char_counts[k]
                else:
                    copied_char_counts[k] -= 1
                sub_variations = Permutator.permutations(copied_char_counts)
                for word in sub_variations:
                    variations.add(k + word)
            return variations

    def list_permutations(self):
        """
        returns a set of words which are permutations of the characters of the word

        :return: all permutations of the original word
        """
        return self.permutations(self._char_counts)


def find_repeats(word: str) -> DefaultDict[str, int]:
    """
    returns a dictionary of characters and number of their occurrances

    :param word: a string to count repeating characters
    :return: a dictionary of string, int
    """
    char_counts = defaultdict(int)
    if word is None or len(word) == 0:
        return char_counts
    for char in word:
        char_counts[char] += 1
    return char_counts



