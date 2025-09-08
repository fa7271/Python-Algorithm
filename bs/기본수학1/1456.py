import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

A, B = map(int,sys.stdin.readline().split(" "))

board = [True] * (int(B ** 0.5) + 1)
board[1] = False
m = int(B **0.5)
for i in range(2,m+1):
    if board[i]:
        for j in range(i**2,m+1,i):
            board[j] = False

result = 0
for i in range(1, len(board)):
    if board[i]:
        res = i * i
        while True:
            if res < A:
                res *= i
            elif res > B:
                break
            res *= i
            result += 1
print(result)


