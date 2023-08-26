
import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
import sys
from itertools import combinations

city = int(input())
points = [0] + [int(i) for i in input().split()]
nums = [i for i in range(1, city + 1)]
graph = [[] for _ in range(city + 1)]

for i in range(city):
    lst = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    graph[i+1] = lst[1:]

def bfs(lst):
    Q = deque()
    Q.append(lst[0])
    visit = [0] * (city+1)
    visit[lst[0]] = 1
    while Q:
        node = Q.popleft()
        for next_node in graph[node]:
            if next_node in lst and visit[next_node] == 0:
                Q.append(next_node)
                visit[next_node] = 1
    for i in lst:
        if visit[i] == 0:
            return False
    return True
res = 1000
for i in range(1,city//2 +1):
    for left in combinations(nums,i):
        right = [i for i in nums if i not in left]
        if bfs(left) and bfs(right):
            sum_left = sum(points[i] for i in left)
            sum_right = sum(points[i] for i in right)

            res = min(res ,abs(sum_left-sum_right))
if res == 1000:
    print(-1)
else:
    print(res)