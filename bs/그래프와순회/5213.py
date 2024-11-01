import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
graph = []
# 입력값 받기
for i in range(n):
    temp = []
    if not i % 2:
        for _ in range(n):
            temp.extend(list(map(int, sys.stdin.readline().rstrip().split(" "))))
    else:
        for _ in range(n - 1):
            temp.extend(list(map(int, sys.stdin.readline().rstrip().split(" "))))
        temp = [0] + temp + [0]
    graph.append(temp)

move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
visited = [[1e9] * 2 * n for _ in range(n)]
visited[0][0] = 1

# 타일 번호지정
tile = [[-1] * (2 * n) for _ in range(n)]
count = 1

for i in range(n):
    temp = 0
    for j in range(2 * n):
        if i % 2 and j in {0, 2 * n - 1}:
            continue
        tile[i][j] = count
        temp += 1
        if temp == 2:
            count += 1
            temp = 0

Q = deque([(0, 0)])
# 역추적
trace = [[(-1, -1)] * 2 * n for _ in range(n)]
trace[0][0] = (0, 0)
res_tile = -1
res_path = (0, 0)

# bfs 죽이기
while Q:
    x, y = Q.popleft()
    V = visited[x][y]
    for dx, dy in move:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < 2 * n:
            # 같은 타일이면서, 이미 방문한 타일 거리 체크
            if tile[x][y] == tile[nx][ny] and V < visited[nx][ny]:
                Q.append((nx, ny))
                visited[nx][ny] = V
                trace[nx][ny] = (x, y)
                if res_tile < tile[nx][ny]:
                    res_tile = tile[nx][ny]
                    res_path = (nx, ny)
            # 다른 타일이지만 숫자가 같고 이미 방문한 흔적이 있지만 내가 더 빠름
            elif graph[x][y] == graph[nx][ny] and V + 1 < visited[nx][ny]:
                Q.append((nx, ny))
                visited[nx][ny] = V + 1
                trace[nx][ny] = (x, y)
                if res_tile < tile[nx][ny]:
                    res_tile = tile[nx][ny]
                    res_path = (nx, ny)
# 거리 출력
print(visited[res_path[0]][res_path[1]])
# 거꾸로 오기

res =[]

def recursion(a, b):
    # 출발지점에 도달한 경우
    if trace[a][b] == (a, b):
        res.append(tile[a][b])
        return
    else:
        # 재귀
        recursion(trace[a][b][0], trace[a][b][1])
        # 이전에 추가된 타일과 현재 타일이 다른 경우에만 추가
        if not res or res[-1] != tile[a][b]:
            res.append(tile[a][b])

recursion(res_path[0], res_path[1])
print(*res)