from sys import stdin,setrecursionlimit

setrecursionlimit(10**6)

def dfs(x, y):

    # stop
    if x == m-1 and y == n-1 :
        return 1

    # search
    possible_direction[x][y] = 0

    if m > x > 0 and total_map[x-1][y] < total_map[x][y] :
        possible_direction[x][y] += dfs(x-1, y)

    if n > y > 0 and total_map[x][y-1] < total_map[x][y]:
        possible_direction[x][y] += dfs(x, y-1)
    
    if 0 <= x < m-1 and total_map[x+1][y] < total_map[x][y] :
        possible_direction[x][y] += dfs(x+1, y)

    if 0 <= y < n-1 and total_map[x][y+1] < total_map[x][y] :
        possible_direction[x][y] += dfs(x, y+1)

    return possible_direction[x][y]     

m, n = map(int, stdin.readline().split())

total_map = []

for i in range(m):
    total_map.append(list(map(int, stdin.readline().split())))

possible_direction = [[-1] * n for _ in range(m)]

print(dfs(0, 0))

