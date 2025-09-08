import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
lst = list(map(int,sys.stdin.readline().split(" ")))

dp =[1] *(n)
for i in range(n-1,-1,-1):
    # 점프 범위 조건
    if i + lst[i] +1 < n:
        # 최댓값 업데이트
        dp[i] = dp[i + lst[i] +1]+ 1
print(*dp)

# 5 4 4 3 3 3 2 1 1


