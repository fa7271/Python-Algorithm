import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n,k = map(int,input().split())
dp = [-1] * 20
dp[n] = 0
Q = deque()
Q.append(n)
# 제일 빠르게 가는 방법
count = 0
while Q:
    x = Q.popleft()
    if x == k :
        count += 1
    for next_node in [(x-1),(x+1),(2*x)]:
        if 0 <= next_node < 20:
            # 방문 아직 안 했거나, 이미 방문 했지만 현재길이 +1 인 경우
            if dp[next_node] == -1 or dp[next_node] == dp[x] + 1:
                dp[next_node] = dp[x] + 1
                Q.append(next_node)
print(dp)
print(count)
