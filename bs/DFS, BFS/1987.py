import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

#
# R,C = map(int,input().split(" "))
# maps =[[i for i in sys.stdin.readline().rstrip()] for i in range(R)]
#
# def bfs():
#     move = [(1,0),( -1,0),(0,-1),(0,1)]
#     result = 0
#     q = set([(0, 0, maps[0][0])])
#     while q:
#         x, y, ck = q.pop()
#         result = max(result, len(ck))
#         for dx, dy in move:
#             nx = x + dx
#             ny = y + dy
#             if R > nx >= 0 and C > ny >= 0 and maps[nx][ny] not in ck:
#                 q.add((nx, ny, maps[nx][ny] + ck))
#     return result
# print(bfs())


r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = set()
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
ans = 0
def dfs(x, y, cnt):
    global ans

    ans = max(ans, cnt)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and not graph[nx][ny] in visited:
            visited.add(graph[nx][ny])
            dfs(nx, ny, cnt + 1)
            visited.remove(graph[nx][ny])

visited.add(graph[0][0])
dfs(0, 0, 1)

print(ans)

