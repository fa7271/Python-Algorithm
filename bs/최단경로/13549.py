import sys, heapq
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, k = map(int,input().split())
dp = [-1] * (100001)
dp[n] = 0

Q = deque()
Q.append(n)

while Q:
    x = Q.popleft()
    if x == k:
        print(dp[x])
    for next_node in [x-1, x+1, 2*x]:
        #방문처리
        if 0 <= next_node <= 100000 and dp[next_node] == -1:
            #순간이동일 경우
            if next_node == 2*x :
                dp[next_node] = dp[x]
                Q.appendleft(next_node)
            # 순간이동이 아닐경우
            else:
                dp[next_node] = dp[x] +1
                Q.append(next_node)