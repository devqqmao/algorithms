import sys
import collections

n, m = list(map(int, input().split()))


def handler(x):
    return int(x) - 1


d = collections.defaultdict(set)
[d[el[0]].add(el[1]) for el in [(list(map(handler, i.split()))) for i in sys.stdin.read().splitlines()]]


# Алгоритм Куна

def dfs(v, used):
    if used[v]:
        return False
    used[v] = True
    for u in d[v]:
        if match[u] == -1:
            match[u] = v
            return True
        if dfs(match[u], used):
            match[u] = v
            return True
    return False


match = [-1] * n
ans = 0

for v in d.keys():
    used = [False] * n
    if dfs(v, used):
        pass

u = set()
for i in range(n):
    if match[i] != -1:
        u.add(match[i])
print(n - len(u))
