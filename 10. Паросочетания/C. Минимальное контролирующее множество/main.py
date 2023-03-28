import sys
import collections

l, r = list(map(int, input().split()))


def handler(x):
    return int(x) - 1


d = collections.defaultdict(set)
[d[el[0]].add(el[1]) for el in [(list(map(handler, i.split()))) for i in sys.stdin.read().splitlines()]]


# find паросочетания

def dfs(v, used):
    if used[v]:
        return False
    used[v] = True
    for u in d[v]:
        if (match[u] == -1 or dfs(match[u], used)):
            match[u] = v
            return True
    return False


# match – хранение ориентации (с кем она соединена)
match = [-1] * r
ans = 0
for v in range(l):
    used = [False] * l
    if dfs(v, used):
        pass

# find VC

# init vars
u_ = set()  # unmatched vertices in l
d_ = collections.defaultdict(set)
complt = set()

# construct l and r graphs
for i in range(r):
    if match[i] != -1:
        u_.add(match[i])
        d[match[i]].discard(i)
        d_[i + l].add(match[i])

for k in d.keys():
    d[k] = {i + l for i in d[k]}

# combine l and r
d.update(d_)

# calculate vertices for dfs
u = set(range(l)) - u_


# perform dfs
def dfs1(v):
    complt.add(v)
    used[v] = 1
    for u in d[v]:
        if used[u] == -1:
            dfs1(u)


used = [-1] * (l + r)
for v in u:
    if used[v] == -1:
        dfs1(v)

# calculate l_minus and r_plus
l_minus = set(range(l)).difference(complt)
r_plus = set(range(l, r + l)).intersection(complt)

# answer
print(len(l_minus) + len(r_plus))
print(len(l_minus), len(r_plus))
[print(i + 1, end=' ') for i in l_minus]
print()
[print(i - l + 1, end=' ') for i in r_plus]
