from sys import stdin

n = stdin.readline()
weights = list(map(int, stdin.readline().split()))
weights.sort()
estimate_w = 1
print(weights)

for w in weights :
    if estimate_w < w :
        break

    estimate_w += w

print(estimate_w)
