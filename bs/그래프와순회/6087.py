import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

m, n = map(int,sys.stdin.readline().split(" "))
graph =[list(sys.stdin.readline()) for _ in range(n)]
spot = []
for i in range(n):
    for y in range(m):
        if graph[i][y] == "C":
            spot.append((i,y))

start = spot[0] ; end = spot[1]
move = [(0,1),(0,-1),(1,0),(-1,0)]
Q = deque()
Q.append((start[0],start[1]))
visited = [[1e9] * m for _ in range(n)]
visited[start[0]][start[1]] = -1
while Q:
    # 거울수, 방향, 현재 x위치, 현재 y위치
    x, y = Q.popleft()
    # 목적지 도착했을때
    if x == end[0] and y == end[1]:
        # 거울 뽑고 종료
        print(visited[x][y])
        break
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        #범위 내에 위치하면서, 벽이 아니고, 거울 안 쓴게 더 좋음
        while 0 <= nx < n and 0 <= ny < m and not graph[nx][ny] == "*" and visited[x][y] < visited[nx][ny]:
            if visited[nx][ny] == visited[x][y] + 1:
                nx, ny = nx + dx, ny + dy
                continue
            # 거울 설치
            visited[nx][ny] = visited[x][y] + 1
            # 다음 방향 큐에 추가
            Q.append((nx,ny))
            nx, ny = nx + dx, ny + dy
