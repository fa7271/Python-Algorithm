import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
lst = list(map(int,sys.stdin.readline().split(" ")))
m = int(input())


dp = [[0] * (n) for _ in range(n)]
# 길이가 1 일때
for i in range(n):
    for j in range(n):
        if i == j :
            dp[i][j] = 1
#길이가 2 일때
for i in range(n-1):
    if lst[i] == lst[i+1]:
        dp[i][i+1] = 1
# 길이가 3 이상일때.
for length in range(3, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        # i는 시작지점 j는 끝지점 i와 j가 같고 [i+1][j-1] 이 팰린드롬이면 이것도 팰린드롬이다.
        if lst[i] == lst[j] and dp[i+1][j-1]:
            dp[i][j] = 1
res = []
for _ in range(m):
    left , right = map(int,sys.stdin.readline().split(" "))
    res.append(dp[left-1][right-1])
print(*res,sep="\n")
