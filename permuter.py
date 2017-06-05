import math


def findRepeats(word):
    d = {}
    d.update(zip(word,[0]*len(word)))
    #print(d)
    for a in word:
        d[a] += 1
    print(d)
    return d


def numberOfPerms(word):
    l = len(word)
    perms = math.factorial(l)
    d = findRepeats(word)
    for _, v in d.items():
        perms /= math.factorial(v)
    return perms, d


def allPerms(d):
    s = sum(d.values())
    print(s, d)
    ls = set()
    if len(d) == 1:
        p1 = ""
        for k, v in d.items():
            for i in range(v):
                p1 += k
        ls.add(p1)
        return ls
    elif s == 2:
        p1, p2 = "",  ""
        for k in d.keys():
            p1 = p1 + k
            p2 = k + p2
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
            l = allPerms(sd)
            for w in l:
                ls.add(k + w)
                ls.add(w + k)
        return ls
    print("unexpected condition")



if __name__ == "__main__":
    word = "aeatae"
    n, d = numberOfPerms(word)
    print("Possible permutaions " +str(n))
    list = allPerms(d)
    print("Perms expected vs actual: ", n," / ", len(list))
    print("Perms: ", list)


