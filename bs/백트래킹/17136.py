import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

graph = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(10)]
# 5장씩
possible = [5, 5, 5, 5, 5]
result = 26

def checkXY(y, ny, x, nx):
    for i in range(y, ny + 1):
        for j in range(x, nx + 1):
            if graph[i][j] == 0:
                return False
    return True


def attach(y, ny, x, nx, param):
    for i in range(y, ny + 1):
        for j in range(x, nx + 1):
            graph[i][j] = param


def bt(count):
    global result
    for y in range(10):
        for x in range(10):
            if graph[y][x]:
                for i in range(5):
                    ny, nx = y + i, x + i
                    # 범위 안이면서, 색종이가 남음
                    if possible[i] != 0 and ny < 10 and nx < 10:
                        # 방향 다 가능한지 체크
                        if checkXY(y, ny, x, nx):
                            attach(y, ny, x, nx, 0)
                            possible[i] -= 1
                            bt(count + 1)
                            attach(y, ny, x, nx, 1)
                            possible[i] += 1
                return
    result = min(result, count)


bt(0)
print(result if result != 26 else -1)
