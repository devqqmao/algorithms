n, k = map(int, input().split())

tree = [0] * (4 * n)
modif = [-1] * (4 * n)


def push(no, nl, nr):
    if modif[no] == -1:
        return

    tree[no] = modif[no] * (nr - nl)

    if nl != nr - 1:
        modif[2 * no + 1] = modif[2 * no + 2] = modif[no]
    modif[no] = -1


def assign(no, nl, nr, l, r, value):
    push(no, nl, nr)

    if nr <= l or r <= nl:
        return

    if l <= nl and nr <= r:
        modif[no] = value
        push(no, nl, nr)
        return

    mid = nl + (nr - nl) // 2

    assign(2 * no + 1, nl, mid, l, r, value)
    assign(2 * no + 2, mid, nr, l, r, value)

    tree[no] = tree[2 * no + 1] + tree[2 * no + 2]


def get(no, nl, nr, l, r):
    push(no, nl, nr)

    if l <= nl and nr <= r:
        return tree[no]

    if l >= nr or r <= nl:
        return 0

    mid = nl + (nr - nl) // 2
    return get(no * 2 + 1, nl, mid, l, r) + get(no * 2 + 2, mid, nr, l, r)


while k > 0:
    x = input().split()
    if x[0] == "A":
        l, r, value = list(map(int, x[1:]))
        assign(0, 0, n, l - 1, r, value)

    if x[0] == "Q":
        l, r = list(map(int, x[1:]))
        print(get(0, 0, n, l - 1, r))

    k -= 1
