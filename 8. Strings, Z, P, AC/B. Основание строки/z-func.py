# t = "abacaba"
# t = "a"
t = input()
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

# answer restoration
# print(z)
# print(lt)
for t in range(lt):
    if z[t] == lt - t:
        print(t)
        break
else:
    print(lt)
