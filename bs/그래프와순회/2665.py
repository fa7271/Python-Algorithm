import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, input().split())
board = [list(map(str,input())) for _ in range(n)]

move = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
def dfs(x,y, zone):
    # 방문 처리 해주고
    visited[x][y] = zone
    now = board[x][y]
    dx, dy = move[now]
    nx = dx + x; ny = dy + y
    # 방문하지 않은 구역
    if visited[nx][ny] == -1:
        # 다음 좌표로 이동
        dfs(nx, ny, zone)
    # 방문 한 구역
    # 다 돌고 돌아옴 즉 싸이클 형성
    elif visited[nx][ny] == zone:
        global count
        count += 1
        return
    # 방문 을 했는데 다른 구역에 숫자가 있다
    # 즉 둘이 연결된다. 세이프존 안 만들어도 된다
    else:
        return
visited = [[-1] * m for _ in range(n)]
count = 0; zone = 0
for x in range(n):
    for y in range(m):
        # 방문 안했으면
        if visited[x][y] == -1:
            # x, y, safezone 0 부터 순서대로 올라감
            dfs(x, y, zone)
            # 다음 safe zone
            zone += 1
print(count)
