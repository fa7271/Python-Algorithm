import heapq,sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n, m = map(int,input().split())

board = [list(map(int,input())) for _ in range(m)]
# 방문표시
visited = [[False] * n for _ in range(m)]
move = [(0,1),(0,-1),(1,0),(-1,0)]

heap = []
heapq.heappush(heap,(0, 0, 0)) # (부순횟수, x, y,)

res = 0
while heap:
    count, x, y = heapq.heappop(heap)
    # visited[x][y] = True
    # 마지막 지점 도착시 정답
    if x == m-1 and y == n-1 :
        print(count)
        break
    for dx, dy in move:
        nx = dx + x; ny = dy + y
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
            # 미로일때
            if board[nx][ny] == 1:
                visited[nx][ny] = True
                # 미로일때는 부숴야함 , 즉 count += 1
                heapq.heappush(heap,(count+1, nx, ny))
            # 미로가 아닐때
            else:
                visited[nx][ny] = True
                # 안 부수고 다음 칸으로 이동
                heapq.heappush(heap,(count,nx,ny))



