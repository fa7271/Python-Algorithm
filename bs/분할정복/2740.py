import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, M = map(int,sys.stdin.readline().split(" "))
A = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]

M, K = map(int,sys.stdin.readline().split(" "))
B = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(M)]

# (N,K) 3.3
res = [[0]*K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            res[i][j] += A[i][k] * B[k][j]
for i in res:
    print(*i)
