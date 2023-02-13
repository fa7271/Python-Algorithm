import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')



def bfs(v):
    Q = deque([N])
    while Q:
        v = Q.popleft()
        if v == M :
            return visited[v]

        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v <= 100000 and not visited[next_v]:
                visited[next_v] = visited[v] + 1
                Q.append(next_v)
N,M = map(int,input().split(" "))
visited = [0] * 100001
print(bfs(N))





