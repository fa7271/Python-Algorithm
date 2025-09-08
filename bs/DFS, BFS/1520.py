import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10**6)
M,N = map(int, sys.stdin.readline().split(" "))
maps = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(M)]

visited = [[ 0 ] * N for _ in range(M)]
start = maps[0][0]; end = maps[M-1][N-1]
move = [(1,0),( -1,0),(0,-1),(0,1)] #상,하,좌,우
dp = [[-1 for _ in range(N)] for _ in range(M)]


def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1

    if dp[x][y] == -1: # 탐색 안 했으면
        dp[x][y] = 0 # 탐색 한걸로 만들어줌
        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < M and 0 <= ny < N:
                if maps[x][y] > maps[nx][ny]:
                    dp[x][y] += dfs(nx, ny)
    return dp[x][y]
print(dfs(0, 0))

