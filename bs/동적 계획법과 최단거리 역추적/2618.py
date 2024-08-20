import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
w = int(input())
case = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(w)]

dp = [[] for _ in range(n+1)]
move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
polices = [(1, 1, 0), (n, n, 1)]

res = 0


def check(polices, a, b):
    visited = [[[-1, -1] for _ in range(n + 1)] for _ in range(n + 1)]
    Q = deque()
    for police in polices:
        visited[police[0]][police[1]][0] = 0
        visited[police[0]][police[1]][1] = police[2]
        Q.append((police[0], police[1], police[2]))
    while Q:
        x, y, car = Q.popleft()
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            if 1 <= nx <= n and 1 <= ny <= n:
                if visited[nx][ny][0] == -1:
                    visited[nx][ny][0] = visited[x][y][0] + 1
                    visited[nx][ny][1] = car
                    Q.append([nx, ny, car])
                elif visited[x][y][0] + 1 < visited[nx][ny][0]:
                    visited[nx][ny][0] = visited[x][y][0] + 1
                    Q.append((nx, ny, car))
    return visited


res = 0
res2 = []
for x, y in case:

    temp = check(polices, x, y)
    res += temp[x][y][0]
    if temp[x][y][0] == 0:
        polices[0] = (x, y, 0)
    else:
        polices[1] = (x, y, 1)
    res2.append(temp[x][y][1] + 1)
print(res)

print(*res2, sep='\n')

