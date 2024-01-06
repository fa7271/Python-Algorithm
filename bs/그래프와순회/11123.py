import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10**6)
T = int(input())
move = [(1,0),(-1,0),(0,-1),(0,1)]
def dfs(y, x):
    graph[y][x] = False

    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0<= nx <W and 0<= ny < H:
            if graph[ny][nx] == '#':
                dfs(ny, nx)

for _ in range(T):
    H,W = map(int, input().split())
    graph = [list(input()) for _ in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#':
                dfs(i, j)
                count += 1

    print(count)