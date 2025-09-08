
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# N = int(input())
# M = int(input())
# loc = list(map(int,sys.stdin.readline().rstrip().split(" ")))
#
# res = 0
# #  가로등을 기준으로 오른쪽, 왼쪽 중 큰 값으로 바꿔줌
# if len(loc) == 1:
#     res = max(N - loc[0],loc[0])
# else:
#     H = loc[0]
#     for i in range(len(loc)):
#         # 맨 왼쪾
#         if i == 0:
#             H = loc[0] -0
#         # 맨오른쪽
#         elif i == len(loc) -1:
#             H = N - loc[i]
#         else:
#             N_H = loc[i] - loc[i-1]
#             if N_H % 2 :
#                 H = N_H//2 +1
#             else:
#                 H = N_H//2
#         res = max(res,H)
# print(res)
#
#
def bs(li, m):
    if li[1]-li[0] > m:
        return 0
    if li[-1]-li[-2] > m:
        return 0
    for i in range(1, len(li)-2):
        if (li[i+1]-li[i])/2 > m:
            return 0
    return 1

N, M = int(input()), int(input())
li = [0] + list(map(int, input().split())) + [N]
s, e = 0, N
res = 0
while s <= e:
    m = (s+e)//2
    if bs(li, m):
        e = m-1
        res = m
    else:
        s = m+1
print(res)