import math
import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N, L, R = map(int,sys.stdin.readline().split())
move = [(1,0),(-1,0),(0,1),(0,-1)]
graph = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]


def bfs(x,y):
    Q = deque()
    Q.append((x,y))
    visited[x][y] = True

    sub_list = [(x,y)]
    sum_union = graph[x][y]
    while Q:
        x, y = Q.popleft()
        for a,b in move:
            nx = x + a
            ny = y + b
            if 0<= nx < N and 0<= ny <N and L <= abs(graph[nx][ny] - graph[x][y]) <= R and visited[nx][ny] == False :
                sub_list.append((nx, ny))
                visited[nx][ny] = True
                Q.append((nx, ny))
                sum_union += graph[nx][ny]
    for i, j in sub_list:
        graph[i][j] = math.floor(sum_union/ len(sub_list))
    return len(sub_list)

day = 0
while True:
    visited = [[False] * N for _ in range(N)]
    flag = False
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                if bfs(x,y) > 1:
                    flag = True
    if not flag:
        break
    day += 1
print(day)