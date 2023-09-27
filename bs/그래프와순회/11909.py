import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


# 조건

# 1. 오른쪽, 아래 로만 가능
# 2. 1차원이 끝일때 아래로만
# 3. 2차원이 끝일떄 오른쪽으로만 가능
# 4. 마지막좌표
# 5. board[x][y] > board[z][k]
#
# n = int(sys.stdin.readline())
# graph =[[0 for _ in range(n+1)]]
# cost_save = [ [0 for _ in range(n+1)] for _ in range(n+1) ]
# for i in range(n) :
#     add=[0]+(list(map(int,sys.stdin.readline().split())))
#     graph.append(add)
# for i in range(1,n+1) : # 왼쪽이랑 위만 검사하면 됨
#     for j in range(1,n+1) :
#         cost_up = int(1e9)
#         cost_left = int(1e9)
#
#         if i-1 < 1 and j-1 < 1 : #왼쪽이나 위가 존재하지 않음
#             continue
#
#             # 위 가능하면
#         if i-1 >= 1 :
#             cost_up = cost_save[i-1][j]
#             # 위의 아이(graph[i-1][j])가 나(graph[i][j])보다 커야지 그냥 내려옴
#             # 내가 더 크다면 위의 아이를 나보다 크게 만들어줄 비용 발생
#             if graph[i][j] >= graph[i-1][j] :
#                 cost_up+=(graph[i][j]-graph[i-1][j])+1
#         # 왼쪽 가능하면
#         if j-1 >= 1 :
#             cost_left = cost_save[i][j-1]
#             if graph[i][j] >= graph[i][j-1] :
#                 cost_left+=(graph[i][j]-graph[i][j-1])+1
#
#         # 둘 중 더 작은 애를 내 비용으로
#         cost_save[i][j] = min(cost_up, cost_left)
#
# print(cost_save[n][n])

n = int(input())
graph =[[0]*(n+1)]+[[0] + list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]
dp = [[0]*(n+1)] + [[0] *(n+1) for _ in range(n+1)]
for x in range(1,n+1):
    for y in range(1,n+1):
        if x-1 < 1 and y-1 < 1 : #왼쪽이나 위가 존재하지 않음
            continue
        up, left = 1e9, 1e9
        # 위쪾이 가능
        if x-1 >= 1:
            up = dp[x-1][y]
            # 만약에 위에가 나보다 더 크면 나보다 더 크게 만들어야함
            if graph[x][y] >= graph[x-1][y]:
                up += graph[x][y] - graph[x-1][y] +1
        # 왼쪽이 가능
        if y-1 >= 1:
            left = dp[x][y-1]
            if graph[x][y] >= graph[x][y-1]:
                left += graph[x][y] - graph[x][y-1] + 1
        dp[x][y] = min(up,left)
print(dp[n][n])