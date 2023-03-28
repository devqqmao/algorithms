n, m = list(map(int, input().split()))

edges = list()
head = [-1 for _ in range(n)]


class Edge:
    # хранит ребра
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


i = 0
while m > i:
    a, b, cap = list(map(int, input().split()))
    add_edge(a - 1, b - 1, cap)
    i += 1


def find_flow(v, max_cap):
    if used[v]:
        return 0

    if v == T:
        return max_cap
    used[v] = True

    i = head[v]  # adjacency multiList
    while i != -1:
        limit = min(edges[i].cap - edges[i].flow, max_cap)
        if limit and (result := find_flow(edges[i].to, limit)):
            edges[i].flow += result
            edges[i ^ 1].flow -= result
            return result
        i = edges[i].nxt


S = 0
T = n - 1
used = [False for _ in range(n)]
ans = 0
# из вершины S
while (delta := find_flow(S, int(1e9))):
    ans += delta
    used = [False for _ in range(n)]
# print(ans)

for i in range(len(edges)):
    print(i)
    print(edges[i].flow)
    print()
