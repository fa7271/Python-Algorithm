import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')



N, M = map(int,input().split(" "))
map = [list(map(int,input())) for i in range(N)]

visited = [ [-1] * (M) for i in range(N)] # 밟은거 확인
move = [(1,0),( -1,0),(0,-1),(0,1)] #상,하,좌,우
visited[0][0] = 1
Q = deque([(0,0)])


while Q:
    x,y = Q.popleft()
    if x == N-1 and y == M-1:
        print(visited[x][y])
    for (a,b) in move:
        dx , dy = x + a, y + b
        if N > dx >= 0 and M > dy >= 0 and visited[dx][dy] == -1 and map[dx][dy] == 1:
            Q.append((dx,dy))
            visited[dx][dy] = visited[x][y] + 1





