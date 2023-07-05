import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N =int(sys.stdin.readline())
board = list(map(int,sys.stdin.readline().split(" ")))
res = 0
for i in range(N-1, -1, -1):
    if res <= board[i]:
        res = board[i]
    else:
        if res % board[i]:
            res = (res // board[i] + 1) * board[i]
print(res)
