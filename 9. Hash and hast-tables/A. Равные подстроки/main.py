p = 2
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

    s1 = ss_hash(l1, r1)
    s2 = ss_hash(l2, r2)

    if s1 == s2:
        print('+', end='')
    else:
        print('-', end='')
    i -= 1
