t = input()
t *= 2
lt = len(t)
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

cnt = 1
for i in range(1, lt // 2):
    if t[z[i]] > t[(i + z[i]) % lt]:
        cnt += 1

print(cnt)
