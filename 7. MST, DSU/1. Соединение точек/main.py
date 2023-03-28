# init funcs

def find(v):
    if v == prev[v]:
        return v
    prev[v] = find(prev[v])
    return prev[v]


def union(f, s):
    f, s = find(f), find(s)
    if f != s:
        if rank[f] < rank[s]:
            f, s = s, f
        prev[s] = f
        if rank[f] == rank[s]:
            rank[f] += 1


V = int(input())
coord = []
edges = []
for _ in range(V):
    coord.append(tuple(map(int, input().split())))
for i in range(len(coord) - 1):
    for j in range(1, len(coord)):
        edges.append(
            (i + 1, j + 1, sqrt((coord[i][0] - coord[j][0]) ** 2
                                + (coord[i][1] - coord[j][1]) ** 2))
        )
edges.sort(key=lambda x: x[2])
prev = list(range(V + 1))
rank = [0 for _ in range(V + 1)]
coord = []
cnt = 0
for edge in edges:
    if find(edge[0]) != find(edge[1]):
        cnt += edge[2]
        coord.append((edge[0], edge[1]))
        union(edge[0], edge[1])
print(cnt)
print(len(coord))
print(V - 1)
for elem in coord:
    print(*elem)
