
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from collections import deque
sys.setrecursionlimit(10**6)
"""
N, M = map(int,sys.stdin.readline().split())
move = [1,2,3,4,5,6]
maps = [0 for i in range(101)]
visited = [False] * (101)
for i in range(M+N):
    a, b = map(int,sys.stdin.readline().split(" "))
    maps[a] = b
Q =deque([(1,0)])

while Q :
    q,count = Q.popleft()
    if q == 100:
        print(count)
    count += 1
    for dx in move:
        nx = q + dx
        if nx > 100 or visited[nx]:
            continue
        visited[nx] = True
        if maps[nx]:
            Q.append((maps[nx],count))
        else:
            Q.append((nx,count))

카운트를 저장하는 방식

"""
import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())
maps = [0] * 101
visited = [False] * 101
move = [1,2,3,4,5,6]
Q = deque([(1,0)])
for i in range(N+M):
    a,b = map(int,sys.stdin.readline().split())
    maps[a] = b

while Q:
    q, count = Q.popleft()
    if q == 100:
        print(count)
        break
    for i in move:
        nx = q+i

        if nx <= 100 and not visited[nx]:
            visited[nx] = True
            if maps[nx] != 0:
                nx = maps[nx]
            Q.append((nx,count+1))

