import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

xs, ys = map(int, input().split(" "))
xe, ye = map(int, input().split(" "))

def cal_distance(dot1, dot2):
    return abs(dot1[0] - dot2[0]) + abs(dot1[1] - dot2[1])

spots = [0] * 8
spots[0] = (xs, ys)
spots[7] = (xe, ye)

graph = [[1e9] * 8 for _ in range(8)]
graph[0][7] = graph[7][0] = cal_distance(spots[0], spots[7])

for i in range(1, 4):
    x1, y1, x2, y2 = map(int, input().split())
    # 거리들 순서대로 받아옴
    spots[i * 2 - 1] = (x1, y1)
    spots[i * 2] = (x2, y2)

    # 양방향 점프가능
    # 점프하는거랑 두개 사이 거리랑 가까운걸로
    graph[i * 2 - 1][i * 2] = graph[i * 2][i * 2 - 1] = min(cal_distance(spots[i * 2 - 1], spots[i * 2]), 10)

for i in range(8):
    for j in range(8):
        graph[i][j] = min(graph[i][j], cal_distance(spots[i], spots[j]))

for k in range(8):
    for i in range(8):
        for j in range(8):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

print(graph[0][7])
