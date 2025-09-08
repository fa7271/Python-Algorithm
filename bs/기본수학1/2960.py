import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, k = map(int, sys.stdin.readline().split(" "))

dp = [True] * (n + 1)
count = 0
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if dp[j]:
            dp[j] = False
            count += 1
            if count == k:
                print(j)
                exit()
# 2 4 6 8 10 12 14 3 6 9 15
