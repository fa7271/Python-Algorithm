import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, k = map(int,sys.stdin.readline().split(" "))
# dp = [[0] * (k+1) for _ in range(n+1)]
# print(dp)
# lst = [[0,0]]
# for i in range(n):
#     lst.append(list(map(int, sys.stdin.readline().split())))
#
# for i in range(1, n + 1):
#     for j in range(1, k + 1):
#         v = lst[i][0]
#         e = lst[i][1]
#         print(v,e)
#         if j < v: # 가방무게 보다 해당 물건이 더 크면
#             dp[i][j] = dp[i - 1][j] # 이전 표 값 넣어줌
#         else: # 들어가는 경우에 이전 표값 vs (지금 가중치 + 이전 표값 가중치 뺀 위치)
#             dp[i][j] = max(dp[i - 1][j], e + dp[i - 1][j - v])
# print(dp[n][k])

# # sol 2
WV = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (k+1)
for w, v in WV:
    for i in range(k, w-1, -1):
        print(i, i-w, v)
        dp[i] = max(dp[i-w]+v, dp[i])
    break
print(dp[k])
