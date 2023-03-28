# input
a = input()
b = input()

# 1st
t = a + "\xF2" + b

# 1st
lt = len(t)
la = len(a)
z = [0] * lt
L, R = 0, 0

for i in range(1, lt):
    k = 0
    if i <= R:
        k = min(z[i - L], R - i + 1)
    while i + k != lt and t[k] == t[i + k]:
        k += 1
    z[i] = k
    if i + z[i] - 1 > R:
        L = i
        R = i + z[i] - 1

# 2nd
a_ = a[::-1]
b_ = b[::-1]
t_ = a_ + "\xF2" + b_

z_ = [0] * lt
L, R = 0, 0

for i in range(1, lt):
    k = 0
    if i <= R:
        k = min(z_[i - L], R - i + 1)
    while i + k != lt and t_[k] == t_[i + k]:
        k += 1
    z_[i] = k
    if i + z_[i] - 1 > R:
        L = i
        R = i + z_[i] - 1

# answer restoration

z = z[la + 1:]
z_ = z_[la + 1:]

l = len(b)
indices = []
cnt = 0
for i in range(len(z) - la + 1):

    if z[i] + z_[l - i - la] >= la - 1:
        indices.append(i + 1)
        cnt += 1

print(cnt)
print(*indices)
