import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
graph = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = 0


def dfs(x, y, temp, depth):
    global result
    if depth == 3:
        result = max(result, temp)
        return
    else:
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # ㅗ 모양 만들기
                if depth == 1:
                    visited[nx][ny] = True
                    # 안 움직이고 그대로 있고 다음꺼는 넣어주고
                    dfs(x, y, graph[nx][ny] + temp, depth + 1)
                    # 돌려주고
                    visited[nx][ny] = False
                visited[nx][ny] = True
                dfs(nx, ny, graph[nx][ny] + temp, depth + 1)
                visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, graph[i][j], 0)
        visited[i][j] = False
print(result)
