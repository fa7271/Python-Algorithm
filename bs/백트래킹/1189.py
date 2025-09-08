import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

r, c, k = map(int,input().split())

board = [list(input()) for _ in range(r)]
wall = []
move = [(0,1),(0,-1),(1,0),(-1,0)]
end = [(0,c-1)]
for x in range(r):
    for y in range(c):
        if board[x][y] == "T":
            wall.append((x,y))
res = 0
Q = deque([(x,y)])
def bt(x,y,count):
    global res
    # 도착지 일경우
    if count == k and y == c-1 and x == 0:
        res += 1
    # 도착직 아닌경우 다음 목적지로 보냄
    else:
        # 현재 위치 방문처리
        board[x][y] = "T"
        for dx, dy in move:
            # 다음 목적지
            nx = dx + x; ny = dy +y;
            # 방문 가능한 범위와, 벽이 아닐때
            if 0<=nx<r and 0<=ny<c and board[nx][ny] ==".":
                # 벽으로 바꿔주고
                board[nx][ny] = "T"
                # 다음 재귀
                bt(nx,ny,count+1)
                # 갔다 와서 다시 가능 방문으로 바꿔놓음
                board[nx][ny] = "."
bt(r-1, 0, 1)
print(res)
