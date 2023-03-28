p = 2
M = 10 ** 9 + 7

letters = 'abcdefghijklmnopqrstuvwxyz'
d = {char: ord(char) - 96 for char in letters}


def hash_string(string):
    hash = 0
    l = len(string)
    for i in range(l):
        val = d[string[i]] * p ** (l - (i + 1))
        hash += val
    return hash % M


s1 = "a" * (10 ** 3 + 3)
s2 = "ba" * 10 ** 3
hash_1 = hash_string(s1)
hash_2 = hash_string(s2)
print(hash_1)
print(hash_2)
