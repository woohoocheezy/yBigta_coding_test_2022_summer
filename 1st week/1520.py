from sys import stdin

def dfs(x, y):

    # stop
    if x == m-1 and y == n-1 :
        print("!!!!!")
        return 1
    
    if possible_direction[x][y] != -1 :
        return possible_direction[x][y]

    # search
    possible_direction[x][y] = 0

    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        # print(x1, y1)

        if 0 <= x1 < m and 0 <= y1 < n and total_map[x1][y1] < total_map[x][y]:
            print(x1, y1)
            possible_direction[x][y] += dfs(x1, y1)

    return possible_direction[x][y]     

m, n = map(int, stdin.readline().split())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
total_map = []

for _ in range(m):
    total_map.append(list(map(int, stdin.readline().split())))

possible_direction = [[-1] * n for _ in range(m)]


# print(total_map)
print(possible_direction)

print(dfs(0, 0))
print(possible_direction)
