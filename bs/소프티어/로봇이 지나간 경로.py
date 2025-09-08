import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

H, W = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
visited = [[False] * W for _ in range(H)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
directions = ['^', '<', 'v', '>']


def check(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < H and 0 <= ny < W and maps[nx][ny] == '#':
            direction = i
            cnt += 1

    if cnt == 1:
        return direction
    else:
        return -1


def findstart(maps):
    for i in range(H):
        for j in range(W):
            if maps[i][j] == "#":
                dir = check(i, j)
                if dir != -1:
                    return i, j, dir


x, y, dir = findstart(maps)

def res(i, j, dir):
    maps[i][j] = "."
    pre_dir = new_dir = dir
    while True:
        while new_dir == pre_dir:
            print("A", end='')
            i, j = i + dx[new_dir], j + dy[new_dir]
            maps[i][j] = "."
            i, j = i + dx[new_dir], j + dy[new_dir]
            maps[i][j] = "."

            pre_dir = new_dir
            new_dir = check(i, j)
        if new_dir == -1:
            break
        elif (new_dir - pre_dir) % 4 == 1:
            print("L", end='')
        elif (new_dir - pre_dir) % 4 == 3:
            print("R", end='')
        pre_dir = new_dir
print(x+1,y+1)
print(directions[dir])
res(x, y, dir)
