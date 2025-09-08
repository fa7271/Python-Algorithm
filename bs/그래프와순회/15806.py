import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# 방크기, 곰팡이개수 좌표, 남은일수
n, m, k, t = map(int, sys.stdin.readline().split())

check = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
move = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]  # 이동경로
board = [[[False, False] for _ in range(n)] for _ in range(n)]  # 짝수면 왼쪽, 홀수면 오른쪽
Q = deque()
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    board[x - 1][y - 1][0] = True  # 짝수날 곰팡이 있다.
    Q.append((x - 1, y - 1, 0))  # 기숙사 청소 검사 시스템은 오늘로부터 정확히 t 일이 지나고 검사를 하며

    # 현재 곰팡이위치
while Q:
    x, y, day = Q.popleft()
    if day >= t:
        continue
    flag = False
    # 다음 곰팡이 위치
    for dx, dy in move:
        nx = dx + x
        ny = dy + y
        # 범위내에 위치하면

        if 0 <= nx < n and 0 <= ny < n:
            n_day = (day + 1) % 2
            if board[nx][ny][n_day] == True:
                continue  # 다음날도 바이러스가 있음
            board[nx][ny][n_day] = True
            Q.append((nx, ny, day + 1))
            flag = True

    if not flag:
        board[x][y][day % 2] = False
che_odd = t % 2
print(board)
for x, y in check:
    if board[x - 1][y - 1][che_odd] == True:
        print("YES")
        exit()
print("NO")
