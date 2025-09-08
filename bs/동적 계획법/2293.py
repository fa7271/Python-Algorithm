import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n,k = map(int,sys.stdin.readline().split(" "))

lst = sorted([int(sys.stdin.readline().rstrip()) for i in range(n)])
dp = [0] * (k+1)
dp[0] = 1
# for i in lst:
#     dp[i] += 1
#
# for i in range(1,k+1):
#     for j in lst:
#         if j < i:
#             dp[i] = max(dp[j]+1, dp[i-j]+dp[j])
# print(dp[-1])


for coin in lst:
    for i in range(coin, k + 1):
        print(coin, i, dp, i-coin)
        dp[i] += dp[i - coin]

print(dp[k])