import sys,time

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

T = int(input())

def coin_dp(n, coins, m):
    dp = [0] * (m+1)
    for i in range(n):
        # 어떤 코인을 주던 coin 에 해당하는 값은 1개
        dp[coins[i]] += 1
        for j in range(coins[i],m+1):
            # 새로운 dp[j] 를 만드는 경우의 수는 dp[j-coin] + 기존 dp[j]
            print(j, j-coins[i])
            dp[j] += dp[j -coins[i]]
    return dp[m]

for _ in range(T):
    # 동전의 가짓수
    n = int(input())
    # 동전 오름차순
    coins = list(map(int,input().split()))
    # 맞춰야 하는 돈
    m = int(input())
    print(coin_dp(n,coins,m))
