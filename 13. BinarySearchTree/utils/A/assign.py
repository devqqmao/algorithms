n = int('inf')

modif = [] * (4 * n)
tree = object


def push(no, nl, nr):
    pass


# no – вершина, nl, nr – грани ответственности текущей вершины, l, r - исходный отрезок, val – значение
def assign(no: int, nl: int, nr: int, l: int, r: int, val: int):
    push(no, nl, nr)

    if l <= nl and nr <= r:
        modif[no] = val
        return

    if nr <= l or r <= nl:
        return

    mid = nl + (nr - nl) // 2
    assign(2 * no + 1, nl, mid, l, r, val)
    assign(2 * no + 2, mid, nr, l, r, val)

    tree[no] = -1
    for ch in [2 * no + 1, 2 * no + 2]:
        child_max = modif[ch] if (modif[ch] != -1) else tree[ch]
        tree[no] = max(tree[no], child_max)
