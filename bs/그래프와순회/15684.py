import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m, h = map(int, sys.stdin.readline().split())  # 세로, 가로, 세로선마다 가로선을 놓을수 있는 위치 수
graph = [[False]*(n+1) for _ in range(h+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split()) # 가로, 세로선
    graph[a][b] = True
def check():
    for i in range(1, n+1):
        now = i
        for j in range(1, h+1):
            if graph[j][now-1]:
                now -= 1
            elif graph[j][now]:
                now += 1
        if now != i:
            return False
    return True

def dfs(cnt,idx):
    global res
    if check():
        res = cnt
        return
    elif cnt == 3 or res <= cnt:
        return
    for i in range(idx, len(combi)):
        x, y = combi[i]
        if not graph[x][y-1] and not graph[x][y+1]: # 양쪽 연결 안되어 있으면
            graph[x][y] = True # 방문 처리
            dfs(cnt+1, i+1) # 다음 꺼 재귀
            graph[x][y] = False # 방문 다시 미 처리


combi = []
for i in range(1,h+1):
    for j in range(1,n):
        if not graph[i][j-1] and not graph[i][j] and not graph[i][j+1]:
            combi.append([i, j])
# 가로선의 정보는 두 정수 a과 b로 나타낸다. (1 ≤ a ≤ H, 1 ≤ b ≤ N-1) b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미.

res = 4
dfs(0,0)
print(res if res < 4 else -1)

