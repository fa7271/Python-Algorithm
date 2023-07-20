import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, M = map(int, sys.stdin.readline().split(" "))
board = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + board[i - 1][j - 1]




# visited = [[False]*M for _ in range(N)]
# move = [(1,0),(0,1),(1,1)] #우,하,대각
# start = [0,0]
# Q = deque([(0, 0)])
# while Q:
#     x, y = Q.popleft()
#     visited[x][y] = True
#     if x == N-1 and y == M-1:
#         print(board[x][y])
#         break
#     for dx, dy in move:
#         nx = dx + x
#         ny = dy + y
#         if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
#             board[nx][ny] += board[dx][dy]
#             Q.append((nx,ny))

