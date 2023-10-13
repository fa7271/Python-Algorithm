import copy
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())

dp =[0] + [1e9] * (N-1)
jump = []
# 슈퍼점프 아직 미사용
for i in range(N-1):
    x, y = map(int,input().split())
    jump.append((x, y))
    # 원점
    if i+1 < N:
        dp[i+1] = min(dp[i] + x,dp[i+1])
    # 투쩜
    if i+2 < N:
        dp[i+2] = min(dp[i] +y , dp[i+2])
res=dp[-1]
k = int(input())
for idx in range(0, N-3):
    new_dp=copy.deepcopy(dp)

    if dp[idx] + k < dp[idx+3]:
        new_dp[idx+3] = dp[idx]+k
        for j in range(idx+4, N):
            new_dp[j] = min(dp[j], new_dp[j-1]+jump[j-1][0], new_dp[j-2]+jump[j-2][1])
        res = min(res,new_dp[-1])
print(res)