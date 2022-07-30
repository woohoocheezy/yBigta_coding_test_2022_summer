from sys import stdin

S = int(stdin.readline())
count = 0
total = 0
x = 1

while True:
    total += x
    count += 1

    if total > S :
        count -= 1
        break

    x += 1

print(count)