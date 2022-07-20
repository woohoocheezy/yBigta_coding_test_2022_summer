from sys import stdin

S = stdin.readline().rstrip()

outputs = []

for i in range(len(S)):
    outputs.append(S[i:])

outputs.sort()

for suffix in outputs:
    print(suffix)