import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

def solution(triangle):

    dp = [[0]*len(triangle) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(0, len(triangle)-1):
        for j in range(len(triangle[i])):
            print(i,j)
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])
            print(dp)
    return max(dp[-1])

N = int(input())
triangle = []
for i in range(N):
    triangle.append(list(map(int,input().split(' '))))
print(solution(triangle))

