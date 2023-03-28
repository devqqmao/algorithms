# x = "abacaba"
x = "abacaba"
p = [0] * len(x)

for i in range(1, len(x)):
    j = p[i - 1]
    while j > 0 and x[j] != x[i]:
        j = p[j - 1]
    if x[j] == x[i]:
        j += 1
    p[i] = j

print(p)
