import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
computer = int(input())
line = int(input())


graph = [[] for _ in range(computer+1)]

for i in range(line):
    start, end = input().split(" ")
    graph[int(start)].append(int(end))
    graph[int(end)].append(int(start))

Q = deque([1])

visited = [False] * (computer +1)
while Q :
    q = Q.popleft()
    for i in graph[q]:
        if visited[i] == False:
            Q.append(i)
            visited[i] = True
print(sum(visited)-1)


# DFS 방식

visitedd = [False] * (computer +1)
def BFS(depth):
    visitedd[depth] = True

    for v in graph[depth]:
        if visitedd[v] == False:
            BFS(v)
BFS(1)
print(sum(visitedd)-1)
