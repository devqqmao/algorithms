n = int('inf')

modif = [] * (4 * n)
tree = object


# no – вершина, nl, nr – грани отрезка
def push(no: int, nl: int, nr: int):
    # если ничего не записано, то ничего не присваиваем (не пушим)
    if modif[no] == -1:
        return

    # в ноду записываем модификатор
    tree[no] = modif[no]

    # если не листовая вершина, то используем его на листьях
    if (nl != nr - 1):
        modif[2 * no + 1] = modif[2 * no + 2] = modif[no]

    # снимаем модификатор
    modif[no] = -1
