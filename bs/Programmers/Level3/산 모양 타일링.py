def solution(n, tops):
    dp = [0] * ((2 * n) + 1)
    dp[0] = 1
    if tops[0]:
        dp[1] = 3
    else:
        dp[1] = 2

    for i in range(2, 2 * n + 1):
        # 위에 타일 놓는 곳 + 둬야하는곳
        if i % 2 == 1 and tops[i // 2] == 1:
            dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 10007
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    print(dp[-1])


print(solution(2, [0, 1]))
# print(solution(2, [0, 1]))
"""
2차원dp , 1차원dp
점화식 후
"""
