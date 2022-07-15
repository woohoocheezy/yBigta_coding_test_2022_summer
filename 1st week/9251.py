from sys import stdin

a = list(stdin.readline().strip())
b = list(stdin.readline().strip())

a, b = [' '] + a, [' '] +   b
m, n = len(a), len(b)

c = [[0 for _ in range(n)] for _ in range(m)]

for i in range(1, m):
    for j in range(1, n):
        if a[i] == b[j]:
            c[i][j] = c[i-1][j-1] + 1
        else:
            c[i][j] = max(c[i][j-1], c[i-1][j])

print(c[-1][-1])