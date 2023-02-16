import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N = int(input())

def bfs(map,x,y):
    queue =deque([(x,y)])
    map[x][y] = 0
    count = 1
    while queue:
        a, b = queue.popleft()
        for next_x, next_y in move:
            nx ,ny = a + next_x,  b + next_y
            if N > nx >= 0 and N > ny >= 0 and map[nx][ny] == 1:
                map[nx][ny] = 0
                queue.append((nx,ny))
                count += 1
    return count


move = [(1,0),( -1,0),(0,-1),(0,1)] #상,하,좌,우
map = [list(map(int,input())) for i in range(N)] # 예제 입력
res= []
block = 0
for x in range(len(map)):
    for y in range(len(map)):
        if map[x][y] == 1:
            count = bfs(map,x,y)
            res.append(count)
            block += 1
res.sort()
print(block)
for i in res:
    print(i)
