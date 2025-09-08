import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

board = sys.stdin.readline().split("-")
res = 0
for i in board[0].split("+"):
    res += int(i)
for i in board[1:]:
    for j in i.split("+"):
        res -=int(j)
print(res)


#
# board = sys.stdin.readline().strip().split("-")
# res = sum(int(i) for i in board[0].split("+"))
# for i in range(1, len(board)):
#     num = eval(board[i].lstrip("0"))
#     res -= num
#
# print(res)