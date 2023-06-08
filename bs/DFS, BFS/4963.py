import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(100000)


def dfs(x, y):
    move = [(1,0),( -1,0),(0,-1),(0,1),(-1,1),(1,1),(-1,-1),(1,-1)]

    maps[x][y] = 0
    for dx, dy in move:
        nx = x + dx
        ny = y + dy

        if 0 <= nx <h and 0 <= ny < w and maps[nx][ny] == 1:
            dfs(nx,ny)

while True:
    w, h = map(int,sys.stdin.readline().split(" "))
    if w == 0 and h == 0 :
        break
    count = 0
    maps = [list(map(int,sys.stdin.readline().split(" "))) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                dfs(i,j)
                count += 1
    print(count)


def bfs(x, y):
    move = [(1, 0), (-1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (-1, -1), (1, -1)]
    maps[x][y] = 0
    queue = deque([(x, y)])
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in move:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                queue.append((nx, ny))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    count = 0
    maps = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)