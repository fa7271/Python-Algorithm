import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

C, N = map(int,input().split(" "))

lst = [list(map(int,input().split(" "))) for _ in range(N)]
dp = [0]+ [1e9] * (C+100)

for x, y in lst:
    for i in range(y,C+100):
        dp[i] = min(dp[i-y]+x, dp[i])
print(min(dp[C:]))

# C,N = map(int,input().split())
# cost_list = [list(map(int,input().split())) for _ in range(N)]
# dp = [1e7 for _ in range(C+100)]
# dp[0]=0
#
# for cost, num_people in cost_list:
#     for i in range(num_people,C+100):
#         dp[i] = min(dp[i-num_people]+cost,dp[i])
#
# print(min(dp[C:]))