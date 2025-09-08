import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
K = int(input())
print(lst)
def dfs(k,lst):
    print(lst,k)
    lst[k] = 1e9 # 숫자 자
    for i in range(len(lst)):
        if k == lst[i]: # 어떤숫자의 부모가 k 이면 잘라야함
            dfs(i,lst)
dfs(K, lst)
count = 0
for i in range(len(lst)):
    if lst[i] != 1e9 and i not in lst: # 1e9 가 아니면서, 부모노드가 아님
        count += 1
print(count)

"""
import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())

graph = [[] for _ in range(N)]
lst =list(map(int,sys.stdin.readline().split(" ")))
for node,i in enumerate(lst[1:],start = 1):
    graph[node].append(i)
    graph[i].append(node)

x = int(input())
Q = deque([x])

# 삭제할 노드
while Q:
    now = Q.popleft()
    for i in graph[now]:
        if i > now:
            Q.append(i)
    graph[now] = False
res = 0
for i in graph:
    if i != False and len(i) == 1:
        res += 1
print(res)

"""