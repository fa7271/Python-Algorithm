import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(input())
    team = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    graph = [[] for _ in range(n + 1)]
    inDegree = [0 for _ in range(n + 1)]
    x = int(input())
    for j in range(n - 1):
        for k in range(j + 1, n):
            graph[team[j]].append(team[k])
            inDegree[team[k]] += 1
    for _ in range(x):
        a, b = map(int, sys.stdin.readline().rstrip().split(" "))
        if a in graph[b]:
            graph[b].remove(a)
            graph[a].append(b)
            inDegree[b] += 1
            inDegree[a] -= 1
        else:
            graph[a].remove(b)
            graph[b].append(a)
            inDegree[a] += 1
            inDegree[b] -= 1
    Queue = deque()
    for i in range(1, n+1):
        if inDegree[i] == 0:
            Queue.append(i)
    if not Queue:
        print("IMPOSSIBLE")
        continue
    # 위상정렬

    res = []
    while Queue:
        node = Queue.popleft()
        res.append(node)
        for next_node in graph[node]:
            inDegree[next_node] -= 1
            if inDegree[next_node] == 0:
                Queue.append(next_node)
    if sum(inDegree) >0:
        print("IMPOSSIBLE")
    else:
        print(*res)
