import sys, time

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n = int(input())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[0] * n for _ in range(2)]
dp[0][0] = lst[0]
dp[1][0] = lst[0]
for i in range(1, n):
    # 숫자 제거 하지 않는경우
    dp[0][i] = max(lst[i], dp[0][i - 1] + lst[i])
    # 숫자 제거하는 경우
    # i 번째 원소를 제거, i이전에 이미 제거 된 경우
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + lst[i])
print(max(max(dp[0]), max(dp[1])))
