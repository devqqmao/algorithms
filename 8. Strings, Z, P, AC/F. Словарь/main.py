from collections import defaultdict


# build trie
# run through letters in a trie and printout terminal points

class Node:
    def __init__(self):
        self.term = False
        self.go = defaultdict()

    def add(self, s, i):
        cur = root
        for c in s:
            if c not in cur.go:
                cur.go[c] = Node()
            cur = cur.go[c]
        cur.term = i


def find_terminals():
    for i in range(len(t)):
        cur = root
        for j in range(i, len(t)):
            if t[j] in cur.go:
                cur = cur.go[t[j]]
                if cur.term:
                    ans[cur.term] = True
            else:
                break


root = Node()

ans = defaultdict()
t = input()
n = int(input())
i = 1

# build a trie

while i < n + 1:
    s = input()
    root.add(s, i)
    i += 1

find_terminals()

for i in range(n):
    if i + 1 in ans:
        print('Yes')
    else:
        print('No')
