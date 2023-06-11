import sys
from itertools import combinations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

def solution(idx, depth):
    global res
    if depth == N // 2:
        start = 0; link = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j] :
                    start += lst[i][j]
                elif not visited[i] and not visited[j]:
                    link += lst[i][j]
        res = min(res, abs(start-link))
        return

    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            solution(i+1,depth+1)
            visited[i] = False

N = int(sys.stdin.readline().rstrip())
lst = [[int(i) for i in sys.stdin.readline().rstrip().split(" ")] for _ in range(N)]
res = 1e9
visited= [False] * N
solution(0, 0)
print(res)
