import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

r, c, t = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(r)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

down_air, up_air = 1e9, 1e9

# 공기청정기 위치 확인
for i in range(r):
    if map[i][0] == -1:
        up_air = i
        down_air = i + 1
        break

# 미세먼지 확장

def bfs():
    # 얼만큼 바뀌는제 배열 선언
    arr = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if map[x][y] != 0 and map[x][y] != -1:
                temp = 0
                for dx, dy in move:
                    nx = dx + x
                    ny = dy + y
                    # 확산 가능
                    if 0 <= nx < r and 0 <= ny < c and map[nx][ny] != -1:
                        # 확산된 바이러스 배열 저장
                        arr[nx][ny] += map[x][y] // 5
                        # 빠진 바이러스 저장
                        temp += map[x][y] // 5
                #  깎여나간거 반영
                map[x][y] -= temp
    # 바뀐거 반영
    for i in range(r):
        for j in range(c):
            map[i][j] += arr[i][j]


def up():
    # 우 상 좌 하
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    # 이전
    temp = 0
    # 방향
    dir = 0
    # 시작 좌표
    x, y = up_air, 1
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        # 한바퀴 돎
        if x == up_air and y == 0:
            break
        #  방향 전환
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            dir += 1
            continue
        #  한칸씩 옮겨주기 바꿔주기
        map[x][y], temp = temp, map[x][y]
        x = nx
        y = ny


def down():
    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 시작 좌표
    x, y = down_air, 1
    dir = 0
    temp = 0
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        # 한바퀴 돎
        if x == down_air and y == 0:
            break
        #  방향 전환
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            dir += 1
            continue
        #  한칸씩 옮겨주기 바꿔주기
        map[x][y], temp = temp, map[x][y]
        x = nx
        y = ny
for _ in range(t):
    bfs()
    up()
    down()
print(sum([sum(i) for i in map]) + 2)