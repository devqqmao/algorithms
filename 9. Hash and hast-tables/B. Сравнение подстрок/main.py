from math import log2

p = 37
M = 10 ** 9 + 7

s = input()
i = int(input())
hashes = list()

letters = 'abcdefghijklmnopqrstuvwxyz'
d = {char: ord(char) - 96 for char in letters}

pows = [0] * (len(s) + 1)
pows[0] = 1
pows[1] = p


def hash(string):
    for _ in range(1, len(string)):
        pows[_ + 1] = p * pows[_] % M
        hashes.append((hashes[-1] * p + d[s[_]]) % M)


def ss_hash(l, r):
    return (hashes[r] - hashes[l - 1] * pows[r - (l - 1)]) % M


hashes.append(0)
hashes.append(d[s[0]])
hash(s)

while i > 0:
    l1, r1, l2, r2 = map(int, input().split())
    d2 = r2 - l2
    d1 = r1 - l1
    dist = min(d1, d2)  # amount of letters
    if d2 > d1:
        d = d1
        d_size = "<"
    elif d2 < d1:
        d = d2
        d_size = ">"
    else:
        d = d1
        d_size = "="


    def case_full(l1, l2, d, d_size):
        if ss_hash(l1, l1 + d) == ss_hash(l2, l2 + d):
            if d_size == "<":
                return "<"
            elif d_size == ">":
                return ">"
            else:
                return "="


    def case_0(l1, l2):
        if s[l1 - 1] > s[l2 - 1]:
            return ">"
        elif s[l1 - 1] < s[l2 - 1]:
            return "<"
        else:
            return "="


    # case full
    res = case_full(l1, l2, d, d_size)
    if res:
        print(res)
        i -= 1
        continue

    # case 0
    zero_equal = False
    res = case_0(l1, l2)
    if res == "=":
        zero_equal = True
    else:
        print(res)
        i -= 1
        continue

    l_ = 0
    r_ = dist + 1
    while r_ - l_ > 1:
        mid = (r_ + l_) // 2
        if ss_hash(l1, l1 + mid) == ss_hash(l2, l2 + mid):
            l_ = mid
        else:
            r_ = mid
    if r_ == 0:
        print("impossible")
    elif r_ == 1:
        if zero_equal:  # if zero are equal
            res = case_0(l1 + 1, l2 + 1)  # case_1
            if res == "=":
                print(res)
                i -= 1
                continue
            else:  # compare ones without size
                print(res)
                i -= 1
                continue
        else:  # compare without size
            print(res)
            i -= 1
            continue
    else:
        res = case_0(l1 + r_, l2 + r_)
        print(res)
        i -= 1
        continue

    i -= 1
