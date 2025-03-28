import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m, k = map(int, sys.stdin.readline().split(" "))

S2D2 = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]

# 양분
vitamin = [[5] * n for _ in range(n)]

graph = [[deque() for _ in range(n)] for _ in range(n)]
dead_trees = [[list() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split(' '))
    graph[x - 1][y - 1].append(z)

move = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
def 봄_여름():
    for x in range(n):
        for y in range(n):
            l = len(graph[x][y])
            for k in range(l):
                if vitamin[x][y] < graph[x][y][k]:
                    for _ in range(k, l):
                        dead_trees[x][y].append(graph[x][y].pop())
                    break
                else:
                    vitamin[x][y] -= graph[x][y][k]
                    graph[x][y][k] += 1

    for x in range(n):
        for y in range(n):
            while dead_trees[x][y]:
                vitamin[x][y] += dead_trees[x][y].pop() // 2

def 가을_겨울():
    for i in range(n):
        for j in range(n):
            # 현재 위치의 나무들 탐색
            for k in range(len(graph[i][j])):
                # 현재 나무의 나이가 씨를 뿌릴 수 있는 상태인 경우
                if graph[i][j][k] % 5 == 0:
                    # 8방향에 씨 뿌림
                    for dx, dy in move:
                        nx = i + dx
                        ny = j + dy
                        # 범위 체크
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        # 새로 태어난 나무들 앞으로 삽입
                        graph[nx][ny].appendleft(1)
            # 밭에 양분 추가
            vitamin[i][j] += S2D2[i][j]


for _ in range(k):
    봄_여름()
    가을_겨울()

res = 0
for i in range(n):
    for j in range(n):
        res += len(graph[i][j])
print(res)