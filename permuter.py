import math


class Permutator:
    """
    class that finds possible permutations of a word

    """

    def __init__(self, iterable):
        self._iterable = iterable
        self._len = len(self._iterable)
        self._d = self.findRepeats(self._iterable)

    @staticmethod
    def findRepeats(iterable):
        d = {}
        d.update(zip(iterable, [0]*len(iterable)))
        for a in iterable:
            d[a] += 1
        return d


    def numberOfPerms(self):
        perms = math.factorial(self._len)
        for v in self._d.values():
            perms /= math.factorial(v)
        return perms

    @staticmethod
    def permutations(d):
        s = sum(d.values())
        ls = set()
        if len(d) == 1:
            p1 = ""
            for k, v in d.items():
                for i in range(v):
                    p1 += k
            ls.add(p1)
            return ls
        elif s == 2:
            p1 = "".join(d.keys())
            p2 = p1[::-1]
            ls.add(p1)
            ls.add(p2)
            return ls
        else:
            for k, v in d.items():
                sd = d.copy()
                if v == 1:
                    del sd[k]
                else:
                    sd[k] -= 1
                l = Permutator.permutations(sd)
                for w in l:
                    ls.add(k + w)
            return ls

    def listPermutations(self):
        return self.permutations(self._d)



