b = input()
a = input()

t = a + b

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

# answer restoration
z = z[la:]

indices = []
counter = 0
for i in range(len(z)):
    if z[i] >= la:
        indices.append(i + 1)
        counter += 1

print(counter)
print(*indices)
