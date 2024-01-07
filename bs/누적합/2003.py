import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().split(" "))
Number = list(map(int, sys.stdin.readline().split(" ")))

left = 0; right = 0

count = 0
while right < n:
    res = sum(Number[left:right+1])
    if res == m:
        count += 1
        right += 1
    elif res > m:
        left += 1
    else:
        right += 1
print(count)




#
# dp = [[0] * (n) for _ in range(n)]
# for i in range(n):
#     dp[i][i] = Number[i]
#
# # 시작 좌표
# count = 0
# for x in range(n):
#     # 도착 좌표
#     for y in range(x + 1, n):
#         if dp[x][y-1] > m:
#             break
#         dp[x][y] = dp[x][y - 1] + Number[y]
#
# for i in dp:
#     count += i.count(m)
# print(count)
#
