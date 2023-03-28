# init funcs

def find(v):
    if v == prev[v]:
        return v
    prev[v] = find(prev[v])
    return prev[v]


def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        if rank[a] < rank[b]:
            a, b = b, a
        prev[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1


# input
V, E = map(int, input().split())

edges = []
for _ in range(E):
    b, e, w = map(int, input().split())
    edges.append((b, e, w))
edges.sort(key=lambda x: x[2])

prev = list(range(V + 1))
rank = [0 for _ in range(V + 1)]
dist = 0

for edge in edges:
    if find(edge[0]) != find(edge[1]):
        dist += edge[2]
        union(edge[0], edge[1])
print(dist)
