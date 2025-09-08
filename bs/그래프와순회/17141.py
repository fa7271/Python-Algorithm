
import sys
from collections import deque
from itertools import combinations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10 ** 6)

# N, M 입력 받기
N, M = map(int, sys.stdin.readline().split(" "))

# 연구소 상태 입력 받기
maps = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]

# 바이러스의 위치 저장
virus = []
move = [(0,1),(0,-1),(1,0),(-1,0)]

# 바이러스의 위치 찾기
for i in range(len(maps)):
    for j in range(len(maps)):
        if maps[i][j] == 2:
            virus.append((i,j))


def bfs(vir):
    Q = deque()
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    c = 0
    for i in vir:
        Q.append((i[0],i[1]))
        visited[i[0]][i[1]] = 0
    while Q:
        x, y = Q.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            # 상하좌우로 이동 가능한 경우
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 and maps[nx][ny] != 1:
                Q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                c = max(c, visited[x][y] +1)
    # 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and maps[i][j] != 1:
                return 1e9
    return c


def check(idx):
    global select, count
    # M개의 바이러스를 선택한 경우
    if len(select) == M:
        count = min(count, bfs(select))
        return
    for i in range(idx,len(virus)):
        x, y = virus[i]
        select.append((x,y))
        check(i+1)
        select.pop()

# 바이러스 위치 조합을 통해 모든 경우의 수를 확인
check(0)

# 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우
if count == 1e9:
    print(-1)
else:
    print(count)
