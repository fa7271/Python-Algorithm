import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
INF = int(1e9)
dp = [[None] * (1 << N) for _ in range(N)]

def dfs(x, visited):
    if visited == (1 << N) - 1:
        if graph[x][0]:
            return graph[x][0]
        else:
            return INF

    if dp[x][visited] != None:
        return dp[x][visited]

    min_v = INF
    for i in range(1, N):
        # 경로 없음
        if not graph[x][i]:
            continue
        #  이미 방문
        if visited & (1 << i):
            continue

        min_v = min(min_v, dfs(i, visited | (1 << i)) + graph[x][i])
    dp[x][visited] = min_v

    return dp[x][visited]


print(dfs(0, 1))
