import copy
import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int,sys.stdin.readline().split(" "))
boards = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
move = [(0,1),(0,-1),(-1,0),(1,0)]
res = 0


# 0 빈칸, 1 벽 2, 바이러스
# 벽은 3개 필수

# 벽 만들기, combinatins 써도 될까 ? 일단 bt로
def wall_bt(depth):
    if depth == 3:
        bfs()
        return
    for x in range(n):
        for y in range(m):
            if boards[x][y] == 0 : # 벽이 아니면
                boards[x][y] = 1 # 벽으로 만들어주고
                wall_bt(depth + 1) # 다음 벽 만들어줘야함
                boards[x][y] = 0 # 다른 조합을 위해 다시 빈칸으로 만들어줌

## 벽을 만들고 나서 bfs출발
def bfs():
    global res
    count = 0
    board = copy.deepcopy(boards) # 그래프 카피
    Q = deque()
    for x in range(n):
        for y in range(m):
            if board[x][y] == 2:
                Q.append((x,y))

    while Q:
        x, y = Q.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0:
                board[nx][ny] = 2
                Q.append((nx,ny))
    for i in range(n):
        count += board[i].count(0)
    res = max(res,count)

wall_bt(0)
print(res)
