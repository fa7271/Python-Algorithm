import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n,m,k = map(int,sys.stdin.readline().split()) # 세로 가로 쓰레기 수
gar = [list(map(int,sys.stdin.readline().rsplit())) for _ in range(k)] # 쓰레기 좌표
graph =[[0]*m for _ in range(n)] # 기본 틀
visited =[[False]*m for _ in range(n)] # 기본 틀
move = [(0,1),(0,-1),(1,0),(-1,0)]
res = 0
for x,y in gar:
    graph[x-1][y-1] = "*"
def bfs(a,b):
    Q = deque([(a,b)])
    visited[a][b] = True
    count = 1
    while Q:
        x, y = Q.popleft()
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            # 다음꺼 체크 가능 한 경우
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == "*":
                # 다음 좌표 추가 해주고
                Q.append((nx,ny))
                # 방문예정이니깐 True 바꿔줌
                visited[nx][ny] = True
                count += 1
    return count

for i in range(n):
    for j in range(m):
        # 쓰레기면
        if graph[i][j] =="*" and not visited[i][j]:
            # 체크하러감
            cnt = bfs(i,j)
            res = max(res,cnt)
print(res)



