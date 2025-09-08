import sys
from itertools import combinations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int,sys.stdin.readline().split(" "))
graph = [[] for _ in range(n)]
for i in range(n):
    lst = list(map(int,sys.stdin.readline().split(" ")))
    for j in lst[1::]:
        graph[i-1].append(j)

x = list(combinations(graph,n-1))
flag = False
for i in x:
    a = sum(i,[])
    if len(set(a)) >= m:
        flag = True
print(1 if flag else 0)
