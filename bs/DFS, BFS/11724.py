import sys
sys.setrecursionlimit(100000)
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
input = sys.stdin.readline
N, M = map(int,input().split(" "))
board = [[] for _ in range(N+1)]
visited = [False]* ( N + 1 )

for i in range(M):
    u, v = map(int,input().split(" "))
    board[u].append(v)
    board[v].append(u)

def dfs(v):
    visited[v] = True
    for e in board[v]:
        if visited[e] == False:
            visited[e] = True
            dfs(e)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)

