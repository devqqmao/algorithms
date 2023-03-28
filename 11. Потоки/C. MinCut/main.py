# from collections import deque


class Edge:
    def __init__(self, to, flow, cap, nxt, i):
        self.to = to
        self.flow = flow
        self.cap = cap
        self.nxt = nxt
        self.ord = i


def add_edge(a, b, cap, i):
    edges.append(Edge(b, 0, cap, head[a], i))
    head[a] = len(edges) - 1

    edges.append(Edge(a, 0, cap, head[b], i))
    head[b] = len(edges) - 1


def bfs():
    global level
    level = [-1] * n
    level[S] = 0

    q = []
    q.append(S)
    while q:
        u = q.pop(0)
        i = head[u]
        while i != -1:
            v = edges[i].to
            if edges[i].cap > edges[i].flow and level[v] == -1:
                level[v] = level[u] + 1
                q.append(v)
            i = edges[i].nxt
    return level[T] != -1


def find_flow(v, max_cap, head):
    if v == T:
        return max_cap

    while True:
        e = head[v]
        if e == -1:
            return 0

        limit = min(edges[e].cap - edges[e].flow, max_cap)

        if limit and level[edges[e].to] == level[v] + 1 \
                and (result := find_flow(edges[e].to, limit, head)):
            edges[e].flow += result
            edges[e ^ 1].flow -= result
            return result
        else:
            head[v] = edges[e].nxt


n, m = list(map(int, input().split()))

edges = []
head = [-1] * n
S = 0
T = n - 1

i = 0
while m > i:
    a, b, cap = list(map(int, input().split()))
    add_edge(a - 1, b - 1, cap, i)
    i += 1

ans = 0
while bfs():
    headcopy = list(head)
    while (delta := find_flow(S, int(1e9), headcopy)):
        ans += delta

used = [-1] * n


def dfs2(v):
    if used[v] == -1:
        used[v] = 1
        i = head[v]
        while i != -1:
            if edges[i].cap != edges[i].flow:
                dfs2(edges[i].to)
            i = edges[i].nxt


dfs2(S)
# add edges
edges_ = []
for i in range(0, 2 * m, 2):
    if (used[edges[i].to] == 1 and used[edges[i ^ 1].to] == -1) or (
            used[edges[i].to] == -1 and used[edges[i ^ 1].to] == 1):
        edges_.append(edges[i].ord + 1)

print(len(edges_), ans)
[print(e, end=' ') for e in edges_]
