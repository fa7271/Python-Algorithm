import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())

res_x = n // 2
res_y = n // 2
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

left = [[0, 0, 0.02, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0.05, 0, 0, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0, 0, 0.02, 0, 0]]


def rotate(pattern):
    return list(reversed(list(zip(*pattern))))  # 시계 방향 90도 회전


down = rotate(left)
right = rotate(down)
up = rotate(right)

res = 0


def solution(block, dx, dy, direction):
    global res, res_x, res_y

    for _ in range(block):
        res_x += dx
        res_y += dy

        if res_y < 0:  # 맵 밖
            return False

        sand = graph[res_x][res_y]  # 현재 모래
        graph[res_x][res_y] = 0  # 현재 위치 모래 일단 없앰
        spread_sand = 0  # 퍼진 모래 양 / 나중에 남은양 땜에

        # 퍼뜨리기
        for i in range(-2, 3):
            for j in range(-2, 3):
                if direction[i + 2][j + 2] > 0:  # 퍼질 모래 비율이 존재하면 0 이 아님
                    # 그 좌표가 뭐지 ?
                    nx = res_x + i
                    ny = res_y + j

                    # 얼마나 퍼지는거지 ?
                    sand_amount = int(sand * direction[i + 2][j + 2])
                    # 맵 밖으로 안 나가나? -? 그럼 이동
                    if 0 <= nx < n and 0 <= ny < n:
                        graph[nx][ny] += sand_amount  # 격자 내에 있으면 모래 추가
                    # 나간다고?
                    else:
                        res += sand_amount  # 결과에 추가
                    # 기존 좌표에서 날라간 모래
                    spread_sand += sand_amount
        #        안 퍼진 모래는 그대로 다음으로 넘어가야함
        remaining_sand = sand - spread_sand
        nx = res_x + dx
        ny = res_y + dy
        if 0 <= nx < n and 0 <= ny < n:
            graph[nx][ny] += remaining_sand
        else:
            res += remaining_sand


for block in range(1, n + 1):
    # 좌 하
    if block % 2 == 1:
        # 좌로 홀수칸
        solution(block, 0, -1, left)
        # 아래로 홀수칸
        solution(block, 1, 0, down)

    # 우 위
    elif block % 2 == 0:
        # 우로 짝수칸
        solution(block, 0, 1, right)
        # 위로 짝수칸
        solution(block, -1, 0, up)

print(res)
