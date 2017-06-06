import permuter
import pytest

class TestPermuter:

    wordList = ["aat", "eat", "istanbul"]
    countList = [3, 6, 40320]

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def test_findRepeats(self):
        for w, c in zip(TestPermuter.wordList, TestPermuter.countList):
            p = permuter.Permutator(w)
            count = p.numberOfPerms()
            assert count == c, "numberOfPerms returns wrong number"


    def test_listPermutations(self):
        for w, c in zip(TestPermuter.wordList, TestPermuter.countList):
            p = permuter.Permutator(w)
            l = p.listPermutations()
            assert len(l) == c, "listPermutations returns wrong number of perms"
