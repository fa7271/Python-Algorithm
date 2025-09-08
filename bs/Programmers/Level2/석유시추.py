from collections import deque, defaultdict


def solution(land):
    res = 0
    zone = 2  # 구역넘버 시작
    count = []
    dic_count = defaultdict(int)
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * len(land[0]) for _ in range(len(land))]

    # 구역별로, 갯수
    def bfs(a, b, zone):
        Q = deque([(a, b)])
        visited[a][b] = True
        land[a][b] = zone
        count = 1
        while Q:
            x, y = Q.popleft()
            for dx, dy in move:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < len(land) and 0 <= ny < len(land[0]) and not visited[nx][ny] and land[nx][ny] == 1:
                    visited[nx][ny] = True
                    land[nx][ny] = zone
                    Q.append((nx, ny))
                    count += 1
        return count

    for x in range(len(land)):
        for y in range(len(land[0])):
            if land[x][y] == 1 and visited[x][y] == False:
                dic_count[zone] = bfs(x, y, zone)
                zone += 1
    # x 좌표
    result = []
    for y in range(len(land[0])):
        result_temp =set()
        for x in range(len(land)):
            if land[x][y] != 0:
                result_temp.add(land[x][y])
        res = max(res,sum(dic_count[x] for x in result_temp))

    return res


print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 1, 1]]))  # 9
# print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]])) #16
