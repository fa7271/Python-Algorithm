import math
import sys
from math import comb

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

h, c = map(int,input().split())

# temp = abs(h-c) + 1
# board = [[0]* (temp) for _ in range(temp)]
# for i in range(temp):
#     board[0][i] = 1
#
# for i in range(1, temp):
#     for j in range(i, temp):
#         board[i][j] = board[i-1][j] + board[i][j-1]
# print(board[-1][-1])

# 2. 카탈란 수열
d = abs(h-c)
print(d*2,d)
print(comb(d*2,d)//-~d)

# 3. 카탈란 수열
def catalan(n):
    return math.factorial(2*n) // (math.factorial(n) * math.factorial(n+1))
print(catalan(d))