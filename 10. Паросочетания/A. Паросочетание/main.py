import sys

l, r = list(map(int, input().split()))


def handler(x):
    return int(x) - 1


adjl = list(map(lambda x: list(map(handler, x.split()))[:-1], sys.stdin.read().splitlines()))


# Алгоритм Куна

def dfs(v, used):
    if used[v]:
        return False
    used[v] = True
    for u in adjl[v]:
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
        ans += 1

print(ans)
for i in range(r):
    if match[i] != -1:
        print(match[i] + 1, i + 1)
