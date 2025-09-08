import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
lst = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(n)]
move = [(0, 1), (-1, 0), (0, -1), (1, 0)]
now_x, now_y, size = 0, 0, 2
for x in range(n):
    for y in range(n):
        if lst[x][y] != 0:
            if lst[x][y] == 9:
                now_x = x
                now_y = y  # 물고기 크기, 시작위치, 총 거리, 잡아먹은 물고기.


def bfs(x, y, size):
    visited = [[0] * n for _ in range(n)]  # 방문리스트
    dis = [[0] * n for _ in range(n)]  # 아기상어로부터 얼마나 떨어져 있는지 담기 위함

    Q = deque([(x, y)])
    visited[x][y] = 1  # 시작지점 방문처리
    next_Q = []
    while Q:
        a, b = Q.popleft()
        for dx, dy in move:
            nx = dx + a
            ny = dy + b
            # 방문하지 않았고, 범위 내일때
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 나보다 작으면 먹고, 같으면 지나가고, 크면 지나가지도 못함.
                # 잡아먹거나 지나가기 가능
                if lst[nx][ny] <= size:
                    Q.append((nx, ny))
                    dis[nx][ny] = dis[a][b] + 1
                    visited[nx][ny] = 1
                    # 잡아먹기
                    if lst[nx][ny] < size and lst[nx][ny] != 0:
                        next_Q.append((nx, ny, dis[nx][ny]))
    # 거리 짧은순, 가장 위쪽, 가장 왼쪽 인데
    # 리스트로 팝 할거라 - 붙여줌 그러면 맨 위에 들어감
    return sorted(next_Q, key = lambda x : (-x[2],-x[0],-x[1]))

res = 0
eat_size = 0 # 먹은 물고기 수
while True:
    next_eat = bfs(now_x, now_y, size)
    if len(next_eat) == 0:
        break
    next_x, next_y, dis = next_eat.pop()
    # 거리 추가
    res += dis
    # 물고기 먹으면 0 으로 바꿔줌, 내가 있던 위치도 0 됨
    lst[now_x][now_y] = 0; lst[next_x][next_y] = 0


    # 다음위치 바꿔줌
    now_x = next_x; now_y = next_y

    # 갔다 왔으니깐 한마리 먹어주고
    eat_size += 1

    # 마리수 만큼 식사 했으면
    if eat_size == size:
        # 진화
        size += 1
        # 다음엔 1마리 더 먹고 와야함
        eat_size  = 0
print(res)
# while Q:
#     size, now_x, now_y, dis, eatcount = Q.popleft()
#     print(size,now_x)
#     for dx ,dy in move:
#         # 다음 좌표
#         nx = now_x + dx
#         ny = now_y + dy
#
#         # 범위 안 잡아먹을 물고기, 혹은 지나갈 수 있는것들
#         if 0 <= nx < n and 0 <= ny < n:
#             # 물고기가 없어서 지나가기만 가능
#             if lst[nx][ny] == 0:
#                 Q.append((size, nx, ny, dis+1, eatcount))
#             # 다음 노드 물고기가, 나보다 작아서 잡아 먹기 가능함.
#             elif lst[nx][ny] < size:
#                 lst[nx][ny] = 0
#                 eatcount += 1
#                 # 갯수만큼 잡아 먹고 레벨업
#                 if eatcount == size:
#                     Q.append((size +1 , nx, ny, dis +1, 0))
#                 # 아직 레벨업하기에는 부족.
#                 else:
#                     Q.append((size, nx, ny, dis+1, eatcount))
#             # 나랑 크기가 같아 먹지는 못하고 지나갈수만 있음.
#             elif lst[nx][ny] == size:
#                 Q.append((size, nx, ny ,dis+1,eatcount))
