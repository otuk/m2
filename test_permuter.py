import permuter
from util import AppException


class TestPermuter:

    SAMPLE_WORDS = ["aat", "eat", "istanbul", "stress", "x", "", None]
    SAMPLE_PERM_COUNTS = [3, 6, 40320, 120, 1, 0, 0]
    SAMPLE_MAX_REPEAT_COUNTS = [2, 1, 1, 3, 1, 0, 0]

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def test_find_repeats(self):
        for word, max_repeat in zip(TestPermuter.SAMPLE_WORDS, TestPermuter.SAMPLE_MAX_REPEAT_COUNTS):
            d = permuter.find_repeats(word)
            if len(d) > 0:
                m = max(d.values())
                assert m == max_repeat, "find repeats not working"
            else:
                assert word is None or max_repeat == len(word), "0 length string shd have 0 repeats "

    def test_number_of_permutations(self):
        for word, count in zip(TestPermuter.SAMPLE_WORDS, TestPermuter.SAMPLE_PERM_COUNTS):
            try:
                p = permuter.Permutator(word)
            except AppException:
                assert word is None or len(word) == 0, "Exception raised for a non 0-length word"
                continue
            c = p.number_of_permutations()
            assert count == c, "numberOfPerms returns wrong number"

    def test_list_permutations(self):
        for word, count in zip(TestPermuter.SAMPLE_WORDS, TestPermuter.SAMPLE_PERM_COUNTS):
            try:
                p = permuter.Permutator(word)
            except AppException:
                assert word is None or len(word) == 0, "Exception raised for a non 0-length word"
                continue
            l = p.list_permutations()
            assert len(l) == count, "list_permutations returns wrong number of perms"
