import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, M, R = map(int,sys.stdin.readline().rstrip().split(" "))
board = []
deq = deque()

for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

loops = min(N, M) // 2
for i in range(loops):
    deq.clear()
    deq.extend(board[i][i:M-i])	# 위쪽
    deq.extend([row[M-i-1] for row in board[i+1:N-i-1]]) 	# 오른쪽
    deq.extend(board[N-i-1][i:M-i][::-1]) 		# 아래쪽
    deq.extend([row[i] for row in board[i+1:N-i-1]][::-1]) 	# 왼쪽
    deq.rotate(-R)

    for j in range(i, M-i): # 위 1,2,3,4
        board[i][j] = deq.popleft()
    for j in range(i+1,N-i-1):#2,4/ 3,4/ 4,/5
        board[j][M-i-1] = deq.popleft()
    for j in range(M-1-i,i-1,-1) : # 왼쪽으로 가로
        board[N-i-1][j] = deq.popleft()
    for j in range(N-i-2,i,-1): # 맨왼쪽 위로
        board[j][i] = deq.popleft()
for i in board:
    print(*i)