import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

lst1 = [""] + [i for i in sys.stdin.readline().rstrip()]
lst2 = [""] + [i for i in sys.stdin.readline().rstrip()]
dp = [[""] * (len(lst2)) for _ in range(len(lst1))]
for i in range(1, len(lst1)):
    for j in range(1, len(lst2)):
        if lst1[i] == lst2[j]:
            dp[i][j] = dp[i - 1][j - 1] + lst2[j]
        else:
            # dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            # 그냥 냅다 비교하면 문자열 순서임 예를들면 ACB, CA >> CA가 우선
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
print(len(dp[-1][-1]), dp[-1][-1], sep="\n")
