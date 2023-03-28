import math


# build table
def build_table(arr, n):
    for i in range(0, n):
        dp[i][0] = arr[i]
    j = 1
    while (1 << j) <= n:
        i = 0
        while i + (1 << j) <= n:
            if dp[i][j - 1] < dp[i + (1 << (j - 1))][j - 1]:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i + (1 << (j - 1))][j - 1]
            i += 1
        j += 1


# query
def query(u, v, j):
    if dp[u][j] <= dp[v - (1 << j) + 1][j]:
        return dp[u][j]
    else:
        return dp[v - (1 << j) + 1][j]


# recieve input
# n – amount of elements
# m – amount of queries
# a – first el of an array
n, m, a = map(int, input().split())
u, v = map(lambda x: int(x) - 1, input().split())

# fill arr
arr = [a]
i = 0
while i < n - 1:
    a = (23 * a + 21563) % 16714589
    arr.append(a)
    i += 1

# fill sparse_table
b = bin(n)
n_ = len(b) - b.find('1')

dp = [[float('inf') for i in range(n_)] for j in range(n)]
build_table(arr, n)


def precalc_pows(n):
    pows = [0 for _ in range(n + 1)]
    for i in range(2, n + 1):
        pows[i] = pows[i - 1]
        if (1 << (pows[i] + 1)) <= i:
            pows[i] += 1

    return pows


pows = precalc_pows(n)

# construct queries
# get j
i = 1

while m + 1 > i:
    if u > v:
        l, r = v, u
    else:
        l, r = u, v
    j = pows[r - l + 1]
    r = query(l, r, j)
    if m == i:
        print(u + 1, v + 1, r)
        break

    u = ((17 * (u + 1) + 751 + r + 2 * i) % n)
    v = ((13 * (v + 1) + 593 + r + 5 * i) % n)

    i += 1
