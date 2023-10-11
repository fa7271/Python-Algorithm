import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int,input().split())
array = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
Q = deque()
for _ in range(m):
    x, y = map(int,input().split())
    array[x].append(y)
    # 진입차수
    indegree[y] += 1

for i in range(1,n+1):
    if indegree[i] == 0:
        Q.append(i)
res= []
while Q:
    num = Q.popleft()
    res.append(num)
    for i in array[num]:
        indegree[i] -= 1
        if indegree[i] == 0:
            Q.append(i)
print(*res)