Lists = [1, 2, 3]


def Hash(key):
    pass


def find(key):
    i = Hash(key)

    for (k, v) in Lists[i]:
        if k == key:
            return v

        raise "Not Found"


def put(key, new_value):
    i = Hash(key)

    for (j, (k, v)) in enumerate(Lists[i]):
        if k == key:
            Lists[i] = (k, new_value) # put
            return

    Lists[i].append((key, new_value))
