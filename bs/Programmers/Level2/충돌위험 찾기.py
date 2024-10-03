from collections import  Counter


def solution(points, routes):
    def bfs(route):
        idx = 0
        sx, sy = spots[route[0] - 1]
        for i in range(1, len(route)):
            ex, ey = spots[route[i] - 1]
            if idx == 0:
                second[idx].append((sx, sy))

            # x 좌표 맞추기
            while sx != ex:
                if sx < ex:
                    sx += 1
                else:
                    sx -= 1
                idx += 1
                if idx < len(second):  # 인덱스 범위 확인
                    second[idx].append((sx, sy))

            # y 좌표 맞추기
            while sy != ey:
                if sy < ey:
                    sy += 1
                else:
                    sy -= 1
                idx += 1
                if idx < len(second):  # 인덱스 범위 확인
                    second[idx].append((sx, sy))
            sx, sy = ex, ey

    spots = [i for i in points]
    second = [[] for _ in range(201)]

    for route in routes:
        bfs(route)
    res = 0
    for i in second:
        if i:
            temp = len(set(i))
            if temp != len(i):
                count = Counter(i)
                result = [key for key, value in count.items() if value >= 2]
                res += len(result)

    return res

