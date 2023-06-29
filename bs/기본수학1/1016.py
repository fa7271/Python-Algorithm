import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

X, Y = map(int, sys.stdin.readline().split(" "))
res = Y - X + 1
board = [1] * res
lst = [i**2 for i in range(2, int(Y ** 0.5) + 1)]
#     j = i ** 2
#     start = (X // j) * j
#     if start < X:
#         start += j
#     for k in range(start, Y + 1, j):
#         if not board[k - X]:
#             board[k - X] = True
#             res -= 1
#
# print(res)
for i in lst:
    n = (X//i)*i
    while n < Y+1:
        if n - X >= 0:
            board[n-X] = 0
        n += i
print(sum(board))
