# 정렬을 어떻게, 어떤 자료구조를 써야 가장 빠르게 할 수 있을까
 
from sys import stdin

n = int(stdin.readline())
ropes = []

for _ in range(n):
    ropes.append(int(stdin.readline()))

ropes.sort(reverse=True)

max = -1

for idx, rope in enumerate(ropes):
    temp = (idx+1) * rope
    if max < temp:
        max = temp

print(max)