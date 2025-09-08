import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10*6)
n, m = map(int,sys.stdin.readline().split(" "))
dp = [0] * 100001 # 거리 저장
check = [0] * 100001 # 경로 저장
Q = deque([n])

# 지나온 경로 찾기 위한 dfs 시동 걸어야함.
def find(node):

    res = []
    for i in range(dp[node] + 1):
        res.append(node)
        node = check[node]
    print(*res[::-1])


while Q:
    node = Q.popleft()
    if node == m:
        dp_len = dp[node]
        print(dp[node])
        find(node)
        break
    for next_node in [node-1,node+1, 2*node]:
        if 0 <= next_node <= 100000 and not dp[next_node]:
            dp[next_node] = dp[node] + 1
            Q.append(next_node)
            check[next_node] = node

