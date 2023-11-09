import sys
sys.stdin = open('/Python/h.txt', 'r')

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
dp = [0 for _ in range(n)]
for i in range(n):
    # 처음은 첫 회의가는 사람들
    if i ==0:
        dp[0] = lst[0][2]
    # 두 번째는 첫 회의가는 사람들 vs,어제 간 사람들
    # 회의 시간이 겹치지 않기 때문이다.
    elif i == 1:
        dp[1] = max(lst[1][2], dp[0])
    #나머지
    else:
        dp[i] = max(dp[i-2] + lst[i][2],dp[i-1])

print(dp[n-1])