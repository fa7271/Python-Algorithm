
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, M = map(int,sys.stdin.readline().rstrip().split(" "))

board = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            board[i][j] = min(board[i][j],board[i][k]+board[k][j])

for i in range(M):
    x, y, e = map(int,sys.stdin.readline().rstrip().split(" "))
    if board[x-1][y-1] <= e :
        print("Enjoy other party")
    else:
        print("Stay here")