import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, k = map(int, sys.stdin.readline().split(' '))
dp =[[False,False] for _ in range(500001)] # 짝수 홀수 나눠서 생각
# 방문한 곳을 또 가면 방문처리에서 못 간다.
if n == k:
    print(0)
    exit()
Q = deque([n])
time = 1
k += time
while True:
    # 50만 초과시 종료
    if k > 500000:
        break

    res = []
    for node in Q:
        for next_node in [node+1, node-1, 2*node]:
            if 0 <= next_node <= 500000 and not dp[next_node][time % 2]:
                res.append(next_node)
                dp[next_node][time % 2] = time
    if dp[k][time%2]:
        print(time)
        exit()
    Q = res
    time += 1
    k += time
print(-1)





