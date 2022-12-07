def solution(n):
    dp = [0 for i in range(n+1)]
    dp[0],dp[2], = 1,3

    for i in range(4,n+1,2):
        dp[i] = (dp[i-2] * 4 - dp[i-4]) % 1000000007


    return dp[-1] if n % 2 == 0 else 0


# 점화식 f(i) = (f(i-2) * n) - f(i-4)


print(solution(8))