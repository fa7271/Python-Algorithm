import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().split(" "))
lst = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
index_L = []
water = deque()
for x in range(len(lst)):
    for y in range(len(lst[0])):
        if lst[x][y] == "L":
            index_L.append((x, y))
        if lst[x][y] == "L" or lst[x][y] == ".":
            water.append((x,y))


start = index_L[0]
end = index_L[1]

Q = deque([(start[0],start[1])])
visited = [[False] * m for _ in range(n)]
count = 0


# 백조가 갈 수 있는 위치들 next_Q에 담김
def find_swan(lst, visited, Q):
    next_Q = deque()
    while Q:
        x, y = Q.popleft()
        if x == end[0] and y == end[1]:
            return True, []
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if lst[nx][ny] == "X":
                    next_Q.append((nx, ny))
                else:
                    Q.append((nx, ny))
    return False, next_Q


def melt_ice(water, lst):
    next_water = deque()
    while water:
        x, y  = water.popleft()
        for dx,dy in move:
            nx = x + dx
            ny = y + dy

            if not 0 <= ny < m or not 0 <= nx < n:
                continue
            if lst[nx][ny] == 'X':
                next_water.append((nx,ny))
                lst[nx][ny] = '.'
    return next_water


while True:
    flag, Q = find_swan(lst, visited, Q)  # 백조가 다음 턴에 설 수 있는 위치 찾기
    if flag:
        break
    water = melt_ice(water, lst)
    print(water, Q)
    count += 1

print(count)
