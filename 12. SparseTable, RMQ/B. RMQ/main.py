import sys


def build_tree(node, node_l, node_r):
    if node_l == node_r:
        tree[node] = leaves[node_r]

    else:
        mid = (node_l + node_r) // 2

        build_tree(2 * node + 1, node_l, mid)
        build_tree(2 * node + 2, mid + 1, node_r)

        tree[node] = min(tree[2 * node + 1],
                         tree[2 * node + 2])


def set(node, node_l, node_r, i, new_value):
    if node_l == node_r:
        assert node_l == i
        tree[node] = new_value

    else:
        mid = (node_l + node_r) // 2
        if i <= mid:
            set(2 * node + 1, node_l, mid, i, new_value)
        else:
            set(2 * node + 2, mid + 1, node_r, i, new_value)
        tree[node] = min(tree[2 * node + 1],
                         tree[2 * node + 2])


def get(node, node_l, node_r, l, r):
    if l <= node_l and node_r <= r:
        return tree[node]

    if l > node_r or r < node_l:
        return float('inf')

    mid = (node_l + node_r) // 2

    return min(get(2 * node + 1, node_l, mid, l, r),
               get(2 * node + 2, mid + 1, node_r, l, r))


n = int(input())
leaves = list(map(int, input().split()))

tree = [-1 for _ in range(4 * n)]
build_tree(0, 0, n - 1)

for line in sys.stdin:
    operation, l, r = line.split()
    l, r = int(l), int(r)
    if operation == "set":
        set(0, 0, n - 1, l - 1, r)
    elif operation == "min":
        print(get(0, 0, n - 1, l - 1, r - 1))
    else:
        raise Exception
