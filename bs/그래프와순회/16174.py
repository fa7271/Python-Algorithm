import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())

maps = [list(map(int,sys.stdin.readline().split(" "))) for _ in range(N)]

dx, dy = [0, 1], [1, 0]
visited = [[False]*N for _ in range(N)]
Q = deque([(0,0,maps[0][0])])

while Q:
    x, y, count = Q.popleft() # 뽑아주고

    if maps[x][y] == -1:
        print("HaruHaru")
        exit()

    if maps[x][y] == 0:
        break

    for i in range(2):
        nx = x + dx[i] * count
        ny = y + dy[i] * count
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
            Q.append((nx,ny,maps[nx][ny]))
            visited[nx][ny] = True # 현재 밟은걸로 바꿔줌.

print("Hing")
