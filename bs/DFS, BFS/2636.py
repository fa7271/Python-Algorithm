import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

def bfs():
    q = deque([(0,0)])
    melt = deque()

    while q:
        dx, dy = q.popleft()
        for x,y in move:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if maps[nx][ny] == 0:
                    q.append((nx,ny))
                elif maps[nx][ny] == 1:
                    melt.append((nx,ny))
    for x,y in melt:
        maps[x][y] = 0
    return len(melt)

n,m = map(int,sys.stdin.readline().split())
maps = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]
cnt =sum([sum(i) for i in maps])
move = [(1,0),(-1,0),(0,1),(0,-1)]
time = 1
while True:
    visited = [[0] * m for _ in range(n)]
    meltCnt = bfs()
    cnt -= meltCnt
    if cnt == 0:
        print(time,meltCnt)
        break
    time +=1
