import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, input().split(" "))
board = [list(map(int,input())) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
move = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs():
    Q = deque()
    Q.append((0,0,0))
    visited[0][0][0] = 1 # 3차원 리스트 맨 마지막 벽을 아직 안 부심

    while Q:
        x, y, e = Q.popleft()
        if x == n - 1 and y == m - 1 :
            return visited[x][y][e]
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            # 이동할 위치가 맵 범위내에 있고, 해당 위치의 값이 벽이 아니고, 아직 방문하지 않았다면
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and visited[nx][ny][e] == 0:
                visited[nx][ny][e] = visited[x][y][e] + 1
                Q.append((nx,ny,e))
            # 이동할 위치가 맵 범위내에 있고, 해당 위치의 값이 벽이며, 벽을 부순 횟수가 0 인경우
            elif 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and e == 0:  # 다음 칸이 벽이고 아직 뿌시기 가능 할경우
                visited[nx][ny][e+1] = visited[x][y][e] + 1
                Q.append((nx,ny,e+1))
    return -1
print(bfs())
print(visited[0][0][1])
