import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, input().split())
board = [list(map(str, input())) for _ in range(n)]

move = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
visited = [[-1] * m for _ in range(n)]
count = 0
zone = 0

def dfs(x,y,zone):
    visited[x][y] = zone # 구역처리
    dx, dy = move[board[x][y]] # 현재노드가 가르키는 방향
    # 다음 노드
    nx = x + dx
    ny = y + dy
    print(nx,ny,"방문여부",visited[nx][ny],zone)

    if visited[nx][ny] == -1 : # 다은 노드가 방문 안 한 지역 일때
        dfs(nx, ny, zone) # 방문처리를 해주고, 구역번호도 같이 넘겨준다.

    # dfs 를 통해 한바퀴를 통해 자기자신으로 돌아오면 구역이 생성된다. count += 1
    elif visited[nx][ny] == zone :
        global count
        count += 1
        return

    # 방문 을 했는데 다른 구역 번호가 있다.
    # 두 개의 구역이 하나의 세이프존만 있어도 사용 가능하다.
    # 즉 둘이 연결된다
    else:
        return
for x in range(n):
    for y in range(m):
        if visited[x][y] == -1 :
            dfs(x, y, zone)
            zone += 1 # 구역번호 증가
print(count)


# 3 3
# DRD
# DLL
# RUU > 1개필요