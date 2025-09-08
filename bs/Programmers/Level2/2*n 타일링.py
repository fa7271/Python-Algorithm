def solution(n):
    dp = [0 for i in range(n+1)]
    dp[1], dp[2] = 1, 2
    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[n]


print(solution(4))


def solution1(x):

    if x <= 2:
        return x
    else:
        return (solution1(x-1) + solution1(x-2)) % 1000000007

print(solution1(4))
