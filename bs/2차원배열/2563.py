import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
# 가로세로 100 짜리 만들어줌
board = [[0] * 101 for i in range(101)]

for i in range(N):
    x, y = map(int,input().split(' '))
    for j in range(10):
        for z in range(10):
            board[x+j][y+z] = 1
res = 0
for i in board:
    res += i.count(1)
print(res)
