
def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i, j in puddles: # 웅덩이가 있는 곳은 -1로 표시
        dp[j][i] = -1
    for x in range(1,n+1):
        for y in range(1,m+1):
            if dp[x][y] == -1:
                dp[x][y] = 0
            else :dp[x][y] += (dp[x-1][y] + dp[x][y-1]) % 1000000007
    return dp[n][m]


print(solution(4, 3,[[2, 3]]))


# def solution(m, n, puddles):
#     dp = [[0]*(m+1) for _ in range(n+1)]
#     dp[1][1] = 1
#     for i, j in puddles: # 웅덩이가 있는 곳은 -1로 표시
#         dp[j][i] = -1
#
#     for x in range(1,n+1):
#         for y in range(1,m+1):
#             if dp[x][y] == -1:
#                 dp[x][y] = 0
#                 continue
#             dp[x][y] += (dp[x-1][y] + dp[x][y-1]) % 1000000007
#     return dp[n][m]
#
#
# print(solution(4, 3,[[2, 2]]))