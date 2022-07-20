from sys import stdin

long_kmp = stdin.readline().strip()

long_kmp = long_kmp.split('-')

for i, name in enumerate(long_kmp):
    if i != len(long_kmp)-1 :
        print(name[0],end="")
    else:
        print(name[0])
