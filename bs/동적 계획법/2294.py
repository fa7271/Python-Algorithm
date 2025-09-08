import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, k = map(int,sys.stdin.readline().split(" "))
moneys = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)])
dp = [100001] * (k+1)
dp[0] = 0


for money in moneys:
    for i in range(money, k+1):
        dp[i] = min(dp[i], dp[i-money]+1)

if dp[i] == 100001:
    print(-1)
    exit()
else:
    print(dp[i])

