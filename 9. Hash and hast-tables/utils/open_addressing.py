keys = [1, 2, 3]
values = [1, 2, 3]
i = k = 0



def Hash(key):
    pass


def put(k, v):
    i = Hash(k)

    while keys[i] != None:
        if keys[i] == k:
            values[i] = v
            return
        else:
            i += 1

    keys[i] = k
    values[i] = v

# put / find
# идем до первой свободной ячейки, или пока не найдем ключ

def find(k):
    i = Hash(k)

    while keys[i] != None:
        if  keys[i] == k:
            return keys[i]
        else:
            i += 1

# and value not deleted then break

def delete(k):
    pass


# не просто
keys[i] = None
values[i] = None

keys[i] = k
values[i] = 'deleted'

# open addressing (прыжки на квадрат)
# 2 функции хэширование: в какую ячейку, куда делать прыжки
