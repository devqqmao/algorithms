import sys, threading


def main():
    class Edge:
        def __init__(self, ind, to, flow, cap, nxt):
            self.ind = ind
            self.to = to
            self.flow = flow
            self.cap = cap
            self.nxt = nxt

    def add_edge(ind, a, b, cap):
        edges.append(Edge(ind, b, 0, cap, head[a]))
        head[a] = len(edges) - 1
        edges.append(Edge(ind, a, 0, 0, head[b]))
        head[b] = len(edges) - 1

    path = []

    def find_flow(v, max_cap):
        if used[v]:
            return 0
        if v == t:
            return max_cap
        used[v] = True
        i = head[v]
        while i != -1:
            limit = min(edges[i].cap - edges[i].flow, max_cap)
            if limit and (result := find_flow(edges[i].to, limit)):
                edges[i].flow += result
                edges[i ^ 1].flow -= result
                path[count].append(edges[i].ind)
                return result
            i = edges[i].nxt
        return 0

    n, m, s, t = map(int, input().split())
    s -= 1
    t -= 1

    edges = []
    head = [-1] * n
    for i in range(m):
        a, b = map(int, input().split())
        add_edge(i, a - 1, b - 1, 1)

    ans = 0
    count = 0
    path = [[], []]
    while count < 2:
        used = [False] * n
        delta = find_flow(s, int(1e9))
        count += 1
        if not delta:
            break
        ans += delta

    if len(path[0]) > 0 and len(path[1]) > 0:
        print("YES")

        # path 1
        print(s + 1, end=' ')
        for p in reversed(path[0]):
            print(edges[p * 2].to + 1, end=' ')
        print()
        # path 2
        print(s + 1, end=' ')
        for p in reversed(path[1]):
            print(edges[p * 2].to + 1, end=' ')
    else:
        print("NO")


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    threading.stack_size(10000000)
    thread = threading.Thread(target=main)
    thread.start()

# import math
#
# print(math.log2(10000000))
