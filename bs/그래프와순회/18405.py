import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, k = map(int, input().split(" "))
graph = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]
s, a, b = map(int, input().split(" "))

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
Q = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            Q.append((graph[i][j], i, j))
Q.sort()

Q = deque(Q)
time = 0
while Q:
    if time == s:
        break
    for i in range(len(Q)):
        virus, x, y = Q.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]
                Q.append((graph[nx][ny], nx, ny))
    time += 1
print(graph[a-1][b-1])