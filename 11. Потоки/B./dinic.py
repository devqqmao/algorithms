# from collections import deque


class Edge:
    def __init__(self, to, flow, cap, nxt):
        self.to = to
        self.flow = flow
        self.cap = cap
        self.nxt = nxt


def add_edge(a, b, cap):
    edges.append(Edge(b, 0, cap, head[a]))
    head[a] = len(edges) - 1

    edges.append(Edge(a, 0, 0, head[b]))
    head[b] = len(edges) - 1


def bfs():
    global level
    level = [-1] * n
    level[S] = 0

    # q = deque()
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
    # return False if level[T] < 0 else True


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
    add_edge(a - 1, b - 1, cap)
    i += 1

ans = 0
while bfs():
    headcopy = list(head)
    while (delta := find_flow(S, int(1e9), headcopy)):
        ans += delta

print(ans)
for i in range(0, len(edges), 2):
    print(edges[i].flow)
