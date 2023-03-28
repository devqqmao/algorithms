# input
n, m = list(map(int, input().split()))
t = input().split()
n = n * 2 + 1
t.append('\xF0')
t.extend(t[len(t) - 2::-1])

z = [0] * n
L, R = 0, 0

for i in range(1, n):
    k = 0
    if i <= R:
        k = min(z[i - L], R - i + 1)
    while i + k != n and t[k] == t[i + k]:
        k += 1
    z[i] = k
    if i + z[i] - 1 > R:
        L = i
        R = i + z[i] - 1

z = z[::-1]
n = n // 2
ans = []
print(z)

print(n, end=' ')

for i in range(1, n):
    if z[i] == i + 1 and z[i] % 2 == 0:
        ans.append(n - (i + 1) // 2)

print(*ans)
