# def funcs

def find(v):
    if v == parent[v]:
        return v
    parent[v] = find(parent[v])
    return parent[v]


def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1


# input
V = int(input())
coords = []
edges = []

parent = list(range(V + 1))
rank = [0 for _ in range(V + 1)]

dist = 0

for _ in range(V):
    coords.append(tuple(map(int, input().split())))
for i in range(len(coords) - 1):
    for j in range(1, len(coords)):
        edges.append(
            (i + 1, j + 1, ((coords[i][0] - coords[j][0]) ** 2
                            + (coords[i][1] - coords[j][1]) ** 2) ** 0.5)
        )

# sort
edges.sort(key=lambda x: x[2])

# solve
coords = []

for edge in edges:
    if find(edge[0]) != find(edge[1]):
        dist += edge[2]
        coords.append((edge[0], edge[1]))
        union(edge[0], edge[1])
print(dist)
print(V - 1)
for e in coords:
    print(*e)
